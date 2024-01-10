from sqlalchemy import create_engine, MetaData
import os

# Database URL from .env file
DATABASE_URL = os.environ['DATABASE_URL']

# Connect to the database
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Load the schema from the database
metadata.reflect(engine)

# Initialize a dictionary to hold schema information and data
schema_info = {}

# Number of records to fetch from each table
record_limit = 5  # Adjust as needed

for table in metadata.tables.values():
    table_name = table.name
    excluded_columns = []  # Define the columns to exclude (e.g., columns with byte data)
    table_info = {
        "columns": [],
        "relationships": [],
        "excluded_columns": [],  # Add this line to include excluded columns info
        "data": []  # Using a key "data" to store records
    }

    # Collect columns and identify columns with byte data
    for column in table.c:
        column_info = {
            "name": column.name,
            "type": str(column.type)
        }
        table_info["columns"].append(column_info)
        
        # Exclude byte data columns
        if 'BLOB' in str(column.type).upper() or 'BYTEA' in str(column.type).upper():
            excluded_columns.append(column.name)

    # Add excluded columns to table_info
    table_info["excluded_columns"] = excluded_columns

    # Fetch a few records from the table
    with engine.connect() as connection:
        result = connection.execute(table.select().limit(record_limit)).fetchall()
        for row in result:
            row_data = dict(row)
            # Remove excluded columns from the row data
            for col in excluded_columns:
                row_data.pop(col, None)
            table_info["data"].append(row_data)  # Append the row data to the 'data' key

    # Add table information to schema info
    schema_info[table_name] = table_info

# Now, schema_info variable contains schema details and data named after each table
# You can print it to see the structure
print(schema_info)
