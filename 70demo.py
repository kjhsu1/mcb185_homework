# 70demo.py by Kenta Hsu 

# empty dictionary 
d = {}
d = dict()

# dictionary 
d = {'dog': 'woof', 'cat': 'meow'}
print(d)

# print
print(d['cat'])

# add new key value pair 
d['pig'] = 'oink'
print(d)

# delete item 
del d['cat']
print(d)

# get error if you try to access a nonexistant key 

# using 'in' keyword 
# use to refer to key

if 'dog' in d: print(d['dog'])

# normal 'in' iteration
for key in d: print(f'{key} says {d[key]}')

# most common way to iterate 
# kinda like enumerate, can keep track of index and key of dict
print()
for k, v in d.items(): print(k, 'says', v)


# get just the keys 
print()
print(d.keys())

# get just the values 
print()
print(d.values())

# store the values in the list 
# casting to a list 
print(list(d.values()))

# counting nucleotides with dictionary 
seq = 'ATGA'
count = {}
for nt in seq:
	if nt not in count: count[nt] = 0
	count[nt] += 1

# sorting dictionaries 
# this sorts the keys
# sorted(count), imagine this as list of keys but sorted
for k in sorted(count): print(k, count[k])

# sorting dictionaries by values 
# sorted() takes a list as argument 
# dictionary.item() outputs kinda like two parallel...
# key-value pair lists
'''
sorted() can also take 2 arguments
the dictionary and either the key or value specification
lambda functions are the specifier 
'''
for k, v in sorted(count.items(), key=lambda item: items[1]):
		print(k, v)

# K-mers 
# k-mers refer to the individual window in a 
# sliding window algorithm 

























