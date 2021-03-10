# create_table.py

import psycopg2
from connect_db import get_database_connection

DB_NAME = "demo"

def create_table():
    """
    Creates a table ready to accept our data.

    write code that will execute the given sql statment
    on the database
    """

    create_table = """ CREATE TABLE IF NOT EXISTS authors(
        ID          SERIAL              PRIMARY KEY,
        author      TEXT                NOT NULL,
        title       TEXT                NOT NULL,
        pages       INTEGER             NOT NULL,
        due_date    CHAR(15)            NOT NULL
    );   
    """

    pass # student code goes here


def populate_table():
    """
    Populate the table database.

    write code that will use the given sql statement to populate
    the new table with the contract_list data
    """

    contract_list = [
    ["Thompson, Keith", "Oh Python! My Python!", 1200, "2029-11-15"],
    ["Fritts, Larry", "Fun with Django", 150, "2021-06-23"],
    ["Applegate, John", "When Bees Attack! The Horror!", 550, "2020-12-10"],
    ["Brown, James", "Martin Buber's Philosophies", 700, "0221-07-12"],
    ["Smith, Jackson", "The Sun Also Orbits", 400, "2020-10-31"],
    ["Smith, Jackson", "The Sun Also Orbits", 600, "2029-10-31"]
]

    add_data_stmt = ''' INSERT INTO authors(author,title,pages,due_date) VALUES(?,?,?,?); '''

    pass # student code goes here

def test_table_created():
    """ 
    Test table was created.
    """
    
    test_stmt = ''' SELECT count(name) FROM authors; '''
    
    # get connection and cursor to db
    cxn = get_database_connection()
    cur = cxn.cursor()
        
    # send sql query to request
    cur.execute(test_stmt)
    cxn.commit()
    
    assert cur.fetchone()[0] == 1, 'table does not exist.'

    # close database connection.
    cur.close()
    cxn.close()

def test_populate_table():
    # Get connection and cursor to db
    cxn = get_database_connection()
    cur = cxn.cursor()
    
    cur.execute("select * from authors;")
    results = cur.fetchall()

    assert len(results) == 6, 'The table does not have six rows.'

    cur.close()
    cxn.close()

def main():
    create_table()
    test_table_created()
    populate_table()
    test_populate_table()
           
if __name__ == "__main__":
    main()
