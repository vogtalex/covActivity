import unittest
import leapYear

class testCaseAdd(unittest.TestCase):
	def test_add(self):
		self.assertEqual(leapYear.leapYearFinder(4), True)
		self.assertEqual(leapYear.leapYearFinder(100), True)
		self.assertEqual(leapYear.leapYearFinder(400), True)
		self.assertEqual(leapYear.leapYearFinder(3), True)

if __name__ == '__main__':
	unittest.main()