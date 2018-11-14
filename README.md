[![Build Status](https://travis-ci.com/andrewhingah/store_manager_3.svg?branch=develop)](https://travis-ci.com/andrewhingah/store_manager_3)
[![Coverage Status](https://coveralls.io/repos/github/andrewhingah/store_manager_3/badge.svg?branch=bg-fix-tear-down-in-tests-%23161656911)](https://coveralls.io/github/andrewhingah/store_manager_3?branch=bg-fix-tear-down-in-tests-%23161656911)
[![Maintainability](https://api.codeclimate.com/v1/badges/262d9eee667b4517dcad/maintainability)](https://codeclimate.com/github/andrewhingah/store_manager_3/maintainability)
# store_manager_3
Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.
This is an implementation of a restful api to power the frontend pages.

## Endpoints

| Endpoints                    | Functionality              | Authorization              |
| -----------------------------|:--------------------------:| --------------------------:|
| POST /auth/signup            | Register a user            | Admin only                 |
| POST /auth/login             | Login a user               | Admin and store attendant  |
| GET /products                | Fetch all products         | Admin and store attendant  |
| GET /products/<productId>    | Fetch single product       | Admin and store attendant  |
| GET /sales                   | Fetch all sales            | Admin only                 |
| GET /sales/<saleId>          | Fetch a single sale        | Admin and the sale creater |
| POST /products               | Create a product           | Admin only                 |
| POST /sales                  | Create a sale order        | Store attendant only       |
| PUT /products/<productId>    | Modify a product           | Admin only                 |
| DELETE /products/<productId> | Delete an existing product | Admin only                 |

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

- Set up database

	Development database

	`$ psql -c 'create database <development_database>;' -U <postgres_username>`

	Testing database

	`$ psql -c 'create database <testing_database>;' -U <postgres_username>`

- Run tests `pytest --cov=app`

- Test the endpoints on postman.

	- Sign in as the default admin
	
		url:
			`http://127.0.0.1:5000/api/v2/auth/login`

		Headers
			`Content-Type: application/json`

		Body

			`{
				"email":"super@admin.com",
				"password":"A123@admin"
			}`


	- Copy the access token generated and add it as an `Authorization` header in the other requests

	- Post product

		A sample post product API request should look like this:

		Headers:
			`Content-Type: application/json`
			`Authorization: Bearer +access_token`


		Body

			`{
				"category": "electronics"
				"name": "Iphone 6",
				"quantity": "30",
				"price": 50500
			}`

	- To sign up a new store attendant

		url:
			`http://127.0.0.1:5000/api/v2/auth/signup`

		Headers:
			`Content-Type: application/json`
			`Authorization: Bearer +access_token`

		Body

			`{
				"name": "Henry John"
				"email":"henry@store.com",
				"password":"A123#tdg3",
				"role": "normal"
			}

	- Create a sale order

		A sample post sale API request should look like this:

			Headers:
				`Content-Type: application/json`
				`Authorization: Bearer +access_token`

			Body

				`{
					"product_id": 1,
					"quantity": "30"
				}`


## Built With

- Python 3

- Flask

- Flask-Restful

## Contributing

- Fork it from https://github.com/andrewhingah/store_manager_3/fork

- Create your feature branch `git branch somefeature` then `git checkout somefeature`

- Commit your changes `git commit "Add some feature"`

- Push to the branch `git push origin somefeature`

- Create a new pull request

## Author

Andrew Hinga
