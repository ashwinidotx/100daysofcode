import unittest

def digits(x):
	"""convert in integer into a list of digits."""

	digs = []
	while x!=0:
		div, mod = divmod(x, 10)
		digs.append(mod)
		x=div
	return digs

def is_pallindrome(x):
	"""Determine if an integer is a pallindrome"""
	digs = digits(x)
	for f, r in zip(digs, reversed(digs)):
		if f!=r:
			return False
	return True

#-----------------------------------#

class Tests(unittest.TestCase):
	"""Tests for the is_pallindrome() function"""

	def test_negative(self):
		"""Check that it returns false correctly."""
		self.assertFalse(is_pallindrome(1234))

	def test_positive(self):
		"""Check that it returns true correctly."""
		self.assertTrue(is_pallindrome(1234321))

	def test_single_digit(self):
		"""check that it works for a single digit"""
		for i in range(10):
			self.assertTrue(is_pallindrome(i))


if __name__ == '__main__':
	unittest.main()