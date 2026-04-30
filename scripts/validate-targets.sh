#!/usr/bin/env bash
# Boot each kept-target image, wait for the database to come up, run a known
# query against the loaded data, then tear it down. Intended as a deployment
# precondition: the release pipeline (and the e2e CI job) call this against
# the just-built `${REPO}:<target>-${VERSION}` images and refuse to publish if
# any target fails.
#
# Inputs:
#   VERSION (default 2026.0.0)
#   REPO    (default doublewick/boxball)
#
# Exit 0 = every target passed. Exit 1 = at least one failed.
#
# Each target gets a hard wallclock timeout per readiness probe. The probe is
# a polling query (not a log pattern) — robust to log-format drift across
# upstream image versions.

set -uo pipefail

VERSION="${VERSION:-2026.0.0}"
REPO="${REPO:-doublewick/boxball}"
RESULTS=()
FAIL=0

# Poll a command until it succeeds (returns 0). Times out at $2 seconds.
wait_for() {
  local desc="$1" timeout="$2"
  shift 2
  local start
  start=$(date +%s)
  while true; do
    if "$@" >/dev/null 2>&1; then
      return 0
    fi
    if [ $(($(date +%s) - start)) -gt "$timeout" ]; then
      echo "  TIMEOUT ${desc} after ${timeout}s"
      return 1
    fi
    sleep 2
  done
}

cleanup() {
  docker rm -f "$1" >/dev/null 2>&1 || true
}

run_target() {
  local target="$1"
  local name="boxball-validate-${target}"
  local image="${REPO}:${target}-${VERSION}"
  echo "=========================================="
  echo "TARGET: $target ($image)"
  echo "=========================================="
  cleanup "$name"
  case "$target" in
    postgres|postgres-columnar)
      docker run -d --name "$name" -e POSTGRES_PASSWORD=postgres "$image" >/dev/null
      wait_for "postgres ready" 600 \
        docker exec "$name" pg_isready -U postgres -d postgres || { cleanup "$name"; return 1; }
      # initdb opens to client traffic before init scripts (the load) finish.
      # Poll until baseballdatabank.teams has rows. A bare SELECT exits 0
      # against an empty table, so the previous probe could declare success
      # mid-load; require the result to actually contain '1'.
      wait_for "teams loaded" 600 \
        bash -c "docker exec \"$name\" psql -U postgres -tAc \"SELECT 1 FROM baseballdatabank.teams LIMIT 1\" 2>/dev/null | grep -q 1" || {
          cleanup "$name"; return 1; }
      out=$(docker exec "$name" psql -U postgres -tAc \
        "SELECT count(*) FROM information_schema.tables WHERE table_schema='baseballdatabank'" 2>&1)
      echo "  baseballdatabank tables: $out"
      [[ "$out" =~ ^[0-9]+$ ]] && [ "$out" -gt 0 ] || { cleanup "$name"; return 1; }
      out=$(docker exec "$name" psql -U postgres -tAc \
        "SELECT count(*) FROM baseballdatabank.teams" 2>&1)
      echo "  teams row count: $out"
      [[ "$out" =~ ^[0-9]+$ ]] && [ "$out" -gt 0 ] || { cleanup "$name"; return 1; }
      ;;
    mysql)
      docker run -d --name "$name" -e MYSQL_ALLOW_EMPTY_PASSWORD=yes "$image" >/dev/null
      wait_for "mysql up" 900 \
        docker exec "$name" mysql -uroot -e "SELECT 1" || { cleanup "$name"; return 1; }
      wait_for "teams loaded" 900 \
        bash -c "docker exec \"$name\" mysql -uroot -N -e \"SELECT 1 FROM baseballdatabank.teams LIMIT 1\" 2>/dev/null | grep -q 1" || {
          cleanup "$name"; return 1; }
      out=$(docker exec "$name" mysql -uroot -N -e \
        "SELECT count(*) FROM information_schema.tables WHERE table_schema='baseballdatabank'" 2>&1)
      echo "  baseballdatabank tables: $out"
      [[ "$out" =~ ^[0-9]+$ ]] && [ "$out" -gt 0 ] || { cleanup "$name"; return 1; }
      out=$(docker exec "$name" mysql -uroot -N -e \
        "SELECT count(*) FROM baseballdatabank.teams" 2>&1)
      echo "  teams row count: $out"
      [[ "$out" =~ ^[0-9]+$ ]] && [ "$out" -gt 0 ] || { cleanup "$name"; return 1; }
      ;;
    sqlite)
      docker run -d --name "$name" "$image" >/dev/null
      # ENTRYPOINT streams `zstd -d` into /db/boxball.db (8.7GB), then starts
      # sqlite_web. Probing for non-empty file picks up the partially-written
      # output mid-stream and yields "database disk image is malformed".
      # `zstd --rm` deletes the source on a clean decompress, so absence of
      # /tmp/boxball.db.zst is the right "DB is whole" signal.
      wait_for "sqlite db ready" 600 \
        bash -c "docker exec \"$name\" sh -c '! test -e /tmp/boxball.db.zst'" || { cleanup "$name"; return 1; }
      out=$(docker exec "$name" sqlite3 /db/boxball.db \
        "SELECT count(*) FROM sqlite_master WHERE type='table' AND name LIKE 'baseballdatabank_%'" 2>&1)
      echo "  baseballdatabank tables: $out"
      [[ "$out" =~ ^[0-9]+$ ]] && [ "$out" -gt 0 ] || { cleanup "$name"; return 1; }
      out=$(docker exec "$name" sqlite3 /db/boxball.db \
        "SELECT count(*) FROM baseballdatabank_teams" 2>&1)
      echo "  teams row count: $out"
      [[ "$out" =~ ^[0-9]+$ ]] && [ "$out" -gt 0 ] || { cleanup "$name"; return 1; }
      ;;
    clickhouse)
      docker run -d --name "$name" --ulimit nofile=262144:262144 "$image" >/dev/null
      wait_for "clickhouse up" 600 \
        docker exec "$name" clickhouse-client --query "SELECT 1" || { cleanup "$name"; return 1; }
      wait_for "teams loaded" 600 \
        bash -c "docker exec \"$name\" clickhouse-client --query \"SELECT 1 FROM baseballdatabank.teams LIMIT 1\" 2>/dev/null | grep -q 1" || { cleanup "$name"; return 1; }
      out=$(docker exec "$name" clickhouse-client --query \
        "SELECT count() FROM system.tables WHERE database='baseballdatabank'" 2>&1)
      echo "  baseballdatabank tables: $out"
      [[ "$out" =~ ^[0-9]+$ ]] && [ "$out" -gt 0 ] || { cleanup "$name"; return 1; }
      out=$(docker exec "$name" clickhouse-client --query \
        "SELECT count() FROM baseballdatabank.teams" 2>&1)
      echo "  teams row count: $out"
      [[ "$out" =~ ^[0-9]+$ ]] && [ "$out" -gt 0 ] || { cleanup "$name"; return 1; }
      ;;
    *) echo "unknown target $target"; return 1 ;;
  esac
  cleanup "$name"
  return 0
}

for target in postgres postgres-columnar mysql sqlite clickhouse; do
  if run_target "$target"; then
    RESULTS+=("PASS  $target")
  else
    RESULTS+=("FAIL  $target")
    FAIL=1
  fi
  echo ""
done

echo "=========================================="
echo "SUMMARY"
echo "=========================================="
for r in "${RESULTS[@]}"; do
  echo "  $r"
done
exit "$FAIL"
