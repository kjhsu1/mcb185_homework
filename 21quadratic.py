# 21quadratic by Kenta Hsu

import math

# function that solves the quadratic formula
def quadratic(a,b,c):
	assert(type(a) == int or type(a) == float)
	assert(type(b) == int or type(b) == float)
	assert(type(c) == int or type(c) == float)
	det = b**2 - 4*a*c
	if det >= 0:
		return (-b + math.sqrt(b**2 - 4*a*c)) / (2*a), (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
	if det < 0:
		return 'no real root', 'no real root'
# no roots
x1, x2 = quadratic(5,6,7)
print(x1, x2, sep=', ')

# two real roots 
x1, x2 = quadratic(2,10,3)
print(x1, x2, sep=', ')

# one real root
x1, x2 = quadratic(2,4,2)
print(x1, x2, sep=', ')

