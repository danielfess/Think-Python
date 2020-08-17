import os
import hashlib

def files_with_suffix(dir,suffix):
	"""Returns a list of all files in a directory and
	its subdirectories which end with the given suffix

	dir: directory
	suffix: string
	"""

	contents = os.listdir(dir)
	suffix_files = []
	n = len(suffix)
	for name in contents:
		path = os.path.join(dir,name)
		if os.path.isdir(name):
			suffix_files += files_with_suffix(path,suffix)
		else:
			if path[-n:] == suffix:
				suffix_files.append(path)
	return suffix_files

def check_duplicates(file1,file2):
	"""Computes the md5 checksum of two files to see
	if they are the same file.

	file1, file2: filenames
	"""

	h1 = hashlib.md5(file1.encode('utf-8')).hexdigest()
	h2 = hashlib.md5(file2.encode('utf-8')).hexdigest()
	if h1 == h2:
		return True
	else:
		return False

def check_duplicates2(file1,file2):
	"""Uses the Unix command diff to see if two files
	are the same file.

	file1, file2: filenames
	"""

	fp = os.popen('diff ' + file1 + ' ' + file2)
	res = fp.read()
	stat = fp.close()
	return res, stat

#This code fails.  The code in the book doesn't work.
#Python must have upgraded to a newer version.

if __name__ == '__main__':
	py_files = files_with_suffix('C:\\Users\\danie\\OneDrive\\Documents\\Think_Python','.py')
	duplicates = []
	for f1 in py_files:
		print(f1)
		for f2 in py_files:
			if f1 != f2:
				if check_duplicates(f1,f2):
					duplicates.append((f1,f2))
					#print(check_duplicates2(f1,f2))
	print(duplicates)
				

