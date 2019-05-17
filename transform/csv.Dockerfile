# The CSV for now is unchanged from the extract, but if we want to add further cleaning steps, we can place them
# here without doing further downstream refactoring.
FROM alpine:3.9.3
ARG REPO
ARG VERSION
COPY --from=${REPO}:extract-${VERSION} /extract /transform/csv