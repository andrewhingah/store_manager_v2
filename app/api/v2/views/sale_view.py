from datetime import datetime
from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource, reqparse

from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)

from app.api.v2.models.product_model import Sale
from app.api.v2.models.helpers import get_product, get_sales, get_sale, get_user


parser = reqparse.RequestParser()
parser.add_argument('product_id', required=True, help="Id cannot be blank")
parser.add_argument('quantity', type=int, required=True, help="Only integers allowed")

class AllSales(Resource):
	"""All products class"""

	@jwt_required
	def post(self):
		"""posts a single product"""
		args = parser.parse_args()
		product_id = args['product_id']
		quantity = args['quantity']

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

		new_sale.save()

		return make_response(jsonify(
			{"message":"Sale record created successfully",
			"status":"created",
			"product":new_sale.__dict__}
			), 201)