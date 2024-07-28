from dotenv import load_dotenv
import os
load_dotenv()
from pymongo import MongoClient


# 
CONNECTION_URI=os.getenv("CONNECTION_URI")
ADMIN_DB_NAME=os.getenv("ADMIN_DB_NAME")
STATION_COLLECTION_NAME=os.getenv("STATION_COLLECTION_NAME")
TRAIN_COLLECTION_NAME=os.getenv("TRAIN_COLLECTION_NAME")
VENDOR_COLLECTION_NAME=os.getenv("VENDOR_COLLECTION_NAME")
CUSTOMERS_DB_NAME=os.getenv("CUSTOMERS_DB_NAME")
CUSTOMERS_COLLECTION_NAME=os.getenv("CUSTOMERS_COLLECTION_NAME")
VENDORS_DB_NAME=os.getenv("VENDORS_DB_NAME")
FOOD_COLLECTION_NAME=os.getenv("FOOD_COLLECTION_NAME")
ORDER_COLLECTION_NAME=os.getenv("ORDER_COLLECTION_NAME")


# Setup MongoDB connection
client = MongoClient(CONNECTION_URI)

# Access the specific databases and collections
admin_db = client[ADMIN_DB_NAME]
customers_db = client[CUSTOMERS_DB_NAME]
vendors_db = client[VENDORS_DB_NAME]

# Collections from AdminDB
stations_collection = admin_db[STATION_COLLECTION_NAME]
trains_collection = admin_db[TRAIN_COLLECTION_NAME]
vendors_collection = admin_db[VENDOR_COLLECTION_NAME]

# Collections from CustomersDB
customers_collection = customers_db[CUSTOMERS_COLLECTION_NAME]

# Collections from VendorsDB
food_items_collection = vendors_db[FOOD_COLLECTION_NAME]
orders_collection = vendors_db[ORDER_COLLECTION_NAME]