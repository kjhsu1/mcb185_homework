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

















