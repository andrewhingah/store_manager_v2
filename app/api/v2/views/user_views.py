from flask import Flask, jsonify, make_response, request
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import (jwt_required, create_access_token, get_jwt_identity, get_raw_jwt)
from werkzeug.security import safe_str_cmp

from ....database.helpers import insert_user,get_user

from ..models.user_model import User


parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('email')
parser.add_argument('username')
parser.add_argument('password')

class UserRegistration(Resource):
	"""All products class"""

	def post(self):
		"""Register a new user"""
		
		args = parser.parse_args()
		name = args['name']
		email = args['email']
		username = args['username']
		password = args['password']

		user = get_user(email)

		if user is None:
			user = User(name, email, username, password)
			user.signup()

			return make_response(jsonify(
				{"message":"User created!",
				"user":user.__dict__}
				), 201)
		else:
			return make_response(jsonify({'message':'Email already exists.'}))

class UserLogin(Resource):
	'''login a registered user'''
	def post(self):
		args = parser.parse_args()
		email = args['email']
		password = args['password']

		user = get_user(email)
		if user is None:
			return jsonify({"message": "Your account does not exist, please register"}), 404

		elif not safe_str_cmp(password, user['password']):
			return jsonify({'message': "Incorrect password"}), 400
		else:
			token = create_access_token(identity=email)

		return jsonify({'message': 'Logged in successfully!', 'token': token})