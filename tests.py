import unittest
from credit_card_validator import credit_card_validator

class TestCCValidator(unittest.TestCase):
	def test1(self):
		"""First test with an arbitrary number.
		Picked just to test my gradescope, but will fail length, prefix, and checksum"""
		card_num = "0123456789"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

if __name__ == '__main__':
	unittest.main(verbosity=2)
