from ..database.db_setup import db

users = db.users

def is_user_valid(email, name, password):
	is_email_valid = '@' in email
	is_pw_long = True if len(password) > 6 else False
	username_doesnt_exists = True
	email_doesnt_exists = True

	registration_data = [is_email_valid, is_pw_long, username_doesnt_exists, email_doesnt_exists]

	for user in users.find():
		if(user['name'] == name):
			username_doesnt_exists = False

		if(user['email'] == email):
			email_doesnt_exists = False

	return all(registration_data)

