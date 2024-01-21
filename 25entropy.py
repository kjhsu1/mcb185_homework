# 25entropy.py by Kenta Hsu

import math

# Shannon entropy measures randomness of data, in this case nucleotides
# Takes dna seq as an input, 
def shannon_entropy(a, t, g, c):
	total_nuc = a+t+g+c
	
	a_prob = a / total_nuc							# probability of occurance for each base
	t_prob = t / total_nuc
	g_prob = g / total_nuc
	c_prob = c / total_nuc
	
	a_expression = a_prob * math.log(a_prob, 2)		# expressions inside the sigma
	t_expression = t_prob * math.log(t_prob, 2)
	g_expression = g_prob * math.log(g_prob, 2)
	c_expression = c_prob * math.log(c_prob, 2)

	entropy = -(a_expression + t_expression + g_expression + c_expression)	# final entropy value
	return entropy

# testing  
print(shannon_entropy(1, 2, 3, 4))

# testing part 2 
print(shannon_entropy(5,6,30,100000000000000000000))

# testing part 3
# print(shannon_entropy(10000000,0,0,5))	# when there is not a single base for a, t, g, or c, can we just make the expression equal to 0)


