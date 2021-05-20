import unittest
import leapYear

class testCaseAdd(unittest.TestCase):
	def test_add(self):
		self.assertEqual(leapYear.leapYearFinder(4), True)
		self.assertEqual(leapYear.leapYearFinder(100), False)
		self.assertEqual(leapYear.leapYearFinder(400), True)
		self.assertEqual(leapYear.leapYearFinder(3), False)

	def test_add_large_numbers(self):
		self.assertEqual(leapYear.leapYearFinder(50000), True)

	def test_add_negatives(self):
		self.assertEqual(leapYear.leapYearFinder(-4), True)

if __name__ == '__main__':
	unittest.main()