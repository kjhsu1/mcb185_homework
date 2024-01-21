# 40demo.py by Kenta Hsu

import random

for i in range(5):
	print(random.random())

for i in range(50):
	print(random.choice('ACGT'), end='')

for i in range(50):
	r = random.random()
	if r < 0.7: print(random.choice('AT'), end='')
	else:		print(random.choice('CG'), end='')

# f-strings
i = 1 
pi = 3.14159
print('\n\n')
print('normal string {i} {pi}')
print(f'formatted string {i} {pi}')
print(f'tau {pi + pi}')

# rounding format inside curly bracket
print(f'formatted string {i} {pi:.3f}')

# sys.stderr
# basically everything else in this file is stdout
# but the string 'logging' is stderror 
import sys 
print('logging', file=sys.stderr)

# call to random seed will repeat random.random output
random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())

