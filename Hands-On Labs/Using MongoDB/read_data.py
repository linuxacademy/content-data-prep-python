import pymongo
from connect_db import get_database_connection

DB_NAME = "contracts"
COLLECTION = "contracts"

def read_data_from_db():
    """
    Read all documents from the collection.

    """
    

def main():
    results = read_data_from_db()
    assert results, "No results found!"

    # Provide the data in readable format
    print(f"Author\tTitle\tDue Date\t\n")
    for item in results:
        print(f"{item['author']}\t{item['title']}\t{item['due_date']}\n")

           
if __name__ == "__main__":
    main()
