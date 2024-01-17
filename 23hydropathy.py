# 23hydropathy.py by Kenta Hsu

# KD hydrophobicity value for amino acid letter 
def KD_hydrophobicity(amino_acid):
	if amino_acid == 'A': 	return 1.8
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

# Alanine 
print(KD_hydrophobicity('A'))

# Histidine 
print(KD_hydrophobicity('H'))

# Serine 
print(KD_hydrophobicity('S'))



