# 51cdslength.py by Kenta Hsu 

# program that reports length of protein coding gene in E.coli genome 

# e.coli genome is stored in a text filel 

# do a line by line reading loop through the file

# find all CDS regions 

import gzip

path = '/Users/kentahsu/Code/MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
with gzip.open(path, 'rt') as fp:
	for line in fp:
		# escape the current loop and move on to next iteration
		if line[0] == '#': continue 
		# turns string into list, split at any white space is default
		words = line.split()
		# also escape current loop if third column does not say CDS 
		if words[2] != 'CDS': continue
		# if it is CDS, get the beginning and end indices and turn them into ints 
		beg = int(words[3])
		end = int(words[4])		
		# print length which is just this formula 
		print(end - beg + 1)	

