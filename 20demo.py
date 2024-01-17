# 20demo.py by Kenta Hsu

import math

print('hello, again') # greeting
print(2.0e-6)
print(1 + 1)
print(10 ** 4)
print(math.factorial(3))
print(math.pi)

# pythagorean stuff

a = 3 							# side of triangle
b = 4 							# side of triangle
c = math.sqrt(a**2 + b**2)		# hypotenuse	
print(c)

# using sep argument for print() function

print(type(a), type(b), type(c), sep=', ')

def greeting():
	print('hello yourself')

def pythagoras(a, b):
	c = math.sqrt(a**2 + b**2)
	return c

x = pythagoras(3,4)
print(x)

# or 
print(pythagoras(a, b))

# assert 

#def pythagoras(a, b): 				# this section made as a comment because yields error
	#assert(a > 0)
	#assert(b > 0)
	#return math.sqrt(a**2 + b**2)

#print(pythagoras(-1, 1))

# or sys.exit()
#def pythagoras(a, b):				# this section made as a comment because yields error
	#if a <= 0: sys.exit('error: a must be greater than 0')
	#if a <= 0: sys.exit('error: a must be greater than 0')
	#return math.sqrt(a**2 b**2)

# practice 
# function for neg to pos numbers
def neg_to_pos(neg_number):
	pos_number = -(neg_number)
	return pos_number
print(neg_to_pos(-5))

# function for compute square volume
def square_volume(base, width, height):
	volume = base*width*height
	return volume
print(square_volume(2,2,2))

# function to compute circle area 
def circle_area(radius):
	area = (math.pi) * (radius**2)
	return area
print(circle_area(2))

# function to convert celsius to kelvins
def cel_to_kel(celsius):
	kelvins = celsius + 273.15
	return kelvins
print(cel_to_kel(50))

# function to convert betwen mph and kph)
def mph_to_kph(mph):
	kph = mph * 1.60934
	return kph 
print(mph_to_kph(60))

# function to convert OD260 to DNA conc.
def OD260_to_DNAconc(OD, A260, A320, dilution_factor):
	DNAconc = (A260 - A320)*dilution_factor*50
	return DNAconc
print(OD260_to_DNAconc(0.6,1,0.5,5))

# function compute distance between two cartesian points
def distance_two_points(ax,ay,bx,by):
	distance_x = abs(ax - bx)
	distance_y = abs(bx - by)
	distance = pythagoras(distance_x, distance_y)
	return distance 
print(distance_two_points(5,5,6,6))

# function that computes midpoint
def midpoint(x1, y1, x2, y2):
	midpoint_x = (x1 + x2) / 2
	midpoint_y = (y1 + y2) / 2
	return midpoint_x, midpoint_y
x, y = midpoint(-1, 3, 3, 4)
print(x, y, sep=', ')

# strings
s = 'hello world'
print(s, type(s))

# conditionals 
a = 2 
b = 2
if a == b:
	print('a equals b')
	print(a, b)

if a == b:
	print('a equals b')
print(a, b)

# boolean
c = a == b
print(c)
print(type(c))

# if elif else 
if a < b:
	print('a < b')
elif a > b:
	print('a > b')
else:
	print('a == b')

# if elif else but cleaner
if a < b: 	print('a < b')
elif a > b: print('a > b')
else: 		print('a == b')

# chaining 
if a < b or a > b: print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

# floating point warning 
a = 0.3 
b = 0.1 * 3
if a < b: 	print('a < b')
elif a > b: print('a > b')
else: 		print('a == b')

# check if close enough
print(abs(a - b)) 
if abs(a - b) < 1e-9: print('close enough')

# math.isclose
if math.isclose(a, b): print('close enough')

# string comparison if not False: print(True)
s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

# mismatched type error 
#a = 1
#s = 'G'
#if a < s: print('a < s')

# more practice 
# function that dtermines if number is integer 
def is_integer(number):
	print(type(number))
	if type(number) == int:	return True
	else:					return False
print(is_integer(5.0))

# function that determines if number is odd
def is_odd(number):
	if number%2 == 0:	return False
	else:				return True
print(is_odd(398))

# function that determines if valid probability
# basically if number is between 0 to 1
def is_valid_prob(prob):
	if prob >= 0 and prob <= 1:	return True
	else:						return False
print(is_valid_prob(0.99))

# function that returns molecular weight of DNA letter
# in units of g/mol: A = 329.21, T = 304.2, C = 289.18, G = 363.22
def molweight_dna(base):
	if base == 'A':		return 329.21
	elif base == 'T': 	return 304.20
	elif base == 'C':	return 289.18
	elif base == 'G':	return 363.22
print(molweight_dna('A'))

# function that returns the complement of DNA letter
def dna_comp(base):
	if base == 'A':		return 'T'
	elif base == 'T':	return 'A'
	elif base == 'G':	return 'C'
	elif base == 'C':	return 'G'
print(dna_comp('A'))















