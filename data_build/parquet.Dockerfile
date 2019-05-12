FROM python:3.7.3-slim-stretch
RUN apt-get update && apt-get install -y zstd
RUN pip install pyarrow
COPY --from=doublewick/boxball:csv-0.0.1 /data /data
