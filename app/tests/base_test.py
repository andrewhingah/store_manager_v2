'''Base test class that defines
setup and initializes data'''

import unittest
import json

from .. import create_app

class BaseTestCase(unittest.TestCase):
    """Parent tests class"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
    
        self.client = self.app.test_client()

        self.users = {'email': 'andrewhinga5@gmail.com', 'username': 'andrew5', 'password': '1234'}
        self.new_user = {'email': 'john@gmail.com', 'username':'john', 'password': '1881'}
        self.user = {'email': 'henry@gmail.com','username': 'henry','password': 'password'}
        self.bad_user = {"password":"password"}


        self.header = {"Content-Type": "application/json"}

        self.s_url = 'api/v1/auth/signup' #signup url
        self.l_url = 'api/v1/auth/login' #login url
        self.p_url = 'api/v1/products' #products url


if __name__ == "__main__":
	unittest.main()
