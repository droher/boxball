- Change repo name to containerball

- Validation container to help find bugs/discrepancies in Retrosheet data

- Potentially generate ddl in separate container

- Data bugs to notify Retrosheet about:
    - Repeat roster row in BRF1914.ROS (Felix Chouinard)
    - 5/28/2012 HOU-COL doubleheader not flagged as such
    - 1938 schedule file has blank line at the end

- Logic bugs to notify Chadwick Bureau about:
    - cwcomment issue handling multiline comment in 2007 ASG (about Soriano)
    - repeat entries in cwgame table (find specifics before sending)

- Targets to implement:
    - SQLite
    - Parquet (will require dtype mapper)
    - Flat file dumps (find good host, e.g. Mega/OneDrive)
    - Druid
    - Drill
    - Clickhouse
    - Presto
    - Superset (backed by one of the columnar stores above)
    - RStudio
    - Anaconda/Jupyter
    - Spark (1+ language, off Hive?)
    - Tensorflow
    - Keras
    - DataFusion
    - Gatsby/GraphQL/JAMstack site
    - Pyodide
    - CRAN/Pypi packages to download data dumps and load into dataframes
