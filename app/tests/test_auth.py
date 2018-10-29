'''Tests for users'''
import json
from .base_test import BaseTestCase


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
