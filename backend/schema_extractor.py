from sqlalchemy import create_engine, MetaData
from flask import Flask, request, jsonify

# Replace with your actual database URL
DATABASE_URL = "mysql+pymysql://root:root@localhost/sakila"

# Connect to the database
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Load the schema from the database
metadata.reflect(engine)

# Initialize a dictionary to hold schema information
schema_info = {}

# Collect tables, columns, and relationships
for table in metadata.tables.values():
    table_info = {
        "columns": [],
        "relationships": []
    }

    # Collect columns
    for column in table.c:
        column_info = {
            "name": column.name,
            "type": str(column.type)
        }
        table_info["columns"].append(column_info)

    # Collect relationships (foreign keys)
    for fk in table.foreign_keys:
        rel_info = {
            "column": fk.parent.name,
            "references": {
                "table": fk.column.table.name,
                "column": fk.column.name
            }
        }
        table_info["relationships"].append(rel_info)

    # Add table information to schema info
    schema_info[table.name] = table_info

# Now, schema_info variable contains all the schema details
# You can print it to see the structure
#print(schema_info)