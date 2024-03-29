# 84splicesites.py by Kenta Hsu

# use X.C.elegans.fa.gz
'''
- read gff file
- find all the introns
- first 6nt == splice donor 
- last 7nt == splice acceptor 
- create 2 dictionaries
	- one for splice acceptor 
	- one for splice donor 
- go through gff file linearly, for each 'intron'
+= 1 to appropriate bases for each position 
- at the end should have filled dictionary
'''

import sys 
import mcb185
import gzip
import json
import dogma

gff = sys.argv[1]
fa = sys.argv[2]


def po_dict_maker(site_length):
	po = {}
	for i in range(1, site_length+1):
		po[i] = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
	return po

def printer(org, a_or_d, pwm):
	print(f'AC {org}') # org = organism name 
	print('XX')
	print(f'ID {org}')
	print('XX')
	print(f'DE {a_or_d}')
	print(f'PO\tA\tC\tG\tT')
	# this goes through each key in acceptor dict
	for i, nt in enumerate(pwm.keys()): 
		i += 1
		a = pwm[nt]['A']
		c = pwm[nt]['C']
		g = pwm[nt]['G']
		t = pwm[nt]['T']
		print(f'{i}{a:>8}{c:>8}{g:>8}{t:>8}')
	print('XX')
	print('//')

def splice_site_pwm(gff, fa, org):
	introns = []
	with gzip.open(gff, 'rt') as fp:
		for line in fp:
			words = line.split()
			if words[1] != 'RNASeq_splice': continue
			chrom = words[0]
			start = int(words[3]) - 1
			end = int(words[4]) - 1
			n = words[5]
			strand = words[6]
			introns.append((chrom, start, end, n, strand))

	donor = po_dict_maker(6)
	acceptor = po_dict_maker(7)

	for defline, seq in mcb185.read_fasta(fa):
		defline_words = defline.split()
		for intron in introns:
			# if correct chromosome
			if defline_words[0] == intron[0]:
				# if intron is '+' strand
				if intron[4] == '+':
					intron_seq = seq[intron[1]:intron[2]+1]
				# intron has to be at least 60 nt long
				#if len(intron_seq) < 60: continue
				# if minus strand, do reverse comp 
				elif intron[4] == '-':
					intron_seq = mcb185.anti_seq(seq[intron[1]:intron[2]+1])
				# donor and acceptor seq
				d_seq = intron_seq[:6]
				a_seq = intron_seq[-7:]
				# donor 
				for i, nt in enumerate(d_seq):
					index = i + 1
					donor[index][nt] += 1
				# acceptor 
				for i, nt in enumerate(a_seq):
					index = i + 1
					acceptor[index][nt] += 1
	# print 
	printer(org, 'splice acceptor', acceptor)
	printer(org, 'splice donor', donor)


# run
splice_site_pwm(gff, fa, 'C.elegans')




