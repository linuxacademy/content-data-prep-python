import sqlite3
from connect_db import get_database_connection

DB_NAME = "contracts"

def read_data_from_db():
    """
    Read data from database.

    execute the given sql statement and return the results
    """
    
    sql_query = ''' SELECT author,title,due_date FROM authors; '''
      

def test_read_data(results):
    expected = [('Thompson, Keith', 'Oh Python! My Python!', '2029-11-15'), ('Fritts, Larry', 'Fun with Django', '2021-06-23'), ('Applegate, John', 'When Bees Attack! The Horror!', '2020-12-10'), ('Brown, James', "Martin Buber's Philosophies", '0221-07-12'), ('Smith, Jackson', 'The Sun Also Orbits', '2020-10-31'), ('Smith, Jackson', 'The Sun Also Orbits', '2029-10-31')]  
    assert results == expected, "the results do not match the expected"

def main():
    results = read_data_from_db()
    test_read_data(results)

    # Provide the data in readable format
    print(f"Author\tTitle\tDue Date\t\n")
    for item in results:
        print(f"{item[0]}\t{item[1]}\t{item[2]}\n")

           
if __name__ == "__main__":
    main()
