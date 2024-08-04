from config import vendors_collection, food_items_collection, stations_collection, trains_collection, orders_collection, customers_collection
from datetime import datetime
from bson import ObjectId
import json



# utility functions

def get_user_by_username(customer_id):
    """Retrieve a user by their email from the MongoDB customers_collection."""
    try:
        user = customers_collection.find_one({"customer_id": customer_id})
        return user
    except Exception as e:
        print(f"An error occurred: {e}")
        return None



def get_train_by_train_id(train_id):
    
    try:
        train = trains_collection.find_one({"train_id" : train_id})
        if not train:
            return "Train with {train_id} not found in trains_collection".format(train_id)
        
        return train
    except Exception as e:
        return f"Error : {e}"

def get_vendor_info(key_name, key_value):

    try:    
        vendors = list(vendors_collection.find({key_name: key_value}))
        return vendors
    except Exception as e:
        return f"Error : {e}"

def get_food_items_info(key_name, key_value):

    try:
        food_items = list(food_items_collection.find({key_name :key_value}))
        return food_items
    except Exception as e:
        return f"Error : {e}"


def get_order_info_order_id(order_id, key_name=None):

    try:
        response = orders_collection.find_one({"_id" : ObjectId(order_id)})
        if key_name:
            response = response[key_name]
        
        return response
    except Exception as e:
        return f"Error : {e}"
        

def get_orders_using_id(key_name, key_value):

    try:
        response = list(orders_collection.find({key_name: key_value}))

        return response
    except Exception as e:
        return f"Error : {e}"


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


