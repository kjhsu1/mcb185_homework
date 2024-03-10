# 65transmembrane.py by Kenta Hsu

# program predicts which proteins in proteome are transmembrane 

'''
transmembrane proteins have 
- hydrophobic peptide near N-terminus
- other hydrophobic regions all throughout
'''

# use kyte-dolittle hydrophobicity 
# use .faa.gz (fasta format amino acids)
# soft link is e.coli.faa.gz in mcb185_homework

# YOU CAN ABSTRACT THE WINDOW ALGORITHM 

import sys 
import mcb185
import dogma

path = sys.argv[1]

# sliding window function 
def sliding_window(seq, w, kd_min):
	for i in range(len(seq) -w +1):	
		kd_sum = 0
		current_window = seq[i:i+w] 
		for aa in current_window: 
			kd_sum += dogma.kd_hydrophobicity(aa)
		# average
		average_kd = kd_sum / w
		if average_kd >= kd_min and current_window.find('P') == -1:
			return True
	# return False if no transmembrane seq
	return False

def is_transmembrane_protein(seq):	# feed entire aa seq
	first30 = seq[:30]	# char 0-29
	after30 = seq[30:]	# char 30-end
	# test
	req1 = sliding_window(first30, 8, 2.5)
	req2 = sliding_window(after30, 11, 2.0)
	if req1 == True and req2 == True: return True
	# if not
	return False

def transmembrane(path):
	transmembrane_prot_list = []
	# check if transmembrane protein, append defline if yes
	for defline, seq in mcb185.read_fasta(path):
		if len(seq) < 41: continue
		if is_transmembrane_protein(seq) == True:
			transmembrane_prot_list.append(defline)
	
	# return a nice string 
	transmembrane_prot_string = '\n'.join(transmembrane_prot_list)
	return transmembrane_prot_string

# run
print(transmembrane(path))

