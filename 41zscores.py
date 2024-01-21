# 41zscores.py by Kenta Hsu 
# count how many randomly generated numbers from a normal distribution is above 1, 2, and 3 standard deviations

import random
z1 = 0
z2 = 0
z3 = 0
limit = 100000
for i in range(limit):
	r = random.gauss(0.0, 1.0)
	if r > 1: z1 += 1
	if r > 2: z2 += 1
	if r > 3: z3 += 1
print(1 - 2*z1/limit)	# times two because values on both side of the mean 
print(1 - 2*z2/limit)
print(1 - 2*z3/limit)
