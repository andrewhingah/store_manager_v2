from flask import Flask, Blueprint


from app.database.database import Database

from instance.config import app_config

db = Database()

def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	db.init_app(app)

	from .api.v2 import version2 as v2

	app.register_blueprint(v2)

	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')

	return app
