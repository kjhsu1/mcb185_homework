# test_dogma.py by Kenta Hsu

import dogma 

# testing out dogma library
print(dogma.transcribe('ACGT'))
print(dogma.revcomp('AAAACGT'))
# works 

# in professional setting people use units test and integration tests to see if library functions are working properly 

# translation 
# convert RNA seq to protein 
print(dogma.translate('ATGTAA'))	# should return M*


# sliding window algorithm 
# translate is a form of this 
'''
w = 10
s = 1 
for i in range(0, len(seq) -w +1, s):
	subseq = seq[i:i+w]
'''


# testing comp and skew functions
s = 'TGAACGTGGGGGGCATATGTATATATACCTAGATACCCGTAGTGTAAAAAAAAA'
print(dogma.gc_comp(s))
print(dogma.gc_skew(s))

# test translate 
print(dogma.translate(s))

# testing if else stacks
one = 2
two = 3
if one == 1: print(1)
else: print('not one')
if two == 2: print(2)
else: print('not two')

