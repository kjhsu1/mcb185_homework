# 32fibonacci.py by Kenta Hsu

# function that takes n as argument
# return up to the nth fibonacci sequence number

# add two previous fibonacci sequence to get current number 

def fibonacci(n):
	fib1 = 0
	fib2 = 1
	print(fib1)
	print(fib2)
	for i in range(n-2):
		fib3 = fib1 + fib2
		print(fib3)
		fib1 = fib2
		fib2 = fib3

fibonacci(11)
