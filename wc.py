def linecount(filename):
	count = 0
	for line in open(filename):
		count += 1
	return count

if __name__ == '__main__':
	print(linecount('wc.py'))

print(__name__)