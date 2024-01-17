# 31fizzbuzz.py by Kenta Hsu

# loop through 1 to 100, print
# if number divisible by 3 print 'Fizz' instead 
# if number divisible by 5 print 'Buzz' instead
# if both 'FizzBuzz'

# order of if, elif statement matters
# you have to make sure to detect fizzbuzz first
for i in range(1,101):
	if i % 3 == 0 and i % 5 == 0:
		print('FizzBuzz')
	elif i % 5 == 0:
		print('Buzz')
	elif i % 3 == 0:
		print('Fizz')
	else:
		print(i)