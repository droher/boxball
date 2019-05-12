- Build targets out of cleansed CSV that converts T/F to 1/0 and blanks to NULL

- Validation container/script to help find bugs/discrepancies in Retrosheet data

- Potentially generate ddl in separate container

- Data bugs to notify Retrosheet about:
    - Repeat roster row in BRF1914.ROS (Felix Chouinard)
    - 5/28/2012 HOU-COL doubleheader not flagged as such
    - 1938 schedule file has blank line at the end

- Logic bugs to notify Chadwick Bureau about:
    - cwcomment issue handling multiline comment in 2007 ASG (about Soriano)
    - repeat entries in cwdaily table (find specifics before sending)

- Targets to implement:
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

- Pyarrow steps in case I forget:
    - Establish Arrow schemas for each file (can just be a sqlalchemy -> arrow lookup dict)
    - Inflate csvs before starting the read (doesn't look like CompressedInputStream can do this correctly,
    so probably a better idea to either deflate the files in bash first or use the python zstandard library
    to inflate row-by-row.
    - Create a ParquetWriter with the schema for the file, put it in a with block
    - Under that block, loop: read x lines from a PythonFile CSV or the zstandard stream into a BufferedReader
    - Then use read_csv to create a table (using that schema)
    - Write the table to the ParquetWriter, repeat until no more data
    - x should be as large as we can get without causing OOM issues on a 2GB box 