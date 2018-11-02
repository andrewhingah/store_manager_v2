from flask import Flask, jsonify, make_response, request
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import (
	jwt_required, create_access_token, get_jwt_identity, get_raw_jwt, jwt_required)
from werkzeug.security import safe_str_cmp

from app.api.v2.models.helpers import insert_user,get_user

from app.api.v2.models.user_model import User
from app.api.v2.utils.validate import validate_email, validate_all


class UserRegistration(Resource):
	"""Registers a new user"""
	def post(self):
		"""Register a new user"""
		email = get_jwt_identity()
		user = get_user(email)

		data = request.get_json(force = True)
		name = data.get('name')
		email = data.get('email')
		password= data.get('password')
		role= data.get('role')

		if validate_all(name, email, password):
			return validate_all(name, email, password)

		user = get_user(email)

		if user is None:
			user = User(name=name, email=email, password=password, role=role)
			user.signup()

			return {"message":"User created!","user":user.__dict__}, 201
		else:
			return {'message':'Email already exists.'}, 202

class UserLogin(Resource):
	'''login a registered user'''
	def post(self):

		data = request.get_json()
		email = data.get('email')
		password = data.get('password')

		if validate_email(email):
			return validate_email(email)

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