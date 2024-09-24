import DBConnector




# SQL command to create a new table
sqlCommand = 'CREATE TABLE IF NOT EXISTS Martin_Porter_Table (MID VARCHAR, MName VARCHAR);'

# Execute the SQL command.
my_db.query(sqlCommand, '')
