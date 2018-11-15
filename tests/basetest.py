'''Tests for users'''

import os
import unittest
import json

from app import create_app

from app.manage import migrate, reset_migrations

class BaseTestCase(unittest.TestCase):
    """Parent tests class"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")
        with self.app.app_context():
            migrate()
    
        self.client = self.app.test_client()
        self.checker = self.app.test_client()
        self.attendant = self.app.test_client()

    
        self.admin_login = {
        'email': 'super@admin.com',
        'password': 'A123@admin'
        }

        self.att_user = {
        'name': 'john terry',
        'email': 'john@gmail.com',
        'password': '1881@#&TQ',
        'role': 'normal'
        }

        self.new_user = {
        "name": "John Kamau",
        "email": "johnkamau@gmail.com",
        "password": "kamau_12_Q",
        'role': "normal"
        }

        self.bad_user = {
        "password":"password"
        }

        self.new_product = {
        "category": "electronics",
        "name": "HP Laptop",
        "quantity": 50,
        "price": 55555
        }

        self.edit_product = {
        "category": "electronics",
        "name": "MacBook",
        "quantity": 77,
        "price": 99000
        }


        self.invalid_prod = {
        "category": "electronics",
        "quantity": 50,
        "price": 50900
        }

        self.s_url = 'api/v2/auth/signup' #signup url
        self.l_url = 'api/v2/auth/login' #login url
        self.p_url = 'api/v2/products' #products url

        self.header = {"content-type": "application/json"}


        # login the admin
        response = self.client.post("/api/v2/auth/login", data=json.dumps(self.admin_login), headers=self.header)
        # create the authentication headers
        self.authHeaders = {"content-type":"application/json"}

        # put the bearer token in the header
        result = json.loads(response.data.decode())

        self.authHeaders['Authorization'] = 'Bearer '+result['token']

        # create an normal attendant account
        self.attendant.post('/api/v2/auth/signup', data=json.dumps(self.att_user), headers=self.authHeaders)


        # login the store attendant
        res2 = self.attendant.post("/api/v2/auth/login", data=json.dumps(self.att_user), headers=self.header)
        # create the authentication headers
        self.attHeaders = {"content-type":"application/json"}

        # put the bearer token in the header
        result2 = json.loads(res2.data.decode())

        self.attHeaders['Authorization'] = 'Bearer '+result2['token']


    def tearDown(self):
        reset_migrations()


if __name__ == "__main__":
    unittest.main()