# 51cdslength.py by Kenta Hsu 

# program that reports length of protein coding gene in E.coli genome 

# e.coli genome is stored in a text filel 

# do a line by line reading loop through the file

# find all CDS regions 

import gzip

path = '~/MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue 	# escape the current loop and move on to next iteration
		words = line.split()	# turns string into list, split at any white space is default 
		if words[2] != 'CDS': continue	# also escape current loop if third column does not say CDS
		beg = int(words[3])		# if it is CDS, get the beginning and end indices and turn them into ints 
		end = int(words[4])		
		print(end - beg + 1)	# print length which is just this formula 

