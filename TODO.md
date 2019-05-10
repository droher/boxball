- Implement a serialization step to validate data before
loading it into any of the target interfaces.
    - Potentially use Parquet as the final format for the
    data pre-target to leverage compression, and then have
    the first part of the target builds expand to csv

- Data bugs to notify Retrosheet about:
    - Repeat roster row in BRF1914.ROS (Felix Chouinard)
    - 5/28/2012 HOU-COL doubleheader not flagged as such
    - 1938 schedule file has blank line at the end

- Logic bugs to notify Chadwick Bureau about:
    - cwcomment issue handling multiline comment in 2007 ASG (about Soriano)
