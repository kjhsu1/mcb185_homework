# 72kmercount.py by Kenta Hsu

# count kmers 
import sys
import mcb185
import itertools

k = int(sys.argv[2])
kcount = {} # new dictionary 
# for each defline-seq pair...
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) -k +1):
		kmer = seq[i: i+k]
		if kmer not in kcount: kcount[kmer] = 0
		kcount[kmer] += 1
for kmer, n in kcount.items(): print(kmer, n)

# checking for the missing k-mer 
for nts in itertools.product('ACGT', repeat=2):
	kmer = ''.join(nts)
	if kmer in kcount: print(kmer, kcount[kmer])
	else:              print(kmer, 0)
