import unittest
from controller.utils import formating_string_name


class FormatingStringTest(unittest.TestCase):

	def setUp(self):
		self.string1 = 'Pearl Jam'
		self.string2 = 'PearlJam'

	def test_if_was_formated(self):
		string1_expected = 'pearl-jam'
		result = formating_string_name(self.string1)
		
		self.assertEqual(string1_expected, result)
		
		string2_expected = 'pearljam'
		result = formating_string_name(self.string2)
		self.assertEqual(string2_expected, result)
