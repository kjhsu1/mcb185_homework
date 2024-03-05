# 81prosite.py by Kenta Hsu
import mcb185
import re # regular expressions
# step through e.coli protein
# PROSITE/regex 
# D-K-T-G-T, print all matches 

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if 'DKTGT' in seq: print(defline)

# same thing as above using regex library function
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if re.search('DKTGT', seq): print(defline)

# DKTGT is PROSITE pattern for ATPases phosphorylation site 
# full pattern is "D-K-T-G-T-[LIVM]-[TI]"
# hard to use pythonic way 'in' keyword b/c fuzzy pattern 
# use regex library

for deflne, seq in mcb185.read_fasta(sys.argv[1]):
	if re.search('DKTGT[LIVM][TI]', seq): print(defline)

# more complex matching 
# C-x(2,4)-C-x(3)-[LIVMFYWC]-x(8)-H-x(3,5)-H
# zinc-finger proteins
# x(2,4) means 2-4 of any aa 
# difference between regex and PROSTE syntax 
# () rather than {}
# . rather than x 

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if re.search('C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H', seq):
		print(defline)

# regex can also extract the text 
pat = 'C.{2,4}C.{3}[LIVMFYWC].{8}H.{3,5}H'
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	m = re.search(pat, seq) # either None, or match object
	if m: print(m.group(1))









