# 63dust.py by Kenta Hsu

# another sliding window alg 
# calculate shannon entropy for each window 
# if low entropy -> replace bases with 'N'
# low entropy = repetitive seq or low diversity 
# rep seq and low div sequences can create false positives 

import math 
import sys
import mcb185

# stdin -> variables
path = sys.argv[1]
w = int(sys.argv[2])
threshold = sys.argv[3]

# FASTA reader
deflines = []
seqs = []
for defline, seq in mcb185.read_fasta(path):
	deflines.append(defline)
	seqs.append(seq)

# only using first seq (b/c there's only one)
seq = seqs[0]

def shannon_entropy(a, c, g, t):
	# intializing
	h = 0 
	total_nuc = a+t+g+c
	
	# probability of occurance for each base
	a_prob = a / total_nuc			
	c_prob = c / total_nuc
	g_prob = g / total_nuc
	t_prob = t / total_nuc
	
	if a_prob != 0: 
		# expressions inside the sigma
		h = h + a_prob * math.log2(a_prob)
	if c_prob != 0: 
		h = h + c_prob * math.log2(c_prob)
	if g_prob != 0: 
		h = h + g_prob * math.log2(g_prob)
	if t_prob != 0: 
		h = h + t_prob * math.log2(t_prob)

	return -h	# final entropy value

def dust(seq, w, threshold):
	# so we can change char to 'N'
	seq_as_list = list(seq)
	# same idea as 62skewer 
	# only need to take a, t, g, c, count for the first frame
	# we need each nt count for entropy calc
	first_frame = seq[:w]
	a = first_frame.count('A')
	c = first_frame.count('C')
	g = first_frame.count('G')
	t = first_frame.count('T')
	# check first frame separately 
	if shannon_entropy(a, c, g, t) < 1.4:
		for i in range(w-1): seq_as_list[i] = 'N' 
	
	# now do the rest
	for i in range(1, len(seq_as_list) -w +1):
		# update counts 
		# need to do seq[i-1] not seq_as_list[i-1]
		# bc seq_as_list may contain masked nts
		if seq[i-1] == 'A': a -= 1 
		if seq[i-1] == 'C': c -= 1
		if seq[i-1] == 'G': g -= 1
		if seq[i-1] == 'T': t -= 1

		if seq[i+w-1] == 'A': a += 1
		if seq[i+w-1] == 'C': c += 1
		if seq[i+w-1] == 'G': g += 1
		if seq[i+w-1] == 'T': t += 1
		
		# calc entropy, mask accordingly
		if shannon_entropy(a, c, g, t) < 1.4: 
			for j in range(i, i+w): seq_as_list[j] = 'N'

	# join masked list
	seq = ''.join(seq_as_list)
	return seq


print(dust(seq, w, threshold))	# run 


