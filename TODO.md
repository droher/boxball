- Implement a serialization step to validate data before
loading it into any of the target interfaces.
    - Potentially use Parquet as the final format for the
    data pre-target to leverage compression, and then have
    the first part of the target builds expand to csv