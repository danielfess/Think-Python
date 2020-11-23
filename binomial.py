def binomial_coeff(n,k):
	"""Compute the binomial coefficient "n choose k".

	n: number of trials
	k: number of successes

	returns: int
	"""

	#x = 1 if k==0 else 0
	return binomial_coeff(n-1,k) + binomial_coeff(n-1,k-1) if k>0 and n>0 else (1 if k==0 else 0)

print(binomial_coeff(0,0))
print(binomial_coeff(0,1))
print(binomial_coeff(1,0))
print(binomial_coeff(1,1))
print(binomial_coeff(1,2))
print(binomial_coeff(3,2))
print(binomial_coeff(5,3))
print(binomial_coeff(4,2))
print(binomial_coeff(2,0))