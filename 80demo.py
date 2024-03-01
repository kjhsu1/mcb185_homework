# 80demo.py by Kenta Hsu 

import sys 

# sys.argv is a list with a single element
print(sys.argv)
print()
print(sys.argv[0])

# access individual chars in an element of the sys.argv list 
print()
print(sys.argv[0][3]) # prints 'e' in '/Users'

# list of strings as 2D data structure 
# strings as first dimension, letters as the second 
# in general, putting containers in a list makes it multi-dimensional 

# string, tuple, list, and dictionary
d = ['hello', (3.14, 'pi'), [-1, 0, 1], {'years': 200, 'month': 7}]

# arrays vs lists 
# in python, not the same thing 
# array is also linear container, but all elements must be same type 

# matrices 
# rectangular, all elements have the same type  
# computationally arrays and matrices are much more efficient than lists

# a list of dictionaries 
# also called list of objects, list of structs, or list of records 

# records
# records basically mean dictionaries 
# more specifically data type that contain different named fields 

# catalog is a list of records, or list of dictionaries 
# each element in a list contain dictionaries 

# program converts csv files into list of records/catalogs












