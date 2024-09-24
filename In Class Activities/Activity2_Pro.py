"""
Porter Martin
9/24/2024
Activity #2 like a pro
"""
import DBConnector
from Porter_Martin_CYBR493A_Fall24.Training.DBTester import my_db


def CreateTheTable(my_db):
    """
    This method creates the table we need for this activity
    :return: N/A
    """
    # Create a new instance of the DB
    my_db = DBConnector.MyDB()

    # SQL command to create a new table
    sqlCommand = 'CREATE TABLE IF NOT EXISTS Martin_Porter_Table (MID VARCHAR, MName VARCHAR);'

    # Execute the SQL command.
    my_db.query(sqlCommand, '')

def DropTheTable(my_db):
    """
    This method drops the table we created earlier for this activity
    :return: N/A
    """
    # Create a new instance of the DB
    my_db = DBConnector.MyDB()

    # SQL command to create a new table
    sqlCommand = 'DROP TABLE Martin_Porter_Table;'

    # Execute the SQL command.
    my_db.query(sqlCommand, '')

def main():
    # Create a new instance of the DB
    my_db = DBConnector.MyDB()

    CreateTheTable(my_db)
    sqlStatement = 'INSERT INTO MARTIN_PORTER_TABLE VALUES(%s,%s);'
    my_db.query(sqlStatement,('1', 'One'))
    my_db.query(sqlStatement,('2', 'Whopper'))
    my_db.query(sqlStatement,('3', 'Burger'))




    DropTheTable(my_db)


if __name__ == "__main__":
    main()