def reversible_ages(age1,age2):
    """Returns True if the two ages are reverses of each other when written
    as two-digit numbers.

    age1, age2: integers < 100
    """
    
    age1 = str(age1).zfill(2)
    age2 = str(age2).zfill(2)
    return age1 == age2[::-1]

def past_reversible(age,age_diff):
    """For two people of ages (age) and (age + age_diff) (with the same
    birthday), counts how many times in the past (i.e. not including current
    year) the two people's ages have been the reverse of each other.

    age, age_diff: integers, with age + age_diff < 100
    """
    
    count = 0
    for i in range(age):
        if reversible_ages(i,i+age_diff):
            count = count + 1
    return count

print(past_reversible(79,9))

def future_reversible(age,age_diff):
    """For two people of ages (age) and (age + age_diff) (with the same
    birthday), counts how many times in the future the two people's ages
    will be the reverse of each other (e.g. 37 and 73), with a maximum age
    of 99.
    
    age, age_diff: integers, with age + age_diff < 100
    """
    
    count = 0
    i = age + 1
    while i + age_diff < 100:
        if reversible_ages(i,i+age_diff):
            count = count + 1
        i = i + 1
    return count

print(future_reversible(97,36))

for i in range(100):
    j = 1
    while i + j <= 100:
        if (past_reversible(i,j) == 5 and 
            future_reversible(i,j) == 2 and
            reversible_ages(i,i+j)):
            print(i,j)
        j = j + 1