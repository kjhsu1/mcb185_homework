# 61skewer.py by Kenta Hsu

import dogma
import mcb185
import sys

def fasta_to_lists(path):	# returns two lists with defline and seq
	# store defline and sequence in a list 
	# not working with multiple records for this problem
	defline_list = []
	seq_list = []
	
	# append above lists using fasta reader in mcb185 library 
	for defline, seq in mcb185.read_fasta(path):						
		defline_list.append(defline)
		seq_list.append(seq)
	# both lists should now contain deflines and seqs 

	# return 
	return defline_list, seq_list 
defline_list, seq_list = fasta_to_lists(sys.argv[1])

seq = seq_list[0]
w = 1000
for i in range(len(seq) -w +1):
	s = seq[i:i+w]
	print(i, dogma.gc_comp(s), dogma.gc_skew(s))	# calculates gc comp and gc skew for each 10 nucleotide window


