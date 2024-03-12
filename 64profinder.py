# 64profinder.py by Kenta Hsu and Natalia Marin

# input multi-FASTA file of DNA 
# output multi-FASTA file of proteins (in all 6 reading frames)
# this means return 6 fasta AA seq per 1 fasta DNA seq

import dogma 
import sys 
import mcb185

# better way to do it 
# first translate the whole frame without stopping at stop codon
path = sys.argv[1]
min_len = int(sys.argv[2])
seq_list = []
# feed frame appropriate seq -> append valid seqs to seq_list
def append_valid_aaseq(seq, min_len): 
	aa_seq = dogma.translate(seq)
	aa_seq_list = aa_seq.split('*')
	for cds in aa_seq_list:
		new_cds = cds[cds.find('M'):]
		if len(new_cds) > min_len:
			seq_list.append(new_cds)

for defline, seq in mcb185.read_fasta(path):
	# before doing new FASTA seq, clear out seq_list
	seq_list = [] 
	for i in range(3):
		frame_seq = seq[i:]
		rev_comp_seq = dogma.revcomp(seq)[i:]
		append_valid_aaseq(frame_seq, min_len)
		append_valid_aaseq(rev_comp_seq, min_len)
	# print 
	for i, items in enumerate(seq_list):
		print(f'{defline}-prot-{i}')
		print(items)




