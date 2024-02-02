# 33triples.py by Kenta Hsu 

import math

# function that finds all pythagorean triples 
# ie. a, b, c = 3, 4, 5 
# all sides must be integers 

# function takes argument n, finds all triples where a and b < 100

def triples(n):
	# this should iterate through half matrix + major diagonal
	for i in range(1, n):
		for j in range(i, n):	
			c = math.sqrt(i**2 + j**2)
			if math.isclose(c, c // 1):
				print(i, j, c)
triples(100)
				




