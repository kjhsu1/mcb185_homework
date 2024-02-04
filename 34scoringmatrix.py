# 34scoringmatrix.py by Kenta Hsu

# iterate through the string container
# set alphabet = " A C G T"
# first row you can just print(alphabet)
# from second row on, iterate through string alphabet

def scoringmatrix():
	alphabet = "   A  C  G  T"
	print(alphabet)
	for char in alphabet:
		if char == 'A':
			print('A +1 -1 -1 -1')
		elif char == 'C':
			print('C -1 +1 -1 -1')
		elif char == 'G':
			print('G -1 -1 +1 -1')
		elif char == 'T':
			print('T -1 -1 -1 +1')
		else: continue
scoringmatrix()