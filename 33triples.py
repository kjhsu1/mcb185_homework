# 33triples.py by Kenta Hsu 

import math

# function that finds all pythagorean triples 
# ie. a, b, c = 3, 4, 5 
# all sides must be integers 

# function takes argument n, finds all triples where a + b < 100

def triples(n):
	for i in range(1, n - 2):
		for j in range(i,n - 2):	# this should iterate through half matrix + major diagonal
			if i + j < 100 and math.isclose(math.sqrt(i**2 + j**2), math.sqrt(i**2 + j**2) // 1):
				print(i, j, math.sqrt(i**2 + j**2))
triples(100)
				




