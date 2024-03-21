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
def translate_transcript(anti, path, min_len):
	for defline, seq in mcb185.read_fasta(path):
		# first find first 'ATG'

		# for the forward strand
		start_index = seq.find('ATG')
		seq = seq[start_index:]
		aa = dogma.translate(seq)
		# need to slice at the first '*'
		aa = aa[:aa.find('*')+1]

		# for the anti if anti == True
		anti_aa = ''
		if anti == True:
			anti_start_index = mcb185.anti_seq(seq).find('ATG')
			anti_seq = mcb185.anti_seq(seq)[anti_start_index:]
			anti_aa = dogma.translate(anti_seq)
			anti_aa = anti_aa[:anti_aa.find('*')+1]
		
		# if aa seq >= than min, print
		if len(aa) >= min_len:
			print(f'>{defline}')
			print(aa)

		# if anti_aa seq >= than min, print
		if len(anti_aa) >= min_len:
			print(f'>anti of {defline}')
			print(anti_aa)
# call
translate_transcript(anti, path, min_len)




