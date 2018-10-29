from ....database import helpers

class User:
	'''Class represents operations related to products'''

	def __init__(self, name, email, username, password):
		self.name = name
		self.email = email
		self.username = username
		self.password = password


	# def signup(self):
	# 	payload = dict(
	# 		email = self.email,
	# 		username = self.username,
	# 		password = self.password
	# 		)

	# 	self.all_users.update({self.email:payload})


	# def get_one(self, email):

	# 	for key in User.all_users:
	# 		if key == email:
	# 			return User.all_users[key]
	# 	message = "User not found"
	# 	return message

	def signup(self):
		helpers.insert_user(self)
