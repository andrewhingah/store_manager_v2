from datetime import datetime
from app.api.v2.models import helpers


class Product:
	'''Class represents operations related to products'''

	def __init__(self, category="", name="", quantity="", price="", date_created="", user_id=""):
		self.category = category
		self.name = name
		self.quantity = quantity
		self.price = price
		self.date_created = date_created
		self.user_id = user_id


	def save(self):
		helpers.create_product(self)