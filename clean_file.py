import string

def clean_file(text):
    """Reads the file 'text', breaks each line into words, removes
    all whitespace and punctuation, and converts to lowercase.

    text: text file

    output: list
    """

    file = open(text)
    cleaned_text = []
    for line in file:
    	line = line.strip()
    	table = line.maketrans(line,line,string.punctuation)
    	line = line.translate(table)
    	line = line.lower()
    	line_list = line.split(' ')
    	line_list2 = []
    	for word in line_list:
    		if word != '':
    			line_list2.append(word)
    	cleaned_text.append(line_list2)
    return cleaned_text

clean = clean_file('words.txt')
