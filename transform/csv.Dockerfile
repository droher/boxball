# The CSV for now is unchanged from the extract, but if we want to add further cleaning steps, we can place them
# here without doing further downstream refactoring.
FROM doublewick/boxball:extract-0.0.1 as extract
FROM alpine:3.9.3
COPY --from=extract /extract /transform/csv