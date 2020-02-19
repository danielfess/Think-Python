import random

def has_duplicates(t):
    """Takes a list t and returns True if the list contains duplicates.
    
    t: list
    
    returns: bool
    """
    
    for item in t:
        if t.count(item) > 1:
            return True
    return False

def generate_birthdays():
    """Generates a list of 23 random birthdays (excluding 29th Feb)
    
    returns: list of 23 integers from 1 to 365
    """
    
    birthdays = []
    for i in range(23):
        x = random.randint(1,365)
        birthdays.append(x)
    return birthdays

count = 0
trials = 10000
for i in range(trials):
    list = generate_birthdays()
    if has_duplicates(list):
        count += 1
prob = count/trials
print('probability = ',prob)