from flask import Flask, request, jsonify
from database import create_food_item,create_station, create_train, create_vendor, update_food_item, update_station, update_train, update_vendor, create_order, update_order, create_user, get_train_by_train_id, get_vendor_info, get_food_items_info,get_orders_using_id,get_order_info_order_id
from dotenv import load_dotenv
import os
from logger import logger
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from utils import view_all_orders, get_user_by_username, parse_for_object_id, calculate_total_price
from bson import json_util, ObjectId


load_dotenv()


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.getenv("AUTH_SECRET_KEY")

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

FLASK_PORT=os.getenv("FLASK_PORT")


# Register and Login routes

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    customer_id = data.get('customer_id')
    name = data.get('name')
    email = data.get('email')
    plain_password = data.get('password')
    phone = data.get('phone')
    address = data.get('address')


    # Hash the password
    hashed_password = bcrypt.generate_password_hash(plain_password).decode('utf-8')

    # Save the user to your database
    # Assuming you have a function `create_user` that saves the user and returns a success flag
    try:
        success = create_user(customer_id,name, email, hashed_password, phone, address)

        if success:
            return jsonify({"success": True, "message": "User registered successfully"}), 201
        else:
            return jsonify({"success": False, "message": "Registration failed"}), 400
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    data = request.json 
    username = data.get("customer_id")
    plain_password = data.get("password")

    # Fetch the user from your database
    # Assuming you have a function `get_user_by_username` that returns the user data
    user = get_user_by_username(username)

    if user and bcrypt.check_password_hash(user['password_hash'], plain_password):
        # Generate a token
        access_token = create_access_token(identity=username)
        return jsonify({"success": True, "access_token": access_token}), 200
    else:
        return jsonify({"success": False, "message": "Invalid username or password"}), 401



# Create Entities

@app.route('/create_vendor', methods=['POST'])
def create_vendor_endpoint():
    data = request.json
    try:
        vendor_id = create_vendor(
            vendor_id=data.get('vendor_id'),
            name=data.get('name'),
            contact_info=data.get('contact_info'),
            station_id=data.get('station_id')
        )
        return jsonify({"success": True, "message": "Vendor created successfully", "vendor_id": str(vendor_id)}), 201
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
    

@app.route('/create_food_item', methods=['POST'])
def create_food_item_endpoint():
    data = request.json
    try:
        item_id = create_food_item(
            item_id=data.get('item_id'),
            name=data.get('name'),
            description=data.get('description'),
            price=data.get('price'),
            category=data.get('category'),
            available=data.get('available'),
            vendor_id=data.get('vendor_id')
        )
        return jsonify({"success": True, "message": "Food item created successfully", "item_id": str(item_id)}), 201
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@app.route('/create_station', methods=['POST'])
def create_station_endpoint():
    data = request.json
    try:
        station_id = create_station(
            station_id=data.get('station_id'),
            name=data.get('name'),
            location=data.get('location')
        )
        return jsonify({"success": True, "message": "Station created successfully", "station_id": str(station_id)}), 201
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@app.route('/create_train', methods=['POST'])
def create_train_endpoint():
    data = request.json
    try:
        train_id = create_train(
            train_id=data.get('train_id'),  
            name=data.get('name'),
            route=data.get('route'),
            active=data.get('active', True)  # Default to True if not specified
        )
        return jsonify({"success": True, "message": "Train created successfully", "train_id": str(train_id)}), 201
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500



@app.route("/create_order",methods=['POST'])
def create_order_endpoint():
    data = request.json
    try:
        total_price = calculate_total_price(data["items"])
        data["total_price"] = total_price
        order_id = create_order(**data)
        return jsonify({"success": True, "order_id": str(order_id)}), 201
    except Exception as  e:
         return jsonify({"success": False, "message": str(e)}), 500
    


# Update

