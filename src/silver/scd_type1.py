from pyspark.sql import SparkSession

def apply_scd_type1(spark: SparkSession):
    """
    SCD Type 1: Overwrites existing data. 
    Use this for correcting errors (e.g., fixing a misspelled name).
    """
    print("Applying SCD Type 1 (Overwrite)...")
    
    # This logic updates the target whenever the source ID matches,
    # simply replacing old values with new ones.
    spark.sql("""
        MERGE INTO workspace.dwh_silver.silver_table AS target
        USING bronze_view AS source
        ON target.order_id = source.order_id
        WHEN MATCHED THEN 
            UPDATE SET target.customer_name = source.customer_name
    """)
    print("SCD Type 1 Applied.")

