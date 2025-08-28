"""
Example reusable PySpark function for production use.
Place your shared logic here, import into notebooks as needed.
"""

from pyspark.sql import DataFrame

def clean_nulls(df: DataFrame, columns: list) -> DataFrame:
    """Remove rows where specified columns are null."""
    return df.dropna(subset=columns)