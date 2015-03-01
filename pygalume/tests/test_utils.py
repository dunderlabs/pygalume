import unittest
from controller.utils import formating_string_name


class FormatingStringTest(unittest.TestCase):

	def setUp(self):
		self.string1 = 'Pearl Jam'
		self.string2 = 'PearlJam'
		self.string3 = 'Pearl Jam '
		self.string4 = ' Pearl Jam'

	def test_if_was_formated(self):
		expected = 'pearl-jam'
		result = formating_string_name(self.string1)
		self.assertEqual(expected, result)
		
		expected = 'pearljam'
		result = formating_string_name(self.string2)
		self.assertEqual(expected, result)

		expected = 'pearl-jam'
		result = formating_string_name(self.string3)
		self.assertEqual(expected, result)

		result = formating_string_name(self.string4)
		self.assertEqual(expected, result)