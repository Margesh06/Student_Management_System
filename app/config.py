import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve MongoDB URI and Database name from environment variables
mongo_uri = os.getenv("MONGODB_URI") 
database_name = os.getenv("DATABASE_NAME") 

# Check if environment variables are loaded correctly
if not mongo_uri or not database_name:
    raise ValueError("Environment variables for MongoDB are not set correctly.")

# Database connection
client = MongoClient(mongo_uri)
db = client[database_name]

def init_db():
    print("Connected to MongoDB Atlas")
