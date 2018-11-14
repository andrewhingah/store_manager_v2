from flask import Flask, jsonify, make_response, request
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import (
	jwt_required, create_access_token, get_jwt_identity, get_raw_jwt, jwt_required)
from werkzeug.security import safe_str_cmp

from app.api.v2.models.helpers import insert_user,get_user

from app.api.v2.models.user_model import User
from app.api.v2.utils.validate import validate_email, validate_all
import datetime

class UserRegistration(Resource):
	"""Registers a new user"""
	@jwt_required
	def post(self):
		"""Register a new user"""
		email = get_jwt_identity()
		user = get_user(email)

		if user['role'] != 'admin':
			return {"message": "You don't have access to this page"}, 403

		data = request.get_json(force = True)
		name = data.get('name')
		email = data.get('email')
		password= data.get('password')
		role= data.get('role')
		print (role)

		if validate_all(name, email, password):
			return validate_all(name, email, password)

		if not role:
			return {"message": "Role must be provided"}, 400

		if str(role) != 'admin' and str(role) != 'normal':
			return {"message": "Role should either be admin or normal"}, 400

		user = get_user(email)

		if user is None:
			user = User(name=name, email=email, password=password, role=role)
			user.signup()

			return {"message":"User created!","user":user.__dict__}, 201
		else:
			return {'message':'User with that email already exists.'}, 202

class UserLogin(Resource):
	'''login a registered user'''
	def post(self):

		data = request.get_json()
		email = data.get('email')
		password = data.get('password')

		if not password:
			return {"Status": "Error", "message": "Password must be provided"}, 400

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
			exp=datetime.timedelta(minutes=120)
			token = create_access_token(identity=email,expires_delta=exp)

		return make_response(jsonify(
			{'message': 'Logged in successfully!', 'token': token}), 201)