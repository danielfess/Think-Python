import copy

class Time:
	"""Represents the time of day.

	Attributes: hour, minute, second.
	"""

def print_time(time):
	print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

def is_after(t1,t2):
	"""Returns True if the time object t1 is chronologically after
	the time object t2.

	t1, t2: time objects
	"""

	bool1 = t1.hour > t2.hour
	bool2 = t1.hour == t2.hour and t1.minute > t2.minute
	bool3 = t1.hour == t2.hour and t1.minute == t2.minute and t1.second >= t2.second
	return bool1 or bool2 or bool3 

def increment(time,seconds):
	"""Advances the given time object by the given number of seconds.

	time: time object
	seconds: non-negative int
	"""

	time.second += seconds
	time.minute += time.second//60
	time.second = time.second % 60
	time.hour += time.minute//60
	time.minute = time.minute % 60

def increment2(time,seconds):
	"""Same as increment, but returns a new time object."""

	new_time = copy.copy(time)
	increment(new_time,seconds)
	return new_time


if __name__ == '__main__':
	t1 = Time()
	t1.hour = 12
	t1.minute = 39
	t1.second = 13

	t2 = Time()
	t2.hour = 13
	t2.minute = 11
	t2.second = 9

	t3 = Time()
	t3.hour = 12
	t3.minute = 37
	t3.second = 56

	print_time(t1)
	print_time(t2)
	print_time(t3)
	print(is_after(t1,t2))
	print(is_after(t1,t3))
	increment(t1,46)
	print_time(t1)
	increment(t1,12)
	print_time(t1)
	t4 = increment2(t1,115)
	print_time(t1)
	print_time(t4)