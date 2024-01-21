# 43randomdna.py by Kenta Hsu
import random
# generate DNA sequences in FASTA format
# variable for how many sequences
# seq with length from 50-60

def randomdna(n):
	base = 'ATGC'
	for i in range(1, n+1):
		print(f'>seq-{i}')
		for i in range(random.randint(50, 60)):
			print(random.choice(base), end='')
		print('')

randomdna(10)
