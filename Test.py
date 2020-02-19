prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter in 'OQ':
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)

fruit = 'banana'

def in_both(word1,word2):
    for letter in word1:
        if letter in word2:
            print(letter)

print(' banana' == 'banana')
print('banana' == 'banana')

new_fruit = fruit.upper()
print(new_fruit)
old_fruit = new_fruit.lower()
print(old_fruit)

cheeses = ['cheddar','swiss','gruyere']
for cheese in cheeses:
    cheese = cheese + '0'
    print(cheese)
print(cheeses)
print(cheeses.append('brie'))
print(cheeses)

s = ' '.join(cheeses)
t = ''.join(cheeses)
print(s)
print(t)

t = ['a','b','c','b']
t.remove('b')
print(t)
t.remove('b')
print(t)

def example3():
    t = []

example3()
print(t)

def example4(t):
    t = []

example4(t)
print(t)

s = [1,2,3]

def example5():
    global t
    t = []
    if 1 in s:
        s.append(4)
        print('list s')
        print(s)

example5()
print(t)

def example6(t):
    t += [4]
    s.append(4)
#Note: If I write s += [4], we get an error since local variable s doesn't
#exist - though s.append(4) works, since append acts on the global s.

example6(t)
print(t)
print(s)