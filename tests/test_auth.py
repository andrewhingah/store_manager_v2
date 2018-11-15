'''Authentication tests'''

import json

from .basetest import BaseTestCase

class UsersTestCase(BaseTestCase): 
    """This class represents Users tests."""

    def test_signup_user_with_existing_email(self):
        '''test signup user with an existing email'''
        data = self.att_user
        response = self.checker.post(self.s_url,
            data=json.dumps(data), headers=self.authHeaders)

        result = json.loads(response.data.decode())

        self.assertEqual(result['message'], 'User with that email already exists.')
        self.assertEqual(response.status_code, 202)

    def test_signup_new_user(self):
        """Test to register new user."""
        data = self.new_user
        response = self.checker.post(self.s_url,
            data=json.dumps(data), headers=self.authHeaders)

        result = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['message'], 'User created!')


    def test_signin_user(self):
        """Test user sign in to their account."""
        data = self.new_user
        response = self.checker.post(self.s_url,
            data=json.dumps(data), headers=self.authHeaders)


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