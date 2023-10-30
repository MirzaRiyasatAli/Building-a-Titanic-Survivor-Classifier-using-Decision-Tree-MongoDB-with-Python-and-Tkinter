import pymongo
import pandas as pd
from pymongo import MongoClient


def save_dataframe_to_mongodb(dataframe, db_name, collection_name, mongo_uri='mongodb://localhost:27017/'):
    """
    Save a Pandas DataFrame into a MongoDB collection.

    Parameters:
    - dataframe: The Pandas DataFrame to be saved.
    - db_name: Name of the MongoDB database.
    - collection_name: Name of the MongoDB collection.
    - mongo_uri: The MongoDB URI (default is 'mongodb://localhost:27017/').
    """
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    # Convert the DataFrame to a list of dictionaries (JSON-like)
    data = dataframe.to_dict(orient='records')

    # Insert the data into the collection
    collection.insert_many(data)


# Define the function to load data from MongoDB
def load_dataframe_from_mongodb(db_name, collection_name, mongo_uri='mongodb://localhost:27017/'):
    """
    Load data from a MongoDB collection into a Pandas DataFrame.

    Parameters:
    - db_name: Name of the MongoDB database.
    - collection_name: Name of the MongoDB collection.
    - mongo_uri: The MongoDB URI (default is 'mongodb://localhost:27017/').

    Returns:
    - Pandas DataFrame containing the data from the specified collection.
    """
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    # Retrieve all documents from the collection
    cursor = collection.find({})

    # Convert the documents to a list of dictionaries
    data = list(cursor)

    # Create a DataFrame from the list of dictionaries
    dataframe = pd.DataFrame(data)

    return dataframe

