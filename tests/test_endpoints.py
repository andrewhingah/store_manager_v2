'''Tests for users'''
# from .base_test import BaseTestCase
import os
import unittest
import json

from app import create_app

from app.manage import migrate, reset_migrations

class BaseTestCase(unittest.TestCase):
    """Parent tests class"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        migrate()
    
        self.client = self.app.test_client()
        self.checker = self.app.test_client()
        self.attendant = self.app.test_client()

        self.users = {
        'name':'andrew hinga',
        'email': 'andrewhinga5@gmail.com',
        'password': '1234',
        'role': 'normal'
        }
        self.user_login = {
        'email': 'andrewhinga5@gmail.com',
        'password': '1234'
        }

        self.att_user = {
        'name': 'john terry',
        'email': 'john@gmail.com',
        'password': '1881',
        'role': 'normal'
        }

        self.user = {
        'name':'andrew hinga',
        'email': 'andrewhinga5@gmail.com',
        'password': '1234',
        'role': 'admin'
        }

        self.new_user = {
        "name": "John Kamau",
        "email": "johnkamau@gmail.com",
        "password": "kamau_12",
        'role': "normal"
        }

        self.bad_user = {
        "password":"password"
        }

        self.new_product = {
        "category": "electronics",
        "name": "HP Laptop",
        "quantity": 50,
        "price": 55000
        }

        self.new_sale = {

        "product_id": 1,
        "quantity": 3
        }

        self.s_url = 'api/v2/auth/signup' #signup url
        self.l_url = 'api/v2/auth/login' #login url
        self.p_url = 'api/v2/products' #products url

        self.header = {"content-type": "application/json"}


        # create an admin
        self.client.post('/api/v2/auth/signup', data=json.dumps(self.user), headers=self.header)

        # login the admin
        response = self.client.post("/api/v2/auth/login", data=json.dumps(self.user_login), headers=self.header)
        # create the authentication headers
        self.authHeaders = {"content-type":"application/json"}

        # put the bearer token in the header
        result = json.loads(response.data.decode())

        self.authHeaders['Authorization'] = 'Bearer '+result['token']

        # create an normal attendant account
        self.attendant.post('/api/v2/auth/signup', data=json.dumps(self.att_user), headers=self.header)


        # login the store attendant
        res2 = self.attendant.post("/api/v2/auth/login", data=json.dumps(self.att_user), headers=self.header)
        # create the authentication headers
        self.attHeaders = {"content-type":"application/json"}

        # put the bearer token in the header
        result2 = json.loads(res2.data.decode())

        self.attHeaders['Authorization'] = 'Bearer '+result2['token']




class UsersTestCase(BaseTestCase): 
    """This class represents Users tests."""

    def test_signup_user_with_existing_email(self):
        data = self.user
        response = self.checker.post(self.s_url,
            data=json.dumps(data), headers=self.header)

        result = json.loads(response.data.decode())

        self.assertEqual(result['message'], 'Email already exists.')

    def test_signup_new_user(self):
        """Test to register new user."""
        data = self.new_user
        response = self.checker.post(self.s_url,
            data=json.dumps(data), headers=self.header)

        result = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['message'], 'User created!')


    def test_signin_user(self):
        """Test user sign in to their account."""
        data = self.new_user
        response = self.checker.post(self.s_url,
            data=json.dumps(data), headers=self.header)


        self.assertEqual(response.status_code, 201)
        
        res = self.checker.post(self.l_url,
            data=json.dumps(data), headers=self.header)

        result = json.loads(res.data.decode())

        self.assertEqual(result['message'], "Logged in successfully!")
        self.assertEqual(res.status_code, 201)


    def test_signin_non_registered_user(self):
        """Test signing in a non-registered user."""
        data = self.new_user
        response = self.checker.post(self.l_url,
            data=json.dumps(data), headers=self.header)

        result = json.loads(response.data.decode())

        # assert that this response must contain an error message 
        # and an error status code 401(Unauthorized)
        self.assertEqual(result['message'],
            "Your account does not exist! Please register")
        self.assertEqual(response.status_code, 401)


    def test_admin_create_new_product(self):
        '''test admin can create a new product'''

        response = self.client.post(self.p_url,
            data=json.dumps(self.new_product), headers=self.authHeaders)
        result = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['message'], 'Product created successfully')


    def test_get_all_products(self):
        '''test admin can get all available products'''
        response = self.client.get(self.p_url, headers=self.authHeaders)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], "success")

    def test_attendant_cannot_create_new_product(self):
        '''test a normal attendant cannot create a new product'''
        response = self.client.post(self.p_url,
            data=json.dumps(self.new_product), headers=self.attHeaders)
        result = json.loads(response.data.decode())
        self.assertEqual(response.status, '403 FORBIDDEN')
        self.assertEqual(result["message"], "You don't have access to this page")

    # def test_get_single_product_by_id(self):
    #     '''test get a single product by id'''
    #     res_1 = self.client.post(self.p_url,
    #         data=json.dumps(self.new_product), headers=self.authHeaders)
    #     self.assertEqual(res_1.status_code, 201)

    #     res_2 = self.client.get('api/v2/products', headers=self.authHeaders)
    
    #     self.assertEqual(res_2.status_code, 200)

    #sales

    # def test_get_all_sales(self):
    #     '''test that a user can get all sales'''
    #     response = self.client.get('api/v2/sales', headers=self.authHeaders)
    #     self.assertEqual(response.status_code, 200)
    #     result = json.loads(response.data.decode())
    #     self.assertEqual(result['message'], 'success')

    def test_attendant_create_new_sale(self):
        '''test attendant can create a sale record'''
        res_1 = self.client.post(self.p_url,
            data=json.dumps(self.new_product), headers=self.authHeaders)
        result = json.loads(res_1.data.decode())
        self.assertEqual(res_1.status_code, 201)

        res_2 = self.client.post('api/v2/sales',
            data=json.dumps(self.new_sale), headers=self.attHeaders)
        result = json.loads(res_2.data.decode())
        self.assertEqual(res_2.status, 201)
        self.assertEqual(result["message"], "created")

    # def test_attendant_create_sale_for_non_existing_product(self):
    #     response = self.client.post('api/v2/sales',
    #         data=json.dumps(self.new_sale), headers=self.attHeaders)
    #     result = json.loads(response.data.decode())
    #     self.assertEqual(response.status, 404)
    #     self.assertEqual(result["message"], "Product is unavailable")

    # def test_get_unavailable_single_sale(self):
    #     response = self.client.get('api/v2/sales/1',
    #         data=json.dumps(self.new_sale), headers=self.attHeaders)
    #     result = json.loads(response.data.decode())
    #     self.assertEqual(response.status, 404)
    #     self.assertEqual(result["message"], "Sale record unavailable")

    # def test_get_single_sale(self):
    #     res_1 = self.client.post(self.p_url,
    #         data=json.dumps(self.new_product), headers=self.authHeaders)
    #     self.assertEqual(res_1.status_code, 201)

    #     res_2 = self.client.post('api/v2/sales',
    #         data=json.dumps(self.new_sale), headers=self.attHeaders)
    #     result = json.loads(res_2.data.decode())
    #     self.assertEqual(res_2.status, 201)
    #     self.assertEqual(result["message"], "created")

    #     re_3 = self.client.get('api/v2/sales/1',
    #         data=json.dumps(self.new_sale), headers=self.attHeaders)
    #     result = json.loads(res_3.data.decode())
    #     self.assertEqual(res_3.status, 200)
    #     self.assertEqual(result["message"], "success")



    def tearDown(self):
        reset_migrations()


if __name__ == "__main__":
    unittest.main()