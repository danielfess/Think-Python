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