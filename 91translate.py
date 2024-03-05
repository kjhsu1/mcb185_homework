#!/usr/bin/env python3
# 91translate.py by Kenta Hsu
# this one is DONE

import argparse
import dogma
import mcb185

# make executable program that translates transcripts 
# transcripts are stored as coding strand DNA (starts w/ATG)
# use C.elegans transcripts 

# CLI argument parser to set up --help

parser = argparse.ArgumentParser(description='DNA translater.')
# if no dashed lines in front, means its positional argument
# if yes dashed line in front, means its conditioanl argument
parser.add_argument('file', type=str, help='fasta file of mRNAs')
parser.add_argument('-a', '--anti', action='store_true', 
	help='also examine the anti-parallel strand')
parser.add_argument('-m', '--m', '-MIN', type=int,
	default=100, help='minimum protein length [%(default).3f]')
arg = parser.parse_args()
print('translating with:', arg.file, arg.m, arg.anti)

# Harvest CLI arguments 
path = arg.file 
min_len = arg.m
anti = arg.anti

# meat of program 

for defline, seq in mcb185.read_fasta(path):
	# first find first 'ATG'
	start_index = seq.find('ATG')
	seq = seq[start_index:]
	aa = dogma.translate(seq)
	
	# if aa seq less than min, skip
	if len(aa) < min_len:
		continue
	
	# else
	print(defline)
	print(aa)
	
	# if anti is true and len(anti_aa) >= 300
	anti_seq = dogma.revcomp(seq)
	start_index = anti_seq.find('ATG')
	anti_aa = dogma.translate(anti_seq[start_index:])
	if anti == True and len(anti_aa) >= 300:
		print(f'Anti of: {defline}')
		print(anti_aa)





