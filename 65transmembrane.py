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

import sys 
import mcb185

path = sys.argv[1]

deflines = []
seqs = []
# append deflines, seqs
for defline, seq in mcb185.read_fasta(path):						
	deflines.append(defline)
	seqs.append(seq)


def proline_check(seq):	# takes seq as string, returns True or False
	if seq.find('P') == -1: return False
	else: return True

def kd_hydrophobicity(amino_acid):
	if amino_acid == 'A':   return 1.8
	elif amino_acid == 'C': return 2.5
	elif amino_acid == 'D': return -3.5
	elif amino_acid == 'E': return -3.5
	elif amino_acid == 'F': return 2.8
	elif amino_acid == 'G': return -0.4
	elif amino_acid == 'H': return -3.2
	elif amino_acid == 'I': return 4.5
	elif amino_acid == 'K': return -3.9
	elif amino_acid == 'L': return 3.8
	elif amino_acid == 'M': return 1.9
	elif amino_acid == 'N': return -3.5
	elif amino_acid == 'P': return -1.6
	elif amino_acid == 'Q': return -3.5
	elif amino_acid == 'R': return -4.5
	elif amino_acid == 'S': return -0.8
	elif amino_acid == 'T': return -0.7
	elif amino_acid == 'V': return 4.2
	elif amino_acid == 'W': return -0.9
	elif amino_acid == 'Y': return -1.3
	elif amino_acid == 'U': return 2.5
	else: sys.exit('Feed a valid amino acid')

def has_signal_pep_check_pass(seq): # feed first 30 aa seq
	# accounts for no proline rule
	# sliding window, w = 8
	w = 8
	for i in range(len(seq) -w +1):	
		kd_sum = 0
		current_window = seq[i:i+w] 
		for aa in current_window: 
			kd_sum += kd_hydrophobicity(aa)
		# average
		average_kd = kd_sum / w
		if average_kd >= 2.5 and proline_check(current_window) == False:
			return True
	# return False if no hydrophobic seq
	return False       

def has_transmembrane_region(seq): # feed seq after first 30 aa
	# another sliding window 
	w = 11 
	for i in range(len(seq) -w +1):	
		kd_sum = 0
		current_window = seq[i:i+w] 
		for aa in current_window: 
			kd_sum += kd_hydrophobicity(aa)
		# average
		average_kd = kd_sum / w
		if average_kd >= 2.0 and proline_check(current_window) == False:
			return True
	# return False if no transmembrane seq
	return False

def is_transmembrane_protein(seq):	# feed entire aa seq
	first30 = seq[:30]	# char 0-29
	after30 = seq[30:]	# char 30-end
	# test
	req1 = has_signal_pep_check_pass(first30)
	req2 = has_transmembrane_region(after30)
	if req1 == True and req2 == True: return True
	# if not
	return False

def transmembrane(deflines, seqs):
	transmembrane_prot_list = []
	# check if transmembrane protein, append defline if yes
	for defline, seq in zip(deflines, seqs):
		if len(seq) < 41: continue
		if is_transmembrane_protein(seq) == True:
			transmembrane_prot_list.append(defline)
	
	# return a nice string 
	transmembrane_prot_string = '\n'.join(transmembrane_prot_list)
	return transmembrane_prot_string

# run
print(transmembrane(deflines, seqs))
'''
for defline, seq in zip(deflines, seqs):
	if is_transmembrane_protein(seq) == True:
		print(defline)
'''
