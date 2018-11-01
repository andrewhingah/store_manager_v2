from datetime import datetime
from flask import Flask, jsonify, make_response, request
from flask_restful import Api, Resource, reqparse

from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

from app.api.v2.models.product_model import Product

from app.api.v2.models.helpers import get_user, get_products, get_product, delete_product, edit_product


# parser = reqparse.RequestParser()
# parser.add_argument('category')
# parser.add_argument('name')
# parser.add_argument('quantity')
# parser.add_argument('price')

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
		
		# args = parser.parse_args()
		# category = args['category']
		# name = args['name']
		# quantity = args['quantity']
		# price = args['price']
		# date_created = datetime.now()
		# user_id = (user['id'])

		data = request.get_json(force = True)

		category = data.get('category')
		name = data.get('name')
		quantity = data.get('quantity')
		price = data.get('price')
		date_created = datetime.now
		user_id = (user['id'])

		newproduct = Product(category, name, quantity, price, date_created, user_id)
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
		email = get_jwt_identity()
		user = get_user(email)
		product = get_product(id)
		if product is None:
			return make_response(jsonify({"message": "Product unavailable"}), 404)
		return make_response(jsonify({"message": "success", "Product": product}), 200)

	@jwt_required
	def delete(self, id):
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
		email = get_jwt_identity()
		user = get_user(email)

		if user['role'] != 'admin':
			return {"message": "You are not permitted to perform this action"}

		product = get_product(id)
		if product is None:
			product = Product(
				category = request.json.get("category"),
				name = request.json.get("name"),
				quantity = request.json.get("quantity"),
				price = request.json.get("price"),
				date_created = datetime.now(),
				id = id,
				user_id = (user["id"]))

			product.save()

			return make_response(jsonify({'Product': product.__dict__,
	        'message': "New product created"}), 200)

		else:
			product['category'] = request.json.get('category')
			product['name'] = request.json.get('name'),
			product['quantity'] = request.json.get('quantity'),
			product['price'] = request.json.get('price'),
			product['date_created'] = datetime.now()
			edit_product(id, product)

			return make_response(jsonify({"Product":product,
				"message":"Updated successfully"}), 200)