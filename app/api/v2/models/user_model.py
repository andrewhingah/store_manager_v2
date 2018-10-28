# from . import helpers
from app.api.v2.models import helpers

class User:
	'''Class represents operations related to products'''

	def __init__(self, name, email, username, password):
		self.name = name
		self.email = email
		self.username = username
		self.password = password


	def signup(self):
		helpers.insert_user(self)
