# 45dndstats.py by Kenta Hsu
import random
# determine averages for different die throws

def standard(num_dice, sides, special):
	average = 0
	sum = 0
	for i in range(6):			# 6 stats so roll 6 times
		for i in range(num_dice):
# at end of loop, sum should contain totals of all 6 stats added together				
			sum += random.randint(1, sides)
	average = sum / 6 
	return average		

def r1(num_dice, sides, special):
	average = 0
	sum = 0
	for i in range(6):			# 6 stats so roll 6 times
		for i in range(num_dice):
			roll = random.randint(1, sides)
			while roll == 1:	# reroll if roll == 1, leave loop after it is not 1 
				roll = random.randint(1, sides)				
			sum += roll		# add roll value to sum
	average = sum / 6				# average stat 
	return average

def x2(num_dice, sides, special):
	average = 0
	sum = 0
	for i in range(6):	# 6 stats so roll 6 times
		for i in range(num_dice):				
			roll1 = 0
			roll2 = 0
			roll1 += random.randint(1, sides)				
			roll2 += random.randint(1, sides)
			if roll1 >= roll2:
				sum += roll1
			else:
				sum += roll2
	average = sum / 6
	return average

def d1(num_dice, sides, special):
	average = 0
	sum = 0
	roll1 = 0 # use this for when special == 'x2'
	roll2 = 0 # use this for when special == 'x2'
	lowest = 6 # use this for when special == 'd1'

	for i in range(6):			# 6 stats so roll 6 times
		for i in range(num_dice):				
			roll = random.randint(1, sides)
			if roll < lowest:
				lowest = roll
			sum += roll
		sum -= lowest
		lowest = 6
	average = sum / 6
	return average

def dnd_stats(num_dice, sides, special):
	# standard rule
	if special == 'none':
		return standard(num_dice, sides, special)

	# reroll any 1s
	elif special == 'r1':
		return r1(num_dice, sides, special)

	# roll 3 dice twice, take the higher value
	elif special == 'x2':
		return x2(num_dice, sides, special)

	# roll 4 six-sided dice, dropping lowest die roll 
	elif special == 'd1':
		return d1(num_dice, sides, special)
		
# checking averages 
sum_none = 0
sum_r1 = 0
sum_x2 = 0
sum_d1 = 0
n = 10000

for i in range(n):
	sum_none += dnd_stats(3, 6, 'none')
	sum_r1 += dnd_stats(3, 6, 'r1')
	sum_x2 += dnd_stats(3, 6, 'x2')
	sum_d1 += dnd_stats(4, 6, 'd1')
	# averages
	average_none = sum_none / n
	average_r1 = sum_r1 / n
	average_x2 = sum_x2 / n
	average_d1 = sum_d1 / n
	# print
print(average_none, average_r1, average_x2, average_d1)





