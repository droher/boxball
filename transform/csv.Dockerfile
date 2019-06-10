# The CSV for now is unchanged from the extract, but if we want to add further cleaning steps, we can place them
# here without doing further downstream refactoring.
ARG VERSION
FROM doublewick/boxball:extract-${VERSION} as extract

FROM alpine:3.9.3
COPY --from=extract /extract /transform/csv