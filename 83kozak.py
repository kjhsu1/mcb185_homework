# 83kozak.py by Kenta Hsu

# Genbank file: gbff.gz
# file contains all the genes/CDS regions in e.coli 
# for CDS contains start-stop coords 
# kozak seq is mostly in 5'UTR but ends with 'AUGG' 
# (includes start codon)

# Let's define kozak sequence as 5'-(gcc)gccRccAUGG-3'
# 13 nt long, extract sequence 9 bases before start codon

# first step: extract the 14 nt including ending with AUGG
# second step: Create PWM for aligned seq?
# third step: put them in TRANSFAC format?

# first step: read e.coli genbank flat file, 
# extract AC, ID, DE, 

# iterate through genbank flat file 
# store all CDS region coordinates in a list?

import sys 
import gzip
import mcb185 

# path to gbff 
path = sys.argv[1]


def store_cds(path):
	# store all cds tuples
	cds = [] # store

	# open gbff
	with gzip.open(path, 'rt') as file:
		# find CDS entires 
		# append start, end, strand in list as tuple 
		for line in file:
			# strip 
			line = line.rstrip()
			words = line.split()
			# if not cds, continue 
			if words[0] != 'CDS': continue
			# ignore the cds regions that start with 'join'
			if words[1].startswith('j'): continue 
			# also igonore cds regions that startwith 'complement(join'
			if words[1].startswith('complement(join'): continue

			# if on - strand 
			if words[1].startswith('complement'):
				strand = '-'
				coords = words[1][11:-1]
				#print(coords)
			# if on + strand
			else:
				strand = '+'
				coords = words[1]
				#print(coords)

			# get start and end coords
			numbers = coords.split('..')
			start = numbers[0]
			end = numbers[1]

			# append cds list with start, end, and strand
			# appending a tuple
			cds.append((start, end, strand))
	return cds

# cds list 
cds_list = store_cds(path)

# extract just the contig origin region, put into a string
def contig_origin(path): 
	with gzip.open(path, 'rt') as file:
		seq_as_list = []
		contig = False
		# extract sequences only from lines after 'ORIGIN'
		for line in file:
			words = line.split()
			
			# if first word is 'ORIGIN'
			if words[0] == 'ORIGIN':
				contig = True
				continue

			# if contig = True
			# add all the sequences parts into the seq_list
			if contig == True:
				for i, word in enumerate(words):
					if i > 0:
						seq_as_list.append(word)
		# after seq_list is complete, join into string 
		seq = ''.join(seq_as_list)
	# return 
	return seq

# pwm dict maker
def pwm_dict_maker(site_length):
	po = {}
	for i in range(1, site_length+1):
		po[i] = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
	return po


# kozak pwm
# set up pwm

def kozak_pwm(path):
	# cds list 
	cds_list = store_cds(path)
	# initialize kozak_pwm
	kozak_pwm = pwm_dict_maker(14)
	# get contig origin regions from gbff
	# get + and - strand
	seq = contig_origin(path)

	for cds in cds_list:
		# extract start and end coords
		start = int(cds[0])
		end = int(cds[1])

		# if strand is pos
		# extract kozak sequence part
		# 14 bases including the start 
		# make sure to adjust to 0-base index
			# -1 to go from 1based to 0based
		if cds[2] == '+':
			kozak = seq[start-9 -1:start+5 -1]
		
		# if strand is neg
		# coords are still relative to the + strand
			# this part was confusing
		# 1. slice for kozak frame on the + strand
		# 2. take revcomp of that, then reverse it
			# effectively just the complement
		elif cds[2] == '-':
			kozak = seq[end -1 -4:end -1 +10]
			kozak = mcb185.anti_seq(kozak)

		# add to pwm
		for i, nt in enumerate(kozak):
			# adjust i to dict key numbers
				# dict keys are 1based index
			# change nt to uppercase 
			i += 1
			nt = nt.upper()
			# add the pwm 
			kozak_pwm[i][nt] += 1
	return kozak_pwm

# call kozak pwm 
comp_kozak = kozak_pwm(path)

# format then print
print('AC E.coli')
print('XX')
print('ID E.coli Kozak Consensus')
print('DE')
# there's probably a better way to do this
a = 'A'
c = 'C'
g = 'G'
t = 'T'
po = 'PO'
print(f'{po:<8}{a:<8}{c:<8}{g:<8}{t:<8}')
for position in comp_kozak:
	a = comp_kozak[position]['A']
	c = comp_kozak[position]['C']
	g = comp_kozak[position]['G']
	t = comp_kozak[position]['T']
	print(f'{position:<8}{a:<8}{c:<8}{g:<8}{t:<8}')
print('XX')








