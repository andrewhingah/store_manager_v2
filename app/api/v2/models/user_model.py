'''Class for user data'''
from app.api.v2.models import helpers

class User:
	'''Class represents operations related to pusers'''

	def __init__(self, name="", email="", password="", role=""):
		self.name = name
		self.email = email
		self.password = password
		self.role = role


	def signup(self):
		helpers.insert_user(self)