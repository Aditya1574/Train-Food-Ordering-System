from config import vendors_collection, food_items_collection, stations_collection, trains_collection, orders_collection, customers_collection
from datetime import datetime
from bson import ObjectId


#  ----------- funtions for creating new entities -----------------
def create_vendor(vendor_id, name, contact_info, station_id):
    """Creates a new vendor in the vendors collection."""
    vendor = {
        "vendor_id": vendor_id,
        "name": name,
        "contact_info": contact_info,
        "station_id" : station_id
    }
    result = vendors_collection.insert_one(vendor)
    return result.inserted_id


def create_food_item(item_id, name, description, price, category, available, vendor_id):
    """Creates a new food item in the food items collection."""
    food_item = {
        "item_id": item_id,
        "name": name,
        "description": description,
        "price": price,
        "category" : category,
        "available": available,
        "vendor_id": vendor_id
    }
    result = food_items_collection.insert_one(food_item)
    return result.inserted_id


def create_station(station_id, name, location):
    """Creates a new station in the stations collection."""
    station = {
        "station_id": station_id,
        "name": name,
        "location": location
    }
    result = stations_collection.insert_one(station)
    return result.inserted_id


def create_train(train_id, name, route, active=True):
    """Creates a new train in the trains collection."""
    train = {
        "train_id": train_id,
        "name": name,
        "route": route,  # This should be a list of station IDs
        "active": active
    }
    result = trains_collection.insert_one(train)
    return result.inserted_id




def create_order(customer_id, train_id, station_id, vendor_id, items, total_price, status):
    """Creates a new order in the orders collection."""
    order = {
        "customer_id": customer_id,
        "train_id": train_id,
        "station_id": station_id,
        "vendor_id" : vendor_id,
        "items": items,  # Expected to be a list of dictionaries with item details
        "total_price": total_price,
        "status": status,
        "order_time": datetime.now()  # Capture the order time
    }
    result = orders_collection.insert_one(order)
    return result.inserted_id


def create_user(customer_id, name, email, password_hash, phone, address):
    """Create a new user in the MongoDB customers_collection."""
            
    try:
        user = {
            "customer_id": customer_id,
            "name": name,
            "email": email,
            "password_hash": password_hash,
            "phone": phone,
            "address": address
        }
        # Insert the user into the collection
        result = customers_collection.insert_one(user)
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False





#  ----------- funtions for updating entities -----------------
def update_vendor(vendor_id, updates):
    """Updates a vendor in the vendors collection."""
    query = {"vendor_id": vendor_id}
    new_values = {"$set": updates}
    result = vendors_collection.update_one(query, new_values)
    return result.modified_count



def update_food_item(item_id, updates):
    """Updates a food item in the food items collection."""
    query = {"item_id": item_id}
    new_values = {"$set": updates}
    result = food_items_collection.update_one(query, new_values)
    return result.modified_count



def update_station(station_id, updates):
    """Updates a station in the stations collection."""
    query = {"station_id": station_id}
    new_values = {"$set": updates}
    result = stations_colltrection.update_one(query, new_values)
    return result.modified_count



def update_train(train_id, updates):
    """Updates a train in the trains collection."""
    query = {"train_id": train_id}
    new_values = {"$set": updates}
    result = trains_collection.update_one(query, new_values)
    return result.modified_count


def update_order(order_id, updates):
    """Updates an order in the orders collection."""
    query = {"_id": ObjectId(order_id)}
    new_values = {"$set": updates}
    result = orders_collection.update_one(query, new_values)
    return result.modified_count


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

# if __name__ == "__main__":
    # new_vendor_id = create_vendor("v001", "Best Vendors Inc.", {"phone": "123-456-7890", "email": "contact@bestvendors.com"})
    # new_food_item_id = create_food_item("f001", "Cheese Pizza", "Delicious cheese pizza", 9.99, True, new_vendor_id)
    # new_station_id = create_station("s001", "Central Station", "123 Main St, Big City")
    # new_train_id = create_train("t001", "Express 101", ["s001"], True)

    # print(view_all_orders("v100"))
