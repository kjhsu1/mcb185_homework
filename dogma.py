# dogma.py by Kenta Hsu

# library for biology 

def transcribe(dna):		# converts DNA coding strand into mRNA 
	return dna.replace('T', 'U')


def revcomp(dna):		# returns reverse compliment sequence
	rc = []
	for nt in dna[::-1]:
		if 		nt == 'A': rc.append('T')
		elif 	nt == 'C': rc.append('G')
		elif	nt == 'G': rc.append('C')
		elif	nt == 'T': rc.append('A')
		else:			   rc,append('N')
	return ''.join(rc)


# translation function 
def translate(dna):
	aas = []	# amino acid sequence 
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if 		codon == 'ATA': aas.append('I')
		elif 	codon == 'ATC': aas.append('I')
		elif 	codon == 'ATT': aas.append('I')
		elif 	codon == 'ATG': aas.append('M')
		elif 	codon == 'ACA': aas.append('T')
		elif 	codon == 'ACC': aas.append('T')
		elif 	codon == 'ACG': aas.append('T')
		elif 	codon == 'ACT': aas.append('T')
		elif 	codon == 'AAC': aas.append('N')
		elif 	codon == 'AAT': aas.append('N')
		elif 	codon == 'AAA': aas.append('K')
		elif 	codon == 'AAG': aas.append('K')
		elif 	codon == 'AGC': aas.append('S')
		elif 	codon == 'AGT': aas.append('S')
		elif 	codon == 'AGA': aas.append('R')
		elif 	codon == 'AGG': aas.append('R')
		elif 	codon == 'CTA': aas.append('L')
		elif 	codon == 'CTC': aas.append('L')
		elif 	codon == 'CTG': aas.append('L')
		elif 	codon == 'CTT': aas.append('L')
		elif 	codon == 'CCA': aas.append('P')
		elif 	codon == 'CCC': aas.append('P')
		elif 	codon == 'CCG': aas.append('P')
		elif 	codon == 'CCT': aas.append('P')
		elif 	codon == 'CAC': aas.append('H')
		elif 	codon == 'CAT': aas.append('H')
		elif 	codon == 'CAA': aas.append('Q')
		elif 	codon == 'CAG': aas.append('Q')
		elif 	codon == 'CGA': aas.append('R')
		elif 	codon == 'CGC': aas.append('R')
		elif 	codon == 'CGG': aas.append('R')
		elif 	codon == 'CGT': aas.append('R')
		elif 	codon == 'GTA': aas.append('V')
		elif 	codon == 'GTC': aas.append('V')
		elif 	codon == 'GTG': aas.append('V')
		elif 	codon == 'GTT': aas.append('V')
		elif 	codon == 'GCA': aas.append('A')
		elif 	codon == 'GCC': aas.append('A')
		elif 	codon == 'GCG': aas.append('A')
		elif 	codon == 'GCT': aas.append('A')
		elif 	codon == 'GAC': aas.append('D')
		elif 	codon == 'GAT': aas.append('D')
		elif 	codon == 'GAA': aas.append('E')
		elif 	codon == 'GAG': aas.append('E')
		elif 	codon == 'GGA': aas.append('G')
		elif 	codon == 'GGC': aas.append('G')
		elif 	codon == 'GGG': aas.append('G')
		elif 	codon == 'GGT': aas.append('G')
		elif 	codon == 'TCA': aas.append('S')
		elif 	codon == 'TCC': aas.append('S')
		elif 	codon == 'TCG': aas.append('S')
		elif 	codon == 'TCT': aas.append('S')
		elif 	codon == 'TTC': aas.append('F')
		elif 	codon == 'TTT': aas.append('F')
		elif 	codon == 'TTA': aas.append('L')
		elif 	codon == 'TTG': aas.append('L')
		elif 	codon == 'TAC': aas.append('Y')
		elif 	codon == 'TAT': aas.append('Y')
		elif 	codon == 'TAA': 
			aas.append('*')
			return ''.join(aas)
		elif 	codon == 'TAG': 
			aas.append('*')
			return ''.join(aas)
		elif 	codon == 'TGC': aas.append('C')
		elif 	codon == 'TGT': aas.append('C')
		elif 	codon == 'TGA': 
			aas.append('*')
			return ''.join(aas)
		elif	codon == 'TGG': aas.append('W')
		else 				  : continue
	return ''.join(aas)

# gc composition of a sequence 
def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)

# gc skew 
def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)
	

# oligo nt temp

def oligo_meltingtemp(seq):
	# nt counts
	a = seq.count('A')
	c = seq.count('C')
	g = seq.count('G')
	t = seq.count('T')
	# seq length
	length = len(seq)
	# meat 
	if length <= 13:
		Tm = (a+t)*2 + (g+c)*4
		return Tm
	else:
		Tm = 64.9 + 41*(g+c - 16.4) / length
		return Tm



