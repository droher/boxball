FROM python:3.7.3-slim-stretch AS build-ddl
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONPATH="/"

FROM build-ddl as build-parquet
RUN pip install pyarrow
COPY --from=doublewick/boxball:csv-latest /data /data
RUN pip install pandas
COPY src/ src/
RUN python -u src/parquet.py
RUN python -u src/ddl_maker.py


FROM alpine:3.9.3
COPY --from=build-parquet /ddl /ddl
COPY --from=build-parquet /data /data
