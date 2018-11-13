"""Module has the create app function"""
from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager
from flask_cors import CORS


from app.db_con import Database

db = Database()

from instance.config import app_config

def create_app(config_name):
	"""define app and register blueprint"""
	app = Flask(__name__, instance_relative_config=True)
	CORS(app)

	jwt = JWTManager(app)

	app.config.from_object(app_config[config_name])
	db.init_app(app)

	from .api.v2 import version2 as v2

	app.register_blueprint(v2)

	return app
