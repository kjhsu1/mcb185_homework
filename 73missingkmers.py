# 73missingkmers.py by Kenta Hsu

import sys
import gzip
import mcb185
import itertools

# searches sequences for the smallest missing k-mer

# start at k=1 and increase until there are missing k-mers 
# just report k-mers that are missing 
# can stop after finding value with missing k-mer
# search both watson and crick strands 

# use e.coli.fna.gz

# function that takes arguments: string seq, and k
# function finds all unique kmers in a seq 
def single_seq_kmer_finder(seq, k):
	# make dict w/all kmers found
	kmers = {}
	for i in range(len(seq) -k +1):
		kmer = seq[i:i+k]
		# default is checking the key
		if kmer not in kmers: kmers[kmer] = 0
		kmers[kmer] += 1
	# kmers should have all kmers stored
	return kmers

# function that compares # of kmers found vs. # possible kmers
def missing_kmer_checker(kmers_dict, k):
	# find all possible kmers
	possible_kmers = 4**k

	# kmers actually found
	found_kmers = len(list(kmers_dict.keys()))

	# check if # found kmers match with # possible kmer
	if possible_kmers == found_kmers: return False
	else: return True 

# function that checks kmers, increasing k by 1 each time
# takes in seq
def check_kmer_until_missing(seq):
	# list that stores all missing kmers
	missing_kmer_list = []
	# counter to track when to stop loop
	missing = False
	# check is kmer missing until missing 
	k = 1
	while missing == False:
		kmer_dict = single_seq_kmer_finder(seq, k)
		missing = missing_kmer_checker(kmer_dict, k)
		# if missing report which k-mers are missing
		# need to use itertools
		# itertools.product() generates tuples with all 
		# possible kmers of particular
		if missing == True:
			# iterate through all possible kmers
			for nts in itertools.product('ACGT', repeat=k):
				# join tuple to get string kmer
				kmer = ''.join(nts)
				if kmer not in kmer_dict.keys():
					missing_kmer_list.append(kmer)
		k += 1
	# return all missing k-mer
	return missing_kmer_list

# function that checks for missing kmers in all sequences in FASTA file
# checks both original strand and reverse comp strand
def kmer_checker(path):
	# for each seq in FASTA file 
	with gzip.open(path, 'rt') as file:
		for defline, seq in mcb185.read_fasta(path):
			# print missing kmer for every seq in file
			# for original strnad
			print(f'{defline}:\n{check_kmer_until_missing(seq)}')
			# for compliment strand
			rev_comp = mcb185.anti_seq(seq)
			print(f"rev comp of {defline} are:\n{check_kmer_until_missing(rev_comp)}")

# run 
path = sys.argv[1]
kmer_checker(path)


'''
seq = 'ATACAGAAATATTTGTCGAGTGGGCCACTCGCCCT'
kmerss = single_seq_kmer_finder(seq, 2)
print(missing_kmer_checker(kmerss, 2))
'''

