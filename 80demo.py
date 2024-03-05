# 80demo.py by Kenta Hsu 

import sys
import dogma 
import json

'''
# sys.argv is a list with a single element
print(sys.argv)
print()
print(sys.argv[0])

# access individual chars in an element of the sys.argv list 
print()
print(sys.argv[0][3]) # prints 'e' in '/Users'

# list of strings as 2D data structure 
# strings as first dimension, letters as the second 
# in general, putting containers in a list makes it multi-dimensional 

# string, tuple, list, and dictionary
d = ['hello', (3.14, 'pi'), [-1, 0, 1], {'years': 200, 'month': 7}]

# arrays vs lists 
# in python, not the same thing 
# array is also linear container, but all elements must be same type 

# matrices 
# rectangular, all elements have the same type  
# computationally arrays and matrices are much more efficient than lists

# a list of dictionaries 
# also called list of objects, list of structs, or list of records 

# records
# records basically mean dictionaries 
# more specifically data type that contain different named fields 

# catalog is a list of records, or list of dictionaries 
# each element in a list contain dictionaries 

# program converts csv files into list of records/catalogs
'''
'''
def read_catalog(filepath):
	catalog = []
	with open(filepath) as fp:
		for line in fp:
			if line.startswith('#'): continue
			name, length, seq, desc = line.rstrip().split(',')
			record = {
				'Name': name,
				'Length': length,
				'Sequence': seq,
				'Description': desc
			}
			catalog.append(record)
	return catalog
			
catalog = read_catalog('/Users/kentahsu/Code/MCB185/data/primers.csv')

# add melting temperature key value pair for each primer
for primer in catalog:
	primer['Tm'] = dogma.oligo_meltingtemp(primer['Sequence'])
print(catalog)

# dicts of lists 
# previous code 
# tracks kmer count but not locations
kcount = {}
for i in range(len(seq) -k +1):
	kmer = seq[i:i+k]
	if kmer not in kcount: kcount[kmer] = 0
	kcount[kmer] +=1 

# how to change this
seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGT'
k = 2 
kloc = {}
for i in range(len(seq) -k +1):
	kmer = seq[i:i+k]
	if kmer not in kloc: kloc[kmer] = [] # make list 
	kloc[kmer].append(i) # append list 
'''
# genbank file 
# files like these are hard to fit in 2 dimensional data
# have to make dictionary in dictionary in dictionary

# JSON
# check for json rules
truc = {
	'animals': {'dog': 'woof', 'cat': 'meow', 'pig': 'oink'},
	'numbers': [1.09, 2.72, 3.14],
	'is_complete': False,
}

print(json.dumps(truc, indent=4)) # fixes code into json

# regex 
# regex for amino acid 



































