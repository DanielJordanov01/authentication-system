import sys
import bcrypt
from packages.database.db_setup import db
from packages.check_uniqueness.check_uniqueness import is_user_valid

# get user data
name = sys.argv[1]
email = sys.argv[2]
password = sys.argv[3]

users = db.users

# convert password to bytes
password = password.encode()

# Recieves True or Flase if the user data is valid
is_valid = is_user_valid(email, name, password)

# hash password
hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())

# register user
if(is_valid):
	user_data = {
		'name': name,
		'email': email,
		'password': hashed_pw
	}

	user = users.insert_one(user_data)
	print('Registered!')
else:
	print('Error')
