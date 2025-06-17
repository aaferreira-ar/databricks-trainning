import dlt
from pyspark.sql.functions import col
from utilities import utils

# This file defines a sample transformation.
# Edit the sample below or add new transformations
# using "+ Add" in the file browser.

@dlt.table
def customers():
    """
    Reads customers 
    """
    path = "/Volumes/lakehouse/lab_aaferreira_lab06/files/dlt/customers/*.csv"

    schema = """
        customer_id INTEGER,
        customer_name STRING,
        email STRING,
        address STRING,
        city STRING,
        state STRING,
        zip STRING,
        phone STRING
    """

    return (
        spark.readStream.schema(schema)
            .format("csv")
            .option("header", "true")
            .load(path)
    )
