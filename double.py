from datetime import datetime

def day_of_week():
	"""Returns the current day of the week."""

	d = datetime.now()
	weekday = d.weekday()
	days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
	print(days[weekday])

def birthday(year,month,day):
	"""Given a birthday, prints the user's age and the number
	of days, hours, minutes and seconds until their next birthday.

	year: integer
	month, day: integers (with the obvious restrictions)
	output: (non-negative int, Time object)
	"""

	birthday = datetime.fromisoformat('%.4d-%.2d-%.2d' % (year,month,day))
	today = datetime.now()
	if birthday.month > today.month:
		age_years = today.year - birthday.year - 1
	elif birthday.month < today.month:
		age_years = today.year - birthday.year
	else:
		if birthday.day <= today.day:
			age_years = today.year - birthday.year
		else:
			age_years = today.year - birthday.year - 1
	next_bday = datetime.fromisoformat('%.4d-%.2d-%.2d' % (year + age_years + 1,month,day))
	time_to_next_bday = next_bday - today
	print('Age:',age_years,', Time to next birthday:', next_bday - today)

def double(b1,b2):
	"""Given two distinct birthdays, computes the day on which one
	person is twice as old as the other.

	b1, b2: (year,month,day) tuples
	output: Datetime object
	"""

	d1 = datetime.fromisoformat('%.4d-%.2d-%.2d' % b1)
	d2 = datetime.fromisoformat('%.4d-%.2d-%.2d' % b2)
	if d1 > d2:
		d1, d2 = d2, d1
	return (d2 + (d2 - d1)).date()

def n_day(b1,b2,n):
	"""Given two distinct birthdays, computes the day on which one
	person is n times as old as the other.

	b1, b2: (year,month,day) tuples
	n: int > 1
	output: Datetime object
	"""

	d1 = datetime.fromisoformat('%.4d-%.2d-%.2d' % b1)
	d2 = datetime.fromisoformat('%.4d-%.2d-%.2d' % b2)
	if d1 > d2:
		d1, d2 = d2, d1
	return (d2 + (d2 - d1)/(n-1)).date()

if __name__ == '__main__':
	day_of_week()
	birthday(1994,2,23)
	double1 = double((1994,2,23),(1990,11,21))
	double2 = double((1990,11,21),(1994,2,23))
	print(double1)
	print(double2)
	triple = n_day((1994,2,23),(1990,11,21),3)
	print(triple)