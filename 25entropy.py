# 25entropy.py by Kenta Hsu

import math

# Shannon entropy measures randomness of data, in this case nucleotides
# Takes dna seq as an input, 
def shannon_entropy(a, c, g, t):
	# intializing
	h = 0 
	total_nuc = a+t+g+c
	
	a_prob = a / total_nuc							# probability of occurance for each base
	c_prob = c / total_nuc
	g_prob = g / total_nuc
	t_prob = t / total_nuc
	
	if a_prob != 0: h = h + a_prob * math.log(a_prob, 2)		# expressions inside the sigma
	if c_prob != 0: h = h + c_prob * math.log(c_prob, 2)
	if g_prob != 0: h = h + g_prob * math.log(g_prob, 2)
	if t_prob != 0: h = h + t_prob * math.log(t_prob, 2)

	return -h	# final entropy value

# testing  
print(shannon_entropy(1, 2, 3, 4))

# testing part 2 
print(shannon_entropy(5,6,30,10000))

# testing part 3
# print(shannon_entropy(10000000,0,0,5))	