@app.route('/update_vendor', methods=['PATCH'])
def update_vendor_endpoint():
    vendor_id = request.args.get("vendor_id")
    updates = request.json
    try:
        modified_count = update_vendor(vendor_id, updates)
        if modified_count:
            return jsonify({"success": True, "message": "Vendor updated successfully"}), 200
        else:
            return jsonify({"success": False, "message": f"No vendor found with vendorID : {vendor_id}"}), 404
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@app.route('/update_food_item', methods=['PATCH'])
def update_food_item_endpoint():
    item_id = request.args.get("item_id")
    updates = request.json
    try:
        modified_count = update_food_item(item_id, updates)
        if modified_count:
            return jsonify({"success": True, "message": "Food item updated successfully"}), 200
        else:
            return jsonify({"success": False, "message": f"No food item found with FoodItemID : {item_id}"}), 404
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500



@app.route('/update_station', methods=['PATCH'])
def update_station_endpoint():
    station_id = request.args.get("station_id")
    updates = request.json
    try:
        modified_count = update_station(station_id, updates)
        if modified_count:
            return jsonify({"success": True, "message": "Station updated successfully"}), 200
        else:
            return jsonify({"success": False, "message": f"No station found with stationID : {station_id}"}), 404
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500



@app.route('/update_train', methods=['PATCH'])
def update_train_endpoint():
    train_id = request.args.get("train_id")
    updates = request.json

    try:
        modified_count = update_train(train_id, updates)
        if modified_count:
            return jsonify({"success": True, "message": "Train updated successfully"}), 200
        else:
            return jsonify({"success": False, "message": f"No train found with trainID {train_id}"}), 404
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500



@app.route('/update_order', methods=['PATCH'])
def update_order_endpoint():
    order_id = request.args.get("item_id")
    updates = request.json
    modified_count = update_order(order_id, updates)
    if modified_count:
        return jsonify({"success": True, "message": "Order updated successfully"}), 200
    else:
        return jsonify({"success": False, "message": "No order found or update failed"}), 404 


# Operationals


@app.route('/vendors_view_orders', methods=['GET'])
def vendors_view_all_orders_endpoint():
    vendor_id = request.args.get("vendor_id")
    try:
        orders = view_all_orders(vendor_id)
        orders = parse_for_object_id(orders)
        return jsonify({"success": True, "orders": orders}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500




@app.route('/get_stations', methods=['GET'])
def get_stations_endpoint():
    train_id = request.args.get('train_id')
    try:
        train = get_train_by_train_id(train_id)

        if not train['active']:
            return jsonify({"data" : "Train Inactive"}), 404
        else:    
            return jsonify({"data" : train['route']}), 200
    except Exception as e:
        return jsonify({"Error" : str(e)}), 400


@app.route('/get_vendors_station_id', methods=['GET'])
def get_vendors_endpoints():
    
    station_id = request.args.get("station_id")

    try:
        vendors = get_vendor_info("station_id", station_id)
        vendors = parse_for_object_id(vendors)
        return jsonify({"data" : vendors}), 200
    except Exception as e:
        return jsonify({"Error" : str(e)}), 400


@app.route('/get_food_items_vendor_id', methods=['GET'])
def get_food_items_endpoints():
    
    vendor_id = request.args.get("vendor_id")

    try:
        food_items = get_food_items_info("vendor_id", vendor_id)
        food_items = parse_for_object_id(food_items)
        return jsonify({"data" : food_items}), 200
    except Exception as e:
        return jsonify({"Error" : str(e)}), 400


# Helper APIs
@app.route("/get_order_info", methods=['GET'])
def get_total_price_endpoints():

    order_id = request.args.get("order_id")
    key_name = request.args.get("key_name", None)
    try:
        order_info = get_order_info_order_id(order_id, key_name)

        order_info = parse_for_object_id(order_info)

        return jsonify({"data" : order_info}), 200
    except Exception as e:
        return jsonify({"Error" : str(e)}),400


@app.route("/customers_view_orders", methods=["GET"])
def customers_view_order_endpoint():

    customer_id = request.args.get("customer_id")

    try:
        response = get_orders_using_id("customer_id", customer_id)
        response = parse_for_object_id(response)

        return jsonify({"data" : response}),200
    except Exception as e:
        return jsonify({"Error":  str(e)}), 400



if __name__ == "__main__":
    app.run(debug=True, port=FLASK_PORT)