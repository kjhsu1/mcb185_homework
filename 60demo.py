# 60demo.py by Kenta Hsu

import sys 
import mcb185
import dogma

# each for loop retrieves one record(one protein seq with defline)
# retrieved as a tuple with two items, the defline and the seq
# this is done for each record meaning that as a whole it returns a 'tuple containing tuples for each record'
'''
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(defline[:30], seq[:40], len(seq))		
'''

'''

# calculate gc composition
for defline, seq in mcb185.read_fasta(sys.argv[1]):		# use FASTA reading function from mcb185 library
	defwords = defline.split()
	name = defwords[0]
	gc = 0
	for nt in seq:
		if nt == 'C' or nt == 'G': gc += 1
	print(name, gc/len(seq))
'''

# if elif else stack 

A = 0
C = 0
G = 0
T = 0
N = 0
for nt in seq:
	if		nt == 'A': A += 1
	elif 	nt == 'C': C += 1
	elif	nt == 'G': G += 1
	elif	nt == 'T': T += 1 
	else:			   N += 1
print(name, A/len(seq), C/len(seq), G/len(seq), T/len(seq), N/len(seq))

# samething as above but use list to store counter variables 
nts = 'ACGTN'
counts = []
for i in range(len(nts)): counts.append(0)
for nt in seq:
	if 		nt == 'A': counts[0] += 1
	elif	nt == 'C': counts[1] += 1
	elif	nt == 'G': counts[2] += 1
	elif	nt == 'T': counts[3] += 1
 	else:			 : counts[4] += 1
 print(name, end='\t')
 for n in counts: print(f'{n/len(seq):.4f}', end='\t')	# specify with exactly 4 decimal places

# list variation to hold counts of each nucleotide 
nts = 'ACGTN'
counts = []
for i in range(len(nts)): counts.append(0)	# create list that tracks count of all 5 types of nucleotides to expect
for nt in seq:
	if 		nt == 'A': counts[0] += 1 
	elif 	nt == 'C': counts[1] += 1 
	elif 	nt == 'G': counts[2] += 1
	elif	nt == 'T': counts[3] += 1
	else:			   counts[4] += 1
print(name, end='\t')
for n in counts: print(f'{n/len(seq):.4f}', end='\t') # print each item in list that stored counts divided by total amount of nucleotide 
print() 

# replace if-elif-else stack with str.find()
nts = 'ACGTN'
counts = [0] * len(nts)	# another way of creating a list with zeros in 5 indices
for nt in seq:
	idx = nts.find(nt)	# find which index the current nucleotide is in nts 
	counts[idx] += 1
print(name, end='\t')
for n in counts: print(f'{n/len(seq):.4f}', end='\t')
print()

# last variation of counting elements in a string using str.count
nts = 'ACGTN'	
print(name, end='\t')
for nt in nts:
	print(seq.counts(nt) / len(seq), end='\t')
print()







