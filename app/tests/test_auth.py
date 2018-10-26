'''Tests for users'''
import json
# from .base_test import BaseTestCase

import unittest
import json

from .. database.db_con import migrate

from .. import create_app

class BaseTestCase(unittest.TestCase):
    """Parent tests class"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        migrate()
    
        self.client = self.app.test_client()

        self.users = {'email': 'andrewhinga5@gmail.com', 'username': 'andrew5', 'password': '1234'}
        self.new_user = {'email': 'john@gmail.com', 'username':'john', 'password': '1881'}
        self.user = {'email': 'henry@gmail.com','username': 'henry','password': 'password'}
        self.bad_user = {"password":"password"}


        self.header = {"Content-Type": "application/json"}

        self.s_url = 'api/v1/auth/signup' #signup url
        self.l_url = 'api/v1/auth/login' #login url
        self.p_url = 'api/v1/products' #products url



class UsersTestCase(BaseTestCase): 
    """This class represents Users tests."""

        
    def test_signup_user_with_existing_email(self):
        """Test to register user with existing email."""
        data = self.users
        response = self.client.post(self.s_url, data=json.dumps(data), headers=self.header)

        result = json.loads(response.data.decode())

        self.assertEqual(result['message'],'Email already exists.')

    def test_signup_new_user(self):
        """Test to register new user."""
        data = self.new_user
        response = self.client.post(self.s_url, data=json.dumps(data), headers=self.header)

        result = json.loads(response.data.decode())

        self.assertEqual(result['message'],'User created!')


    def test_signin_user(self):
        """Test user sign in to their account."""
        data = self.users
        response = self.client.post(self.l_url, data=json.dumps(data), headers=self.header)

        result = json.loads(response.data.decode())

        self.assertEqual(result['message'], "Logged in successfully!")


    def test_signin_non_registered_user(self):
        """Test signing in a non-registered user."""
        data = self.new_user
        response = self.client.post(self.l_url, data=json.dumps(data), headers=self.header)

        result = json.loads(response.data.decode())

        self.assertEqual(result['message'], "Your account does not exist!, Please Register!")


if __name__ == "__main__":
    unittest.main()

