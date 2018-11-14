"""This module contains resources for sales"""

from datetime import datetime
from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource, reqparse

from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

from app.api.v2.models.product_model import Sale
from app.api.v2.models.helpers import get_product, get_sales, get_sale, get_user, decrease_quantity


parser = reqparse.RequestParser()
parser.add_argument('product_id', type=int, help="Id can only be an integer")
parser.add_argument('quantity', type=int, help="Quantity can only be an integer")

class AllSales(Resource):
	"""All products class"""

	@jwt_required
	def post(self):
		"""posts a single product"""
		email = get_jwt_identity()
		user = get_user(email)
		if user['role'] != 'normal':
			return {"message": "You don't have access to this page"}, 403
		args = parser.parse_args()
		product_id = args['product_id']
		quantity = args['quantity']

		if not product_id:
			return {"message": "Product ID must be provided"}, 400
		if not quantity:
			return {"message": "Quantity must be provided"}, 400

		if quantity <= 0:
			return {"message": "Please provide quantity above zero"}

		product = get_product(product_id)
		if product is None:
			return {"message": "Product is unavailable"}, 404

		remaining_q = product['quantity'] - quantity
		total_price = product['price'] * quantity
		name = product['name']
		date_created = datetime.now()

		if remaining_q <= 0:
			return {"message":"The quantity you want to sell exceeds the available inventory"}

		new_sale = Sale(product_id, quantity, remaining_q, total_price, name, date_created)

		#decrement quantity of product
		product['quantity'] = remaining_q
		decrease_quantity(product_id, product)

		new_sale.save()

		return make_response(jsonify(
			{"message":"Sale record created successfully",
			"status":"created",
			"product":new_sale.__dict__}
			), 201)

	@jwt_required
	def get(self):
		"""gets all products"""
		email = get_jwt_identity()
		user = get_user(email)
		if user['role'] != 'admin':
			return {"message": "You don't have access to this page"}, 403
		sales = get_sales()
		if sales is None:
			return make_response(jsonify(
				{
				"message": "No sales available"
				}))
		return make_response(jsonify(
			{
			"message":"success",
			"status":"ok",
			"Sales":sales}), 200)

class SingleSale(Resource):
	'''class represents operations for one sale record'''
	@jwt_required
	def get(self, id):
		'''gets single sale by id'''
		sale_record = get_sale(id)
		if sale_record is None:
			return make_response(jsonify({"message": "Sale record unavailable"}), 404)
		return make_response(jsonify({"message": "success", "Sale": sale_record}), 200)