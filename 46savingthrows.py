# 46savingthrows.py by Kenta Hsu 

import random

# saving throw is basically roll a 20 sided die 
# to decide whether you pass or fail 
# Relys on "difficulty class" 
# some things give you advantages and disadvantages 

# advantages allows you to take higher of 2 throws 
# disadvantages makes you take lower of 2 throws

# simulate saving throws for diff. class 5, 10, and 15 
# calculate prob. of success normally and with advantage/disadvantage

def normal(difficulty_class):			# normal throw
	roll = random.randint(1, 20)
	if roll >= difficulty_class:
		return 'PASS'
	else:
		return 'FAIL'

def advantage(difficulty_class):		# throw with advantage
	# initializing
	first_throw = random.randint(1, 20)		
	second_throw = random.randint(1, 20)
	max = 0
	
	# determine which throw is max
	if first_throw >= second_throw:
		max = first_throw
	else:
		max = second_throw

	# now see if max beats the difficulty class 
	if max >= difficulty_class:
		return 'PASS'
	else:
		return 'FAIL'

def disadvantage(difficulty_class):
	# initializing
	first_throw = random.randint(1, 20)		
	second_throw = random.randint(1, 20)
	min = 0

	# determine which throw is min 
	if first_throw <= second_throw:
		min = first_throw
	else:
		min = second_throw

	# now see if min beats difficulty class
	if min >= difficulty_class:
		return 'PASS'
	else:
		return 'FAIL'		# throw with disadvantage

def prob_of_success(situation, difficulty_class):
	# initialize
	total = 0
	success = 0
	success_rate = 0
	# for each situation

	# normal
	if situation == 'normal':
		# for loop 10000 to simulate 10000 rolls 
		for i in range(10000):
			total += 1
			if normal(difficulty_class) == 'PASS':
				success += 1
	# advantage 
	if situation == 'advantage':
		for i in range(10000):
			total += 1
			if advantage(difficulty_class) == 'PASS':
				success += 1

	# disadvantage
	if situation == 'disadvantage':
		for i in range(10000):
			total += 1 
			if disadvantage(difficulty_class) == 'PASS':
				success += 1

	# computing overall sucess rate 
	success_rate = success / total
	return success_rate



# making table 
situation = '		Normal Advantage Disadvantage'
print(situation)
for i in range(5, 16, 5):
	print('DC:', i, ' ', prob_of_success('normal', i), ' ', 
	prob_of_success('advantage', i), ' ', 
	prob_of_success('disadvantage', i), sep=' ', end='\n')


