# 50demo.py by Kenta Hsu

seq = 'GAATTC'

print(seq[-1])

# iterate 
for nt in seq: print(nt, end='')
print()

# iterate using range 
for i in range(len(seq)):
	print(i, seq[i])	# let's you see the indices of each character in string

# slices 
s = 'ABCDEFGHIJ'
print(s[0:5])	# slices indices 0 to 4, excludes last indices

# slices with steps
print(s[0:8:2])		# 0, 2, 4, 6, not including 8

# from beginning to the index, from index to end 
print(s[:5])
print(s[5:])

# new syntax 
print(s[::])	# beginning to end, intervals not specified so by 1s
print(s[::1])	# beginning to end, intervals of 1
print(s[::2])	# beginning to end, intervals of 1
print(s[::-2])	# negative intervals means start at end at the specified interval

# tuples 
tax = ('Homo', 'sapiens', 9606)		# constructs tuple 
print(tax)							# note the parentheses in the output 

# tuples and strings are immutable, can't change content once set 

'''
s[0] = ''	# s is a string that is defined already, can't change content
tax[0] = 'human'	# same thing for tuples
'''

# strings and tuples can be sliced though
print(tax[::-1])	# prints tuple with order flipped 

# a function that returns two values technically returns a tuple with indices 0 and 1
# quadratic formula is a good example 
def quadratic(a, b, c):
	x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
	x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
	return x1, x2

# unpack tuples that are returned 
x1, x2 = quadratic(5, 6, 1)		# unpacked tuple 
print(x1, x2)
intercepts = quadratic(5, 6, 1)	# packed tuple 
print(intercepts[0], intercepts[1])	

# enumerate and zip 
nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])		# prints the item's index as well as the value 

# enumerate 
for i, nt in enumerate(nts):	# during each loop, value of nt = nts[i]
	print(i, nt)

# zip 
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])		# prints out indices of two tuples at once 

for nt, name in zip(nts, names):	# tuples nts and names both have to be the same length
	print(nt, name) 		# same as enumerate, for each loop nt = nts[i] and name = names[i]
print()
# enumerate zip 
for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)
print()
# lists are mutable
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

# append list
nts.append('C')
print(nts)

# methods
# methods are functions that only work with certain data types. ex. nts.append('C')

# pop 
last = nts.pop()	# declaring variable removes last element in nts, also stores removed element in last
print(last)
print(nts)
print()

# .sort
# all elements must have similar types (except floats and ints)
nts.sort()
print(nts)

nts.sort(reverse=True)	# sort in reverse alphabetical order
print(nts)

# making alias to exisiting list
# you are pointing at the same list object
# modifications made to one will reflect in the other as well 
nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

# making a copy of existing list 
# creates shallow copies?
print()
copy = nts.copy()
copy.sort(reverse=True)
print(copy, nts)

# more on lists
items = list() 	# creates empty list
print(items)
items.append('eggs')
print(items)

# another way to create empty lists
stuff = []
stuff.append(3)
print(stuff)

# turning other iterables into lists
alph = 'ABCDEFGHIJ'
print(alph)
aas = list(alph)
print(aas)

# split and join
print() 
text = 'good day	to you'
words = text.split()	# everything excluding spaces are stored in a list
print(words)

# specifying delimiters ie. where to split
line = '1.41, 2.72, 3.14'
print(line.split(','))

# list to strings 
s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

# searching in containers (not limited to lists)

# in 
if 'A' in alph: print('yay')
if 'a' in alph: print('no')

# index()
print('index G?', alph.index('G'))
# print('index Z?', alph.index('Z'))	# error because 'Z' doesn't exist in list

# find()
# find() only works for strings
print('find G?', alph.find('G')) # returns index of the first element or -1 if not found

# work around for tuples and lists, use if thing in list first to avoid error 


# Practice Problems 

# function that returns minimum value of a list 
def min(num_list):
	num_list.sort()		# sorted from min to max
	return num_list[0]
# testing
number_list = [4, 5, 6, 1]
print(min(number_list))		# should print 1 

# function that returns both min and max 
def min_and_max(num_list):
	# initialize 
	min = 0
	max = 0

	# first the min
	num_list.sort()		# min to max
	min = num_list[0]

	# then the max 
	num_list.sort(reverse=True)
	max = num_list[0]

	# return min and max 
	return min, max  
# test 
number_list = [4, 5, 6, 1]
print(min_and_max(number_list))	# prints tuple 
# or store in two variables 
min, max = min_and_max(number_list)
print(min, max)

# function that returns mean of values in list 
def mean(list):
	# initialize
	sum = 0 
	# iterate through the list 
	for num in list:
		sum += num
	# return mean 
	return sum / len(list)
# testing 
print()
number_list = [1, 2, 3, 4]
print(mean(number_list))

# function that computes entropy of a probability distribution 
# we can do a shannon's entropy calculation
# assume the list contains probability distribution 
import math

def shannon_entropy(list):
	# intializing 
	sum = 0
	# calculate inside the sigma
	for prob in list:
		sum += prob * math.log(prob, 2)
	# return entropy value 
	return -sum
# testing 
prob_dist_list = [0.4, 0.3, 0.2, 0.1]
print()
print(shannon_entropy(prob_dist_list))

# function that computes kullback-leibler distance between two sets of prob distributions 
# basically compares one prob distribuition to an expected second prob distribution
# and puts a value on how rare the first distribution is comparatively 

def kullback_leibler(p_list, q_list):		# q is the expeceted distribution 
	# initialize
	sum = 0

	# iterate, they should both have same length 
	for p_prob, q_prob in zip(p_list, q_list):
		sum += p_prob * math.log2(p_prob / q_prob)

	# return value
	return sum

# testing
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = [0.1, 0.3, 0.4, 0.2] 
print()
print(kullback_leibler(p1, p2))


# files 
# not like strings, tuples, and lists 
# files must be 'opened' to be accessed, and closed 

# read file line by line 
'''
with open(path) as fp:
	for line in fp:
		do_something_with(line)
'''

# open() creates variable type called 'file pointer' 
# open() takes either relative or absoulte path to file
# with automatically closes after everything

# alternate way, not recommended 
''' 
fp = open(path)
for line in fp:
	do_something_with(line)
fp.close()
'''

# compressed files 
# same treatment as normal files except 
# first import gzip 
# change open(path) to gzip.open(path, 'rt')
'''
import gzip 
with gzip.open(path, 'rt') as fp:	# reports content to stdout, same as gunzip -c path
	for line in fp:
		print(lien, end='')
'''
# converting types 
# text files contain only strings 
# meaning, when you want to do math, use int() and float() to convert first

test_list = ['bob']
counter = 0
for thing in test_list:
	if 'bob' == thing: counter += 0

print(counter)


