print('start: append method')
file = open('words.txt')
list = []
for line in file:
    word = line.strip()
    list.append(word)
print('end: append method')


print('start: +[x] method')
file = open('words.txt')
list = []
print(list)
for line in file:
    word = line.strip()
    list = list + [word]
print('end: +[x] method')

