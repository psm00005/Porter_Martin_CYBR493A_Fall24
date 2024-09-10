"""
This class tests the connection to your DB by creating a test table
"""
# Import the connector class
import DBConnector

# Create a new instance of the DB
my_db = DBConnector.MyDB()

# SQL command to create a new table
#sqlCommand = 'CREATE TABLE IF NOT EXISTS TEST (TEST_ID  VARCHAR, TEST_NAME  VARCHAR);'
sqlCommand = 'TRUNCATE TABLE TEST;'


# Message to display upon table creation. Not integrated yet.
sqlMessage = 'Table Test created successfully. Please access pgAdmin to verify table was created successfully'

# Execute the SQL command.
my_db.query(sqlCommand, '')
