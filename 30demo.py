# demo30.py by Kenta Hsu 

import math

# while loop
# while True:
	#print('hello')

# break 
i = 0
while True:
	i = i + 1 
	print('hey', i)
	if i == 3: break

# condition to stop loop
i = 0
while i < 3:
	print(i)
	i = i + 1
print('final value of i is', i)

# for loop
for i in range(1, 10, 3):
	print(i)

# for loops for items in a container
for char in 'hello':
	print(char)

# for loop through 4x4 matrix: inner loop starts at 0
for  i in range(4):
	for j in range(4):
		print(i+1, j+1)

# half matrix including the major diagonal for a 4x4: inner loop starts at i
for  i in range(4):
	for j in range(i, 4):
		print(i+1, j+1)

# half matrix excluding the major diagonal for a 4x4
for  i in range(4):
	for j in range(i+1, 4):
		print(i+1, j+1)

# Practice problems 

# function calculating triangular number, sum of number from 1 to n 
def triangular_number(n):
	sum = 0					# initialize 
	for i in range(1,n+1):	# iterates from 1 to n 
		sum = sum + i
	return sum

print(triangular_number(4))

# function that calculates factorials
def factorials(n):
	product = 1
	if n != 0:
		for i in range(2,n+1):
			product = product * i
		return product
	else:
		return 1

print(factorials(4))
print(factorials(0))	# factorial of 0 is 1 

# function that estimates Euler's number 
def euler(n):
	euler = 0
	for i in range(0,n+1):	# iterates through 0 to n
		euler = euler + (1 / factorials(i))
	return euler

print(euler(1000))	# close enough

# function that checks if number is perfect square 
def perfect_square(number):
	square_root = math.sqrt(number)
	if square_root == square_root // 1:
		return True
	else:
		return False
	
print(perfect_square(16))

# function that checks if number is prime
# prime numbers are numbers that are only divisible by 1 and the number
# make a function that takes n as argument, and iterate from 1 to n
# every iteration mod n by i 
# if at the end of iteration, the only mod that yielded a 0 is 1 and n, then number is prime

def prime_number(n):
	counter = 0 		# if counter is 2 at the end, number is prime
	for i in range(1,n+1):
		if n % i == 0:
			counter = counter + 1
	if counter == 2:
		return True 
	else: 
		return False

print(prime_number(17)) 

def triples(n):
	for i in range(1, n - 1):
		for j in range(i,n - 1):
			print(i, j)

triples(100)




