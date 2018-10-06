import unittest
import os

def analyze_text(filename):
	lines = 0
	chars = 0
	with open(filename, 'r') as f:
		for line in f:
			lines+=1
			chars+=len(line)
	#print(lines, chars)
	return (lines, chars)

class TextAnalysisTests(unittest.TestCase):
	"""Test  for the analyze_text() function """

	def setUp(self):
		"""Fixture that creates a file for the text methods we use"""
		self.filename = 'text_analysis_text_file.txt'
		with open(self.filename, 'w') as f:
			f.write('Now we are engaged in a great civil war.\n'
					'testing whether tat nation,\n'
					'or any nation so conceived and so dedicated,\n'
					'can long endure.')

	def tearDown(self):
		"""Fixture that deletes the files used by test method"""
		try:
			os.remove(self.filename)
		except:
			pass

	def test_function_runs(self):
		"""basic smoke test: does the function run?"""
		analyze_text(self.filename)

	def test_line_count(self):
		"""check line count is correct"""
		self.assertEqual(analyze_text(self.filename)[0], 4)

	def test_character_count(self):
		"""check that the character count is correct."""
		self.assertEqual(analyze_text(self.filename)[1], 130)

	def test_no_such_file(self):
		"""check the proper exception is thrown"""
		with self.assertRaises(IOError):
			analyze_text('foobar')

	def test_no_deletion(self):
		"""Check the function doesnt delete the input file"""
		analyze_text(self.filename)
		self.assertTrue(os.path.exists(self.filename))



if __name__ == '__main__':
	unittest.main()
