import sqlite3
from connect_db import get_database_connection

DB_NAME = "demo"

def delete_data_from_db():
    """
    Delete selected data from database.

    execute the given sql statement to remove
    the extra data
    """
    
    sql_query = ''' DELETE FROM authors WHERE (author="Smith, Jackson" AND pages=400); '''
    
 

def update_data():
    """ Update the selected data.

    execute the given sql statement to 
    correct the due date of the entry
    """
    sql_query = ''' UPDATE authors SET due_date="2020-10-31" WHERE author="Smith, Jackson"; '''
    

def test_delete_data():
    sql_query = ''' SELECT count(author) FROM authors WHERE author="Smith, Jackson"; '''
    
     # make connection to db
    cxn = get_database_connection()

    # create a cursor to db
    cur = cxn.cursor()
        
    # send sql query to request
    cur.execute(sql_query)
    results = cur.fetchall()

    assert results[0][0] == 1, "the number of Smith Jackson rows is incorrect"

    # close database connection.
    cur.close()
    cxn.close() 

def test_update_data():
    sql_query = ''' SELECT due_date FROM authors WHERE author="Smith, Jackson"; '''
    
    # make connection to db
    cxn = get_database_connection()

    # create a cursor to db
    cur = cxn.cursor()
        
    # send sql query to request
    cur.execute(sql_query)
    results = cur.fetchall()

    assert results[0][0] == "2020-10-31", "due date not updated correctly"

    # close database connection.
    cur.close()
    cxn.close()  

def main():
    delete_data_from_db()
    test_delete_data()
    update_data()
    test_update_data()


           
if __name__ == "__main__":
    main()
