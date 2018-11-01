[![Maintainability](https://api.codeclimate.com/v1/badges/262d9eee667b4517dcad/maintainability)](https://codeclimate.com/github/andrewhingah/store_manager_3/maintainability)
# store_manager_3
Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purpose

## Prerequisites

- [Git](https://git-scm.com/downloads)
- [Postman](https://www.getpostman.com/apps)
- [Python 3.6](https://www.python.org/)
- [PostgreSQL](https://www.postgresql.org/)

## Installing

- Clone this repository. `git clone https://github.com/andrewhingah/store_manager_3.git`


- To test API locally, set up a virtual environment in the base project folder

	- `virtualenv venv`

- Create a `.env` file and add the following variables

	`source venv/bin/activate`

	`export FLASK_APP="run.py"`

	`export FLASK_ENV="development"`

	`export SECRET="your_secret_key"`

	`export APP_SETTINGS="development"`


- Source the environment variables: `source .env`

- Install dependecies `pip install -r requirements.txt`

- Run tests `pytest` or `nosetests --exe --with-coverage --cover-package=api`

- Test the endpoints on postman.

	- First create a new user through url `http://127.0.0.1:5000/api/v2/auth/signup`

		Header: `Content-Type: application/json`

		Sample request:

		`{
			"name":"smith",
			"email":"smith@gmail.com",
			"password":"QWdre6po_@"
		}`

	- Sign in the user: url: `http://127.0.0.1:5000/api/v2/auth/login`

		`{
			"email":"smith@gmail.com",
			"password":"7QWdre6po_@"
		}`


		Header: `Content-Type: application/json`

	- Copy the access token generated and post it on the bearer section part in every other endpoint you wish to test:

	- A sample post product API request should look like this:

		Header: `Content-Type: application/json`

		`{
			"category": "electronics"
			"name": "Iphone 6",
			"quantity": "30",
			"price": 50500
		}`

The following endpoints should work:

- `POST /auth/signup`

- `POST /auth/login`

- `GET /products`

- `GET /products/<productId>`

- `PUT /products/<productId>`

- `DELETE /products/<productId>`

- `GET /sales`

- `GET /sales/<saleId>`

- `POST /products`

- `POST /sales`

## Built With

- Python 3

- Flask

- Flask-Restful

## Contributing

- Fork it from https://github.com/andrewhingah/storemanager/fork

- Create your feature branch `git branch somefeature` then `git checkout somefeature`

- Commit your changes `git commit "Add some feature"`

- Push to the branch `git push origin somefeature`

- Create a new pull request

## Author

Andrew Hinga
