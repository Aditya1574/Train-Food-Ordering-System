from flask import Flask, request, jsonify
from database import create_food_item,create_station, create_train, create_vendor, update_food_item, update_station, update_train, update_vendor, create_order, update_order, view_all_orders
from dotenv import load_dotenv
import os
from logger import logger

load_dotenv()


app = Flask(__name__)
FLASK_PORT=os.getenv("FLASK_PORT")


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
        for index, order in enumerate(orders):
            orders[index]["_id"] = str(order['_id'])
        return jsonify({"success": True, "orders": orders}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500




if __name__ == "__main__":
    app.run(debug=True, port=FLASK_PORT)