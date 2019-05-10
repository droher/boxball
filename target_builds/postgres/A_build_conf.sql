-- Built (then modified) using https://pgtune.leopard.in.ua/ with these settings:
-- DB Version: 11
-- OS Type: linux
-- DB Type: dw
-- Total Memory (RAM): 2 GB
-- CPUs num: 1
-- Connections num: 20
-- Data Storage: ssd

-- Substitute your own as you see fit. See `z_run_conf` in this folder for settings that
-- are tuned for querying rather than copying after the load is over.

ALTER SYSTEM SET
 max_connections = '20';
ALTER SYSTEM SET
 shared_buffers = '512MB';
ALTER SYSTEM SET
 effective_cache_size = '1GB';
ALTER SYSTEM SET
 maintenance_work_mem = '1GB';
ALTER SYSTEM SET
 checkpoint_completion_target = '0.9';
ALTER SYSTEM SET
 wal_buffers = '16MB';
ALTER SYSTEM SET
 default_statistics_target = '500';
ALTER SYSTEM SET
 random_page_cost = '1.1';
ALTER SYSTEM SET
 effective_io_concurrency = '200';
ALTER SYSTEM SET
 work_mem = '1GB';
ALTER SYSTEM SET
 min_wal_size = '4GB';
ALTER SYSTEM SET
 max_wal_size = '12GB';
ALTER SYSTEM SET
 checkpoint_timeout = '3600';
