import os

from app import create_app

app = create_app(os.getenv('APP_SETTINGS'))


from app.database.db_con import migrate
migrate()

if __name__ == '__main__':
	app.run(debug=True)