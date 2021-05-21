def leapYearFinder(num):
	leapYear = 0

	if (num % 4) == 0:
		leapYear = 1
		if (num % 100) == 0:
			leapYear = 0
			if (num % 400) == 0:
				leapYear = 1

	if (leapYear == 0):
		return False
	if (leapYear == 1):
		return True
