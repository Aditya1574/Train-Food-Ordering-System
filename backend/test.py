import unittest
from flask import json
from flask_app import app  # Import the Flask app

class TestCase(unittest.TestCase):
    def setUp(self):
        """Set up test variables and initialize app."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()

    def tearDown(self):
        """Tear down test variables after tests are complete."""
        pass


    #  ----------------- testing the create functions -----------

    # def test_create_vendor(self):
    #     """Test API can create a vendor (POST request)"""
    #     vendor = {
    #         'vendor_id': 'v100',
    #         'name': 'Test Vendor',
    #         'contact_info': {'phone': '1234567890', 'email': 'test@example.com'},
    #         'station_id': 's100'
    #     }
    #     response = self.app.post('/create_vendor', data=json.dumps(vendor), content_type='application/json')
    #     self.assertEqual(response.status_code, 201)
    #     self.assertIn('Vendor created successfully', str(response.data))


    # def test_create_food_item(self):
    #     """Test API can create a food item (POST request)"""
    #     food_item = {
    #         'item_id': 'f100',
    #         'name': 'Test Pizza',
    #         'description': 'Delicious cheese pizza',
    #         'price': 9.99,
    #         'category': 'Pizza',
    #         'available': True,
    #         'vendor_id': 'v100'
    #     }
    #     response = self.app.post('/create_food_item', data=json.dumps(food_item), content_type='application/json')
    #     self.assertEqual(response.status_code, 201)
    #     self.assertIn('Food item created successfully', str(response.data))

    # def test_create_station(self):
    #     """Test API can create a station (POST request)"""
    #     station = {
    #         'station_id': 's100',
    #         'name': 'Central Station',
    #         'location': 'Downtown'
    #     }
    #     response = self.app.post('/create_station', data=json.dumps(station), content_type='application/json')
    #     self.assertEqual(response.status_code, 201)
    #     self.assertIn('Station created successfully', str(response.data))

    # def test_create_train(self):
    #     """Test API can create a train (POST request)"""
    #     train = {
    #         'train_id': 't200',
    #         'name': 'Express 200',
    #         'route': ['s100', 's101'],
    #         'active': True
    #     }
    #     response = self.app.post('/create_train', data=json.dumps(train), content_type='application/json')
    #     self.assertEqual(response.status_code, 201)
    #     self.assertIn('Train created successfully', str(response.data))


    # # ------------- comment the below If testing above : testing the update functions -------------------

    # def test_update_vendor(self):
    #     """Test API can update a vendor (PATCH request)"""
    #     # Assuming a vendor exists with vendor_id 'v001'
    #     updates = {'name': 'Updated Vendor Name'}
    #     response = self.app.patch('/update_vendor?vendor_id=v001', data=json.dumps(updates), content_type='application/json')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn('Vendor updated successfully', str(response.data))

    # def test_update_food_item(self):
    #     """Test API can update a food item (PATCH request)"""
    #     # Assuming a food item exists with item_id 'f001'
    #     updates = {'price': 11.99, 'available': False}
    #     response = self.app.patch('/update_food_item?item_id=f100', data=json.dumps(updates), content_type='application/json')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn('Food item updated successfully', str(response.data))

    
    # def test_update_station(self):
    #     """Test API can update a station (PATCH request)"""
    #     # Assuming a station exists with station_id 's001'
    #     updates = {'location': 'New Location Street'}
    #     response = self.app.patch('/update_station?station_id=s100', data=json.dumps(updates), content_type='application/json')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn('Station updated successfully', str(response.data))
    
    # def test_update_train(self):
    #     """Test API can update a train (PATCH request)"""
    #     # Assuming a train exists with train_id 't001'
    #     updates = {'name': 'Super Fast Express9-11'}
    #     response = self.app.patch('/update_train?train_id=t200', data=json.dumps(updates), content_type='application/json')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn('Train updated successfully', str(response.data))
    
    
    # --------------- vendor specific ---------------------

    # def test_create_order(self):
    #     """Test creating a new order."""
    #     order_data = {
    #         "customer_id": "cust123",
    #         "train_id": "train123",
    #         "station_id": "station123",
    #         "vendor_id" : "v100",
    #         "items": [{"item_id": "item123", "quantity": 2, "price": 15}],
    #         "total_price": 30,
    #         "status": "pending"
    #     }
    #     response = self.app.post('/create_order', data=json.dumps(order_data), content_type='application/json')
    #     self.assertEqual(response.status_code, 201)
    #     self.assertIn("order_id", json.loads(response.data).keys())


    # def test_update_order(self):
        # """Test updating an existing order."""
        # updates = {"status": "completed"}
        # response = self.app.patch('/update_order?item_id=66a650d7a08f7adb55894f6c', data=json.dumps(updates), content_type='application/json')
        # self.assertEqual(response.status_code, 200)
        # self.assertIn("Order updated successfully", str(response.data))


    # def test_view_order(self):
    #     """Test viewing an order with a valid ObjectId string."""
    #     response = self.app.get('/vendors_view_orders?vendor_id=v100')
    #     self.assertEqual(response.status_code, 200)
    #     # Ensure that data is returned and the 'order' key is in the response
    #     data = json.loads(response.data)
    #     self.assertTrue(data.get('order') is not None)

    # def test_register_new_user(self):
    #     """Test registering a new user."""
    #     new_user = {
    #         "customer_id": "cust002",
    #         "name": "Jane Doe",
    #         "email": "janedoe@example.com",
    #         "password": "securePassword123",
    #         "phone": "9876543210",
    #         "address": {
    #             "city": "Los Angeles",
    #             "state": "CA",
    #             "postalCode": "90001",
    #             "country": "USA"
    #         }
    #     }
    #     response = self.app.post('/register', data=json.dumps(new_user), content_type='application/json')
    #     self.assertEqual(response.status_code, 201)
    #     self.assertIn("User registered successfully", response.get_data(as_text=True))

    # def test_register_existing_user(self):
    #     """Test registration failure for user with existing email."""
    #     existing_user = {
    #         "customer_id": "cust002",
    #         "name": "Alice Doe",
    #         "email": "janedoe@example.com",  # Assuming this email is already used
    #         "password": "anotherSecurePassword123",
    #         "phone": "9876501234",
    #         "address": {
    #             "city": "Miami",
    #             "state": "FL",
    #             "postalCode": "33101",
    #             "country": "USA"
    #         }
    #     }
    #     response = self.app.post('/register', data=json.dumps(existing_user), content_type='application/json')
    #     self.assertEqual(response.status_code, 400)
    #     self.assertIn("Registration failed", response.get_data(as_text=True))


    def test_login_valid_user(self):
        """Test login with valid credentials."""
        credentials = {
            "customer_id": "cust002",
            "password": "securePassword123"
        }
        response = self.app.post('/login', data=json.dumps(credentials), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.get_data(as_text=True))

    def test_login_invalid_user(self):
        """Test login with invalid credentials."""
        credentials = {
            "customer_id": "nonexistent@example.com",
            "password": "wrongPassword"
        }
        response = self.app.post('/login', data=json.dumps(credentials), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn("Invalid username or password", response.get_data(as_text=True))

    def test_login_invalid_password(self):
        """Test login with a valid username but invalid password."""
        credentials = {
            "customer_id": "cust002",
            "password": "wrongPassword"
        }
        response = self.app.post('/login', data=json.dumps(credentials), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn("Invalid username or password", response.get_data(as_text=True))



