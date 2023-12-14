<p align="center">
<img src="./assets/boxball.jpg" width="50%">
</p>
<p align="center">
<img alt="GitHub release" src="https://img.shields.io/github/release/droher/boxball.svg">
<a href="https://circleci.com/gh/droher/boxball">
    <img src="https://circleci.com/gh/droher/boxball.svg?style=shield&circle-token=2b78bfd4c600c640c479f2f2d9eaa38823ad8b96"/>
</a>
<a href="https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=droher/boxball&amp;utm_campaign=Badge_Grade">
    <img src="https://api.codacy.com/project/badge/Grade/9a163160d3db4621b941b3297bfb9edf"/>
</a>
<a href="https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=droher/boxball&amp;utm_campaign=Badge_Coverage">
    <img src="https://api.codacy.com/project/badge/Coverage/9a163160d3db4621b941b3297bfb9edf"/>
</a>
<img alt="Docker Pulls" src="https://img.shields.io/docker/pulls/doublewick/boxball.svg">
<a href="https://opensource.org/licenses/Apache-2.0">
    <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" /></a>
<br>
</p>

**Update**: I have released a new project, [baseball.computer](https://baseball.computer), which is designed
as the successor to boxball. It is much easier to use (no Docker required, runs entirely in your browser/program)
and includes many more tables, features, and quality controls. The event schema is different, which will be the main migration pain point in
migration. _I aim to continue Boxball maintenence and updates as long as people are still using it,_ and I may try to rebase
boxball on top of the new project to make maintaining both easier. Please let me know if there are things you can do in Boxball that you can't do yet in baseball.computer by filing an issue on the [repo](https://github.com/droher/baseball.computer) or reaching me at david.roher@baseball.computer. 

## Introduction
**Boxball** creates prepopulated databases of the two most significant open source baseball datasets:
[Retrosheet](http://retrosheet.org) and the [Baseball Databank](https://github.com/chadwickbureau/baseballdatabank).
Retrosheet contains information on every major-league pitch since 2000, every play since 1928,
every box score since 1901, and every game since 1871.
The Databank (based on the [Lahman Database](http://www.seanlahman.com/baseball-archive/statistics/)) contains yearly
summaries for every player and team in history. In addition to the data and databases themselves, Boxball relies on the following tools:
*   [Docker](https://docs.docker.com/engine/docker-overview/) for repeatable builds and easy distribution
*   [SQLAlchemy](https://www.sqlalchemy.org/) for abstracting away DDL differences between databases
*   [Chadwick](https://github.com/chadwickbureau/chadwick) for translating Retrosheet's complex event files into a relational format

Follow the instructions below to install your distribution of choice. The full set of images is also available on
Docker Hub.

The Retrosheet schema is extensively documented in the code; see the source [here](https://github.com/droher/boxball/blob/master/transform/src/schemas/retrosheet.py)
until I find a prettier solution.

If you find the project useful, please consider donating to:
*   The [Ali Forney Center](https://aliforneycenter.donordrive.com/index.cfm?fuseaction=donate.general) for homeless LGBTQ youth
*   [350.org](https://act.350.org/donate/build/), a grassroots international climate change organization

Feel free to [contact me](mailto:david@boxball.io) with questions or comments! 

## Requirements
*   [Docker](https://docs.docker.com/install/) (v18.06, earlier versions may not work)
*   2-20GB Disk space (depends on distribution choice)
*   500MB-8GB RAM available to Docker (depends on distribution choice)

## Distributions
### Column-Oriented Databases
#### Postgres cstore_fdw (Recommended)
This distribution uses the [cstore_fdw](https://github.com/citusdata/cstore_fdw) extension to turn PostgreSQL
into a column-oriented database. This means that you get the rich featureset of Postgres,
but with a huge improvement in speed and disk usage. To install and run the database server:

`docker run --name postgres-cstore-fdw -d -p 5433:5432 -e POSTGRES_PASSWORD="postgres" -v ~/boxball/postgres-cstore-fdw:/var/lib/postgresql/data doublewick/boxball:postgres-cstore-fdw-latest`

Roughly an hour after the image is downloaded, the data will be fully loaded into the database, and you can connect to it as the user `postgres`
with password `postgres` on port `5433`
(either using the `psql` command line tool or a database client of your choice). The data will be persisted on your machine in
`~/boxball/postgres-cstore-fdw` (~1.5GB), which means you can stop/remove the container without having to reload the data
when you turn it back on.

#### Clickhouse
[Clickhouse](https://clickhouse.yandex/) is a database developed by Yandex with some very impressive performance benchmarks. It uses less
disk space than Postgres cstore_fdw, but significantly more RAM (~5GB). I've yet to run any query performance comparisons.
To install and run the database server:

`docker run --name clickhouse -d -p 8123:8123 -v ~/boxball/clickhouse:/var/lib/clickhouse doublewick/boxball:clickhouse-latest`

15-30 minutes after the image is downloaded, the data will be fully loaded into the database, and you can connect to it either by attaching the
container and using the `clickhouse-client` CLI or by using a local database client on port `8123` as the user `default`. 
The data will be persisted on your machine in
`~/boxball/clickhouse` (~700MB), which means you can stop/remove the container without having to reload the data
when you turn it back on.

#### Drill
[Drill](https://drill.apache.org/) is a framework that allows for SQL queries directly on files, without having to declare any schema.
It is usually used on a computing cluster with massive datasets, but we use a single-node setup. To install and run:

`docker run --name drill -id -p 8047:8047 -p 31010:31010 -v ~/boxball/drill:/data doublewick/boxball:drill-latest`
 
Data will be immediately available to query after the image is downloaded. Use port `8047` to access the Web UI 
(which includes a SQL runner) and port `31010` to connect via a database client.
You may also attach the container and query from the command line.
The data will be persisted on your machine in `~/boxball/drill` (~700MB).

### Traditional (Row-oriented) Databases
Note: these frameworks are likely to be prohibitively slow when querying play-by-play data, and they take up significantly
more disk space than their columnar counterparts.
#### Postgres
Similar configuration to the cstore_fdw extended version above, but stored in the conventional way.

`docker run --name postgres -d -p 5432:5432 -e POSTGRES_PASSWORD="postgres" -v ~/boxball/postgres:/var/lib/postgresql/data doublewick/boxball:postgres-latest`

Roughly 90 minutes after the image is downloaded, the data will be fully loaded into the database,
and you can connect to it as the user `postgres` with password `postgres` on port `5432`
(either using the `psql` command line tool or a database client of your choice). The data will be persisted on your machine in
`~/boxball/postgres` (~12GB), which means you can stop/remove the container without having to reload the data
when you turn it back on.

#### MySQL
To install and run:

`docker run --name mysql -d -p 3306:3306 -v ~/boxball/mysql:/var/lib/mysql doublewick/boxball:mysql-latest`

Roughly two hours after the image is downloaded, the data will be fully loaded into the database,
and you can connect to it as the user `root` on port `3306`. The data will be persisted on your machine in
`~/boxball/mysql` (~12GB), which means you can stop/remove the container without having to reload the data
when you turn it back on.

#### SQLite (with web UI)
To install and run:

`docker run --name sqlite -d -p 8080:8080 -v ~/boxball/sqlite:/db doublewick/boxball:sqlite-latest`

Roughly two minutes after the image is downloaded, the data will be fully loaded into the database. `localhost:8080`
will provide a [web UI](https://github.com/coleifer/sqlite-web) where you can write queries and perform schema exploration.

### Flat File Downloads

#### Parquet
Parquet is a columnar data format originally developed for the Hadoop ecosystem. It has solid support in Spark, Pandas,
and many other frameworks.
[OneDrive](https://1drv.ms/u/s!AtpEocFNRNBWhAqZMaj40Bb8__6u?e=dNJiod)

#### CSV
The original CSVs from the extract step (each CSV file is compressed in the ZSTD format).
[OneDrive](https://1drv.ms/u/s!AtpEocFNRNBWhDLuZqcmXYOIieKQ?e=xP4Azs)

## Acknowledgements
Ted Turocy's [Chadwick Bureau](http://chadwick-bureau.com/) developed the tools and repos that made this project possible. I am also grateful to [Sean
Lahman](http://www.seanlahman.com/) for creating his database, which I have been using for over 15 years. I was able
to develop and host this project for free thanks to the generous open-source plans of [Jetbrains](https://www.jetbrains.com/?from=boxball), CircleCI, Github, and Docker Hub.

Retrosheet represents the collective effort of thousands of baseball fans over 150 years of scorekeeping and data entry.
I hope Boxball facilitates more historical research to continue this tradition.

## Licence(s)
All code is released under the Apache 2.0 license. Baseball Databank data is distributed under the [CC-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
license. Retrosheet data is released under the condition that the below text appear prominently:

``` 
The information used here was obtained free of
charge from and is copyrighted by Retrosheet.  Interested
parties may contact Retrosheet at "www.retrosheet.org".
```
