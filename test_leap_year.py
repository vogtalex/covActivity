import leapYear

def test_answer():
	assert leapYear.leapYearFinder(4) == True
	assert leapYear.leapYearFinder(100) == False
	assert leapYear.leapYearFinder(400) == True

def test_large_numbers():
	assert leapYear.leapYearFinder(50000) == True
	
def test_negatives():
	assert leapYear.leapYearFinder(-4) == True