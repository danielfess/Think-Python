def sed(pattern,replacement,file1,file2):
	"""Reads file1, writes the contents into file2.  Anywhere
	the string 'pattern' appears, replace it with the string
	'replacement'.

	pattern, replacement: strings
	file1, file2: filenames
	"""

	try:
		f1 = open(file1)
	except:
		print(file1, 'does not exist in this directory')
		return
	try:
		f2 = open(file2,'w')
	except:
		print(file2, 'is not a valid filename')
		return
	for line in f1:
		newline = line.replace(pattern,replacement)
		f2.write(newline)
	f1.close()
	f2.close()

sed('apples','peaches','sed_test1.txt','sed_test2.txt')
sed('apples','peaches','sed_test3.txt','sed_test2.txt')
sed('apples','peaches','sed_test1.txt','sed_test2.t')
f = open('sed_test2.t')
for line in f:
	print(line)