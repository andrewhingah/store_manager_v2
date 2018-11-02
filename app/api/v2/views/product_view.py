"""This module contains resources for products"""

from datetime import datetime
from flask import Flask, jsonify, make_response, request
from flask_restful import Api, Resource, reqparse

from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

from app.api.v2.models.product_model import Product

from app.api.v2.models.helpers import get_user, get_products, get_product, delete_product, edit_product
from app.api.v2.utils.validate import validate_email, verify_name_details, validate_all


parser = reqparse.RequestParser()
parser.add_argument('category', required = True, help = "Category cannot be empty")
parser.add_argument('name', required = True, help = "Name cannot be empty")
parser.add_argument('quantity', required = True, help = "Quantity should be an integer")
parser.add_argument('price', required=True, help="Price cannot be empty")

# data = request.get_json(force = True)

class AllProducts(Resource):
	"""All products class"""
	@jwt_required
	def get(self):
		"""gets all products"""
		products = get_products()
		if products is None:
			return make_response(jsonify(
				{
				"message": "No products available"
				}))
		return make_response(jsonify(
			{
			"message":"success",
			"status":"ok",
			"products":products}), 200)

	@jwt_required
	def post(self):
		"""posts a single product"""
		email = get_jwt_identity()
		user = get_user(email)
		if user['role'] != 'admin':
			return {"message": "You don't have access to this page"}, 403
		
		args = parser.parse_args()
		category = args['category']
		name = args['name']
		quantity = args['quantity']
		price = args['price']
		date_created = datetime.now()
		# user_id = (user['id'])

		if verify_name_details(category):
			return verify_name_details(category)

		if verify_name_details(name):
			return verify_name_details(name)

		newproduct = Product(category, name, quantity, price, date_created)
		newproduct.save()

		return make_response(jsonify(
			{"message":"Product created successfully",
			"status":"created",
			"product":newproduct.__dict__}
			), 201)

		def get(self):
			'''view all available products'''
			email = get_jwt_identity()
			user = get_user(email)

			products = get_products()
			if products is None:
				return jsonify ({"message": "No products available"}), 404

			return jsonify({"message": "successfully", "Products": products}), 200

class SingleProduct(Resource):
	'''This class has all operations related to a single product'''
	def get(self, id):
		'''gets single product by id'''
		email = get_jwt_identity()
		user = get_user(email)
		product = get_product(id)
		if product is None:
			return make_response(jsonify({"message": "Product unavailable"}), 404)
		return make_response(jsonify({"message": "success", "Product": product}), 200)

	@jwt_required
	def delete(self, id):
		'''deletes a single product by id'''
		email = get_jwt_identity()
		user = get_user(email)

		if user['role'] != "admin":
			return {"message": "You are not permitted to perform this action"}

		product = get_product(id)
		if product is None:
			return jsonify({"message": "You requested to delete an unavailable product"})

		delete_product(id)
		return jsonify({"message": "product has been deleted"})

	@jwt_required
	def put(self, id):
		'''
		updates details of an existing product
		creates a new one if not exists
		'''
		email = get_jwt_identity()
		user = get_user(email)

		if user['role'] != 'admin':
			return {"message": "You are not permitted to perform this action"}

		product = get_product(id)
		args = parser.parse_args()
		if product is None:

			product = Product(
				category = args['category'],
				name = args['name'],
				quantity = args['quantity'],
				price = args['price'],
				date_created = datetime.now())

			product.save()

			return make_response(jsonify({'Product': product.__dict__,
	        'message': "New product created"}), 200)

		else:
			product['category'] = args['category']
			product['name'] = args['name']
			product['quantity'] = args['quantity'],
			product['price'] = args['price'],
			product['date_created'] = datetime.now()

			edit_product(id, product)

			return make_response(jsonify({"Product":product,
				"message":"Updated successfully"}), 200)