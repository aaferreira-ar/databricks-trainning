import dlt
from pyspark.sql.functions import col
from utilities import utils

# This file defines a sample transformation.
# Edit the sample below or add new transformations
# using "+ Add" in the file browser.

@dlt.table
def sales():
    """
    Reads sales 
    """
    path = "/Volumes/lakehouse/lab_aaferreira_lab06/files/dlt/sales/*.csv"

    schema = """
        customer_id INTEGER,
        sale_date DATE,
        product STRING,
        quantity INTEGER,
        value DECIMAL(10,2)
    """

    return (
        spark.readStream.schema(schema)
            .format("csv")
            .option("header", "true")
            .load(path)
    )
