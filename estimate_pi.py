import math

def factorial(n):
    while n > 0:
        return n*factorial(n-1)
    return 1

summand = 10
estimate = 0
index = 0
while summand >= 1e-15:
    summand = 2*math.sqrt(2)/9801*factorial(4*index)*(1103+26390*index)/factorial(index)**4/396**(4*index)
    estimate = estimate + summand
    index = index + 1

print(1/estimate)
print(math.pi)
print(estimate*math.pi)
print(1/estimate-math.pi)
print(estimate-1/math.pi)
print(summand)
print(index)