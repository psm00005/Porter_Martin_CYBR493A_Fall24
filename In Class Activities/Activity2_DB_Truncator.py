import DBConnector


# Create a new instance of the DB
my_db = DBConnector.MyDB()

# SQL command to create a new table
sqlCommand = 'DROP TABLE Martin_Porter_Table;'

# Execute the SQL command.
my_db.query(sqlCommand, '')
