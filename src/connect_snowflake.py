import os
from dotenv import load_dotenv
import snowflake.connector
import pandas as pd

load_dotenv()

# Use the actual Snowflake database/schema names created for this project.
conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE", "HR_ATTRITION"),
    schema=os.getenv("SNOWFLAKE_SCHEMA", "RAW"),
)

query = "SELECT * FROM HR_ATTRITION.RAW.HR_ATTRITION_FINAL;"

df = pd.read_sql(query, conn)

print("Data successfully loaded!")
print(f"Dataset Shape: {df.shape}")
print(df.head())

conn.close()