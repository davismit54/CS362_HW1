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
		"""Boundary test with Amex prefix edge case of 34 (valid)"""
		card_num = "349478209483922"
		self.assertTrue(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test4(self):
		"""Boundary test with Amex prefix edge case of 35 (invalid)"""
		card_num = "359028684920562"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test5(self):
		"""Boundary test with Amex prefix edge case of 36 (invalid)"""
		card_num = "363920384502480"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test6(self):
		"""Boundary test with Amex prefix edge case of 37 (valid)"""
		card_num = "349478209483922"
		self.assertTrue(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test7(self):
		"""Boundary test with Amex prefix edge case of 38 (invalid)"""
		card_num = "381235769370231"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test8(self):
		"""Boundary test with MC prefix edge case of 50 (invalid)"""
		card_num = "5038927492018394"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test9(self):
		"""Boundary test with MC prefix edge case of 51 (valid)"""
		card_num = "5148202485492031"
		self.assertTrue(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test9a(self):
		"""Boundary test with MC prefix edge case of 55 (valid)"""
		card_num = "5548202485492037"
		self.assertTrue(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test10(self):
		"""Boundary test with MC prefix edge case of 56 (invalid)"""
		card_num = "5628304849036147"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test11(self):
		"""Boundary test with MC prefix edge case of 2220 (invalid)"""
		card_num = "2220374591275499"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test12(self):
		"""Boundary test with MC prefix edge case of 2221 (valid)"""
		card_num = "2221374380240497"
		self.assertTrue(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)
	
	def test12a(self):
		"""Boundary test with MC prefix edge case of 2720 (valid)"""
		card_num = "2720239484058341"
		self.assertTrue(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test13(self):
		"""Boundary test with MC prefix edge case of 2721 (invalid)"""
		card_num = "2721384027592346"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)
	
	def test14(self):
		"""Boundary test with Visa prefix edge case of 4 (valid)
		Amex and MC tests include 3 and 5, so no more needed"""
		card_num = "4370275028493452"
		self.assertTrue(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test14(self):
		"""Length of 0 test for error guessing (invalid)"""
		card_num = ""
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)
	
	def test15(self):
		"""only 0s test for error guessing (invalid)"""
		card_num = "0000000000000000"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)
	
	def test16(self):
		"""Boundary Test for Amex length of 14 (invalid)"""
		card_num = "34193280402846"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)
	
	def test17(self):
		"""Boundary Test for Amex length of 16 (invalid)"""
		card_num = "3719328040284342"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test18(self):
		"""Boundary Test for MC length of 15 (invalid)"""
		card_num = "513802792754045"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test19(self):
		"""Boundary Test for MC length of 17 (invalid)"""
		card_num = "27203794720574835"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test20(self):
		"""Boundary Test for Visa length of 15 (invalid)"""
		card_num = "458303729492459"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test21(self):
		"""Boundary Test for Visa length of 17 (invalid)"""
		card_num = "45830372949243335"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test22(self):
		"""Error guess of valid entry plus a leading zero (invalid)"""
		card_num = "04372072049275895"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test23(self):
		"""Error guessing of lots of zeros for checksum (valid)"""
		card_num = "4000000000000002"
		self.assertTrue(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)
	
	def test24(self):
		"""Error guessing crazy length (invalid)"""
		card_num = "293847592837458972349578298345789237458972938457923847598273495872934875928347592734589724395729384579823745982734598273458972938457928347598237"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test25(self):
		"""Boundary check, incorrect checksum Visa (invalid)"""
		card_num = "4565798658765787" #checksum should be 8
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)
	
	def test26(self):
		"""Boundary check, incorrect checksum Visa (invalid)"""
		card_num = "4565798658765789" #checksum should be 8
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test27(self):
		"""Boundary check, incorrect checksum MC (invalid)"""
		card_num = "5537029402384043" #checksum should be 4
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)
	
	def test28(self):
		"""Boundary check, incorrect checksum MC (invalid)"""
		card_num = "5537029402384045" #checksum should be 4
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

	def test29(self):
		"""Boundary check, incorrect checksum Amex (invalid)"""
		card_num = "372904820489328" #checksum should be 9
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)
	
	def test30(self):
		"""Boundary check, incorrect checksum Amex (invalid)"""
		card_num = "372904820489320" #checksum should be 9
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

"""Got bugs 1-8 and 10, need #9
Starting Partition Testing for corner cases
Features:
	CC number string
Categories:
	Length:
		MC and Visa: <16	Amex < 15
		MC and Visa: = 16	Amex = 15
		MC and Visa: >16	Amex > 15
	Prefix:
		Visa: 4
		MC: 51-55 & 2221-2720
		Amex: 34 & 37
	Checksum:
		correct
		incorrect
"""
def test31(self):
		"""Partition test with Amex prefix edge case of 33 (invalid)
		with invalid checksum"""
		card_num = "3312312312312316"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

def test32(self):
		"""Partition test with Amex prefix edge case of 34 (valid)
		with invalid checksum"""
		card_num = "349478209483921"
		self.assertTrue(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

def test33(self):
		"""Partition test with Amex prefix edge case of 35 (invalid)
		with invalid checksum"""
		card_num = "359028684920563"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

def test34(self):
		"""Partition test with Amex prefix edge case of 36 (invalid)
		with invalid checksum"""
		card_num = "363920384502489"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

def test35(self):
		"""Partition test with Amex prefix edge case of 37 (valid)
		with invalid checksum"""
		card_num = "349478209483920"
		self.assertTrue(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

def test36(self):
		"""Partition test with Amex prefix edge case of 38 (invalid)
		with invalid checksum"""
		card_num = "381235769370233"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

def test37(self):
		"""Partition test with MC prefix edge case of 50 (invalid)
		with invalid checksum"""
		card_num = "5038927492018398"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

def test38(self):
		"""Partition test with MC prefix edge case of 51 (valid)
		with invalid checksum"""
		card_num = "5148202485492033"
		self.assertTrue(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

def test39(self):
		"""Partition test with MC prefix edge case of 55 (valid)
		with invalid checksum"""
		card_num = "5548202485492036"
		self.assertTrue(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

def test40(self):
		"""Partition test with MC prefix edge case of 56 (invalid)
		with invalid checksum"""
		card_num = "5628304849036143"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

def test41(self):
		"""Partition test with MC prefix edge case of 2220 (invalid)
		with invalid checksum"""
		card_num = "2220374591275491"
		self.assertFalse(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)

def test42(self):
		"""Partition test with MC prefix edge case of 2221 (valid)
		with invalid checksum"""
		card_num = "2221374380240492"
		self.assertTrue(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)
	
def test43(self):
		"""Partition test with MC prefix edge case of 2720 (valid)
		with invalid checksum"""
		card_num = "2720239484058345"
		self.assertTrue(credit_card_validator(card_num), msg='credit_card_validator({})'.format(card_num),)



if __name__ == '__main__':
	unittest.main(verbosity=2)
