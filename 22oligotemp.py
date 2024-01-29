# 22oligotemp.py by Kenta Hsu 

import sys

# compute oligo melting temp given # of each DNA base
# first see if see if length is longer or shorter than 13 bases 
# then calculate using respective formualas
def oligo_meltingtemp(a, t, g, c,):

	length = a+t+g+c  					# where meat of program starts
	if length <= 13:
		Tm = (a+t)*2 + (g+c)*4
		return Tm
	else:
		Tm = 64.9 + 41*(g+c - 16.4) / length
		return Tm

# longer than 13 
print(oligo_meltingtemp(10, 10, 10, 10))

# shorter than 13 
print(oligo_meltingtemp(5, 5, 1, 1))

# length of 13
print(oligo_meltingtemp(5, 5, 1, 2))


		

		


