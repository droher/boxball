<p align="center">
<img src="./assets/boxball.jpg" width="50%">
</p>
<p>
<a href="https://circleci.com/gh/droher/boxball">
    <img src="https://circleci.com/gh/droher/boxball.svg?style=shield&circle-token=2b78bfd4c600c640c479f2f2d9eaa38823ad8b96" align="left" />
</a>
<a href="https://codecov.io/gh/droher/boxball">
  <img src="https://codecov.io/gh/droher/boxball/branch/master/graph/badge.svg?token=EFOhQUQcHk" align="left" />
</a>
<br>
</p>

## Introduction
Boxball creates prepopulated databases of the two most significant open source baseball datasets: Retrosheet and the
Baseball Databank. Retrosheet contains information on every major-league pitch since 2000, every play since 1937,
every box score since 1906, and every game since 1871. The Databank (also known as the Lahman Database) contains yearly
summaries for every player and team in history. In addition to the data and databases themselves, Boxball relies on the following tools:
 * Docker for repeatable builds and easy distribution
 * SQLAlchemy for abstracting away DDL differences between databases
 * Chadwick for translating Retrosheet's complex event files into a relational format

Follow the instructions below to install your distribution of choice. The full set of images is also available on
Docker Hub.

If you find the project useful, please consider donating to:
* The [Ali Forney Center](https://aliforneycenter.donordrive.com/index.cfm?fuseaction=donate.general) for homeless LGBTQ youth
* [350.org](https://act.350.org/donate/build/), a grassroots international climate change organization

Feel free to [contact me](mailto:david@boxball.io) with questions or comments! 

## Requirements
* Docker (v18.06, earlier versions may not work)
* 2-20GB Disk space (depends on distribution choice)
* 500MB-8GB RAM available to Docker (depends on distribution choice)
## Distributions
### Column-Oriented Databases
#### Postgres cstore_fdw (Top choice)
This distribution uses the `cstore_fdw` extension to turn PostgreSQL into a column-oriented database. This means that you
get the rich featureset of Postgres, but with a huge improvement in speed and disk usage. To install the database, run:

`docker run doublewick/boxball:postgres-cstore-fdw-0.0.2 -v ~/boxball/postgres-cstore-fdw`
## Acknowledgements

