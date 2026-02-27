import os
from pymongo import MongoClient

MONGODB_ATLAS_URL = os.getenv("MONGODB_ATLAS_URL")
MONGODB_ATLAS_USER = os.getenv("MONGODB_ATLAS_USER")
MONGODB_ATLAS_PWD = os.getenv("MONGODB_ATLAS_PWD")

def main():
    client = MongoClient(
        MONGODB_ATLAS_URL,
        username=MONGODB_ATLAS_USER,
        password=MONGODB_ATLAS_PWD,
        serverSelectionTimeoutMS=5000
    )

    db = client.bookstore
    authors = db.authors

    total = authors.count_documents({})
    print(f"Total authors: {total}\n")

    for author in authors.find({}, {"name": 1, "nationality": 1, "birthday": 1, "_id": 0}):
        print(f"{author['name']} ({author['nationality']}) - Birthday: {author.get('birthday', 'N/A')}")

    # Close connection
    client.close()

if __name__ == "__main__":
    main()