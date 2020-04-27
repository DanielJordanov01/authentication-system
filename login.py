import sys
import bcrypt
from packages.database.db_setup import db

email = sys.argv[1]
password = sys.argv[2]

users = db.users

password = password.encode()

def check_credentials(user):
	if(user['email'] == email and bcrypt.checkpw(password, user['password'])):
		print('Logged in!')
	else:
		print('Wrong credentials!')

for user in users.find():
	check_credentials(user)
