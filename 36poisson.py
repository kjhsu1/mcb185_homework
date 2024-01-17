# 36poisson.py by Kenta Hsu
import math
# poisson probabilty models probabilities of rare events that occur independantly from each other 
# expectation, or lambda, is # of that particular event we expect to observe in a given interval 

def poisson(n, k):
	expectation = n * ((n**k) * ((math.e ** -n) / math.factorial(k)))
	probability = ((math.e)**(-expectation) * expectation**k) / math.factorial(k)
	return probability
print(poisson(5, 6))
