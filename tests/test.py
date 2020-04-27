import unittest
from packages.check_uniqueness.check_uniqueness import is_user_valid

class TestMain(unittest.TestCase):

	def test_is_email_valid(self):
		# assume
		test_email = 'test123.com'
		# action
		result = is_user_valid(test_email, 'asdf', '1234343')
		# assert
		self.assertFalse(result)

	def test_pw_length(self):
		# assume
		test_password = '12345'
		# action
		result = is_user_valid('test123@abv.bg', 'asdf', test_password)
		# assert
		self.assertFalse(result)
		
if __name__ == '__main__':
	unittest.main()
