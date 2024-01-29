# 21quadratic by Kenta Hsu

import math

# function that solves the quadratic formula
def quadratic(a, b, c):
	det = b**2 - 4*a*c
	if det >= 0:
		result1 = (-b + math.sqrt(det)) / (2*a)
		result2 = (-b - math.sqrt(det)) / (2*a)
		return result1, result2
	if det < 0:
		return 'no real root', 'no real root'
# no roots
x1, x2 = quadratic(5, 6, 7)
print(x1, x2, sep=', ')

# two real roots 
x1, x2 = quadratic(2, 10, 3)
print(x1, x2, sep=', ')

# one real root
x1, x2 = quadratic(2, 4, 2)
print(x1, x2, sep=', ')

