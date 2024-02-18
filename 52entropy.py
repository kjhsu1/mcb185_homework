# 52entropy.py by Kenta Hsu

# in 51, we got data from the system directories and 
# files whilst staying in a python script 
# we can also get data directly from the CLI

# sys.argv is the complete list of words on the CLI 
import sys 
import math 

probs = []	# empty list 
for arg in sys.argv[1:]:
# sys.argv[1] == first CLI argument in 
# CLI == script name == 52entropy.py	
	f = float(arg)	# make arg a float
	assert(f > 0 and f < 1)
	probs.append(float(arg))

total = 0
for p in probs: total += p  # p is float from list probs
# if sum of all p doesn't equal 1 then sys.exit and report error 
if not math.isclose(total, 1.0):
	sys.exit('error: probs must sum to 1.0')	

h = 0
for p in probs:
	h -= p * math.log2(p)

print(h)