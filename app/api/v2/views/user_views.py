from flask import Flask, jsonify, make_response, request
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import (
	jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)
from werkzeug.security import safe_str_cmp

from app.api.v2.models.helpers import insert_user,get_user

from app.api.v2.models.user_model import User


class UserRegistration(Resource):
	"""All products class"""

	def post(self):
		"""Register a new user"""

		data = request.get_json()
		name = data['name']
		email = data['email']
		password= data['password']

		user = get_user(email)

		if user is None:
			user = User(name=name, email=email, password=password)
			user.signup()

			return make_response(jsonify(
				{"message":"User created!",
				"user":user.__dict__}
				), 201)
		else:
			return make_response(jsonify(
				{'message':'Email already exists.'}), 202)

class UserLogin(Resource):
	'''login a registered user'''
	def post(self):

		data = request.get_json()
		email = data['email']
		password = data['password']

		user = get_user(email)
		if user is None:
			return make_response(jsonify(
				{"message": "Your account does not exist! Please register"}),
				 401)

		elif not safe_str_cmp(password, user['password']):
			return make_response(jsonify(
				{'message': "Incorrect password"}), 400)
		else:
			token = create_access_token(identity=email)

		return make_response(jsonify(
			{'message': 'Logged in successfully!', 'token': token}), 201)