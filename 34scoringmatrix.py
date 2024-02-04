# 34scoringmatrix.py by Kenta Hsu and Natalia Marin

# iterate through the string container
# set alphabet = " A C G T"
# first row you can just print(alphabet)
# from second row on, iterate through string alphabet

def scoringmatrix():
	nts = 'ACGT'
	print(' ', end='')
	for nt in nts:
		print('  ', end='')
		print(nt, end='')
	print()
	for nt in nts:
		print(nt, end=' ')
		for nt2 in nts:
			if nt == nt2:
				print('+1', end=' ')
			else:
				print('-1', end=' ')
		print()

scoringmatrix()


