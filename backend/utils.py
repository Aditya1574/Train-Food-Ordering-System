from config import vendors_collection, food_items_collection, stations_collection, trains_collection, orders_collection, customers_collection
from datetime import datetime
from bson import ObjectId
import json



# utility functions

def view_all_orders(vendor_id):
    """Returns all orders containing items from the specified vendor."""
    # Using aggregation to unwind items array and match vendor_id in the items
    pipeline = [
        {"$unwind": "$items"},
        {"$match": {"vendor_id": vendor_id}},
        {"$group": {
            "_id": "$_id",  # Group back by order ID to re-assemble the order documents
            "customer_id": {"$first": "$customer_id"},
            "train_id": {"$first": "$train_id"},
            "station_id": {"$first": "$station_id"},
            "items": {"$push": "$items"},
            "total_price": {"$first": "$total_price"},
            "status": {"$first": "$status"},
            "order_time": {"$first": "$order_time"}
        }}
    ]
    return list(orders_collection.aggregate(pipeline))



def get_user_by_username(customer_id):
    """Retrieve a user by their email from the MongoDB customers_collection."""
    try:
        user = customers_collection.find_one({"customer_id": customer_id})
        return user
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def parse_for_object_id(response):   

    if isinstance(response, dict):
        if "_id" in response:
            response["_id"] = str(response["_id"])
        
    if isinstance(response, list):    
        for index, obj in enumerate(response):
            if "_id" in obj:
                response[index]["_id"] = str(obj["_id"])
    
    return response

def calculate_total_price(items):

    quantity = int(items["quantity"])
    price_per_item = int(items["price"])

    return str(quantity*price_per_item)