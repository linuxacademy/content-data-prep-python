# populate_data.py

import pymongo
from connect_db import get_database_connection

DB_NAME = "contracts"

def populate_data():
    """
    Populate the data

    write code that will insert the given contract_list document into a collection
    """

    contract_list = [
        {"author": "Thompson, Keith", "title": "Oh Python! My Python!", "pages": "1200", "due_date": "2029-11-15"},
        {"author": "Fritts, Larry", "title": "Fun with Django", "pages": "150", "due_date": "2021-06-23"},
        {"author": "Applegate, John", "title": "When Bees Attack! The Horror!", "pages": "550", "due_date": "2020-12-10"},
        {"author": "Brown, James", "title": "Martin Buber's Philosophies", "pages": "700", "due_date": "0221-07-12"},
        {"author": "Smith, Jackson", "title": "The Sun Also Orbits", "pages": "400", "due_date": "2020-10-31"},
        {"author": "Smith, Jackson", "title": "The Sun Also Orbits", "pages": "600", "due_date": "2029-10-31"}
    ]

    
    pass # student code goes here

def test_populate_data():
    # Get db connection
    db = get_database_connection()

    contracts = db.contracts
    
    assert contracts.count_documents({}) == 6, 'The table does not have six rows.'

def main():
    populate_data()
    test_populate_data()
           
if __name__ == "__main__":
    main()
