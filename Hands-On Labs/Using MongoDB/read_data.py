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
        print(f"{item[0]}\t{item[1]}\t{item[2]}\n")

           
if __name__ == "__main__":
    main()
