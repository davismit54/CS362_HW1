import unittest
from credit_card_validator import credit_card_validator

class TestCCValidator(unittest.TestCase):
	def test1(self):
		"""First test with an arbitrary invalid number.
		Picked just to test my gradescope, but will fail length, prefix, and checksum"""
		card_num = "0123456789"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)
	
	def test2(self):
		"""Boundary test with Amex prefix edge case of 33 (invalid)"""
		card_num = "3312312312312315"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test3(self):
		"""Boundary test with Amex prefix edge case of 38 (invalid)"""
		card_num = "381235769370231"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test4(self):
		"""Boundary test with Amex prefix edge case of 34 (valid)"""
		card_num = "349478209483922"
		self.assertTrue(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

if __name__ == '__main__':
	unittest.main(verbosity=2)
