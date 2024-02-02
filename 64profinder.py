# 64profinder.py by Kenta Hsu

'''
NOTE: IN THE CURRENT VERSION THE AA seq stops at the first stop codon
- Meaning that when you run the ecoli genome with min length == 100,
all 6 frames will be 'too short'
- Not sure if I'm supposed to do that or something else, may have to fix 
'''

# input multi-FASTA file of DNA 
# output multi-FASTA file of proteins (in all 6 reading frames)
# this means return 6 fasta AA seq per 1 fasta DNA seq

import dogma 
import sys 
import mcb185

# from CLI argument 
path = sys.argv[1]
min_pro_length = sys.argv[2]

def fasta_to_lists(path): # returns two lists with defline and seq
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

def profinder(path, min_pro_length):
	# cast min protein len to int 
	min_pro_length = int(min_pro_length)
	# get all deflines and seq 
	deflines, seqs = fasta_to_lists(path)
	# new lists for deflines and AA seqs
	aa_deflines = []
	aa_seqs = []
	# append lists, go through 6 frames
	for defline, sequence in zip(deflines, seqs):
		seq = sequence
		# read all 6 frames 
		# +1, +2, +3 
		pos1 = dogma.translate(seq)
		pos2 = dogma.translate(seq[1:])
		pos3 = dogma.translate(seq[2:])
		
		# -1, -2, -3 
		rev_comp_seq = dogma.revcomp(seq) 
		min1 = dogma.translate(rev_comp_seq)
		min2 = dogma.translate(rev_comp_seq[1:])
		min3 = dogma.translate(rev_comp_seq[2:])
		
		# append aa seqs (6 total)
		if len(pos1) > min_pro_length: aa_seqs.append(pos1)
		else: aa_seqs.append(f'AA seq less than {min_pro_length}')
		if len(pos2) > min_pro_length: aa_seqs.append(pos2)
		else: aa_seqs.append(f'AA seq less than {min_pro_length}')
		if len(pos3) > min_pro_length: aa_seqs.append(pos3)
		else: aa_seqs.append(f'AA seq less than {min_pro_length}')
		if len(min1) > min_pro_length: aa_seqs.append(min1)
		else: aa_seqs.append(f'AA seq less than {min_pro_length}')
		if len(min2) > min_pro_length: aa_seqs.append(min2)
		else: aa_seqs.append(f'AA seq less than {min_pro_length}')
		if len(min3) > min_pro_length: aa_seqs.append(min3)
		else: aa_seqs.append(f'AA seq less than {min_pro_length}')
		
		# append aa deflines (6 total) (labled 0~5)
		for i in range(6):
			aa_deflines.append(f'{defline[:11]}-prot-{i}')
	# return fully appended defline and seq lists
	return aa_deflines, aa_seqs

# run
aa_deflines, aa_sequences = profinder(path, min_pro_length)
# put back into FASTA format 
aa_fasta = []
aa_fasta_string = []
for defline, seq in zip(aa_deflines, aa_sequences):
	aa_fasta.append(f'>{defline}')
	aa_fasta.append(seq)
aa_fasta_string = '\n'.join(aa_fasta)
# print
print(aa_fasta_string)











