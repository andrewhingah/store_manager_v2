from flask import Flask, Blueprint

# from flask_jwt_extended import JWTManager

from instance.config import app_config

def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)
	# jwt = JWTManager(app)

	from .api.v1 import version2 as v2

	app.register_blueprint(v2)

	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')

	return app
