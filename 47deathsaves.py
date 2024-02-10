# 47deathsaves.py by Kenta Hsu 

import random

# roll d20 on your turn
# if roll is less than 10 record "failure"
# if roll is more than 10 record "success"

# if you collect 3 'failure's you die 
# if you collect 3 'success's you are stable
# if you roll 1 it counts as 2 failures
# if you roll 20, you gain 1 health and revive. 

# calculate probability of death, stablize, and revive 

def death_saves():
	# initializing 
	fail = 0
	success = 0
	current_roll = 0
	revive = 0

	# continue to roll until you die, stablize, or revive 
	while success < 3 and fail < 3 and revive == 0:
		current_roll = random.randint(1, 20)
		# order of if/elifs matter here, need to check for 1 and 20 first
		if current_roll == 20: revive = 1
		elif current_roll == 1:	fail += 2
		elif current_roll >= 10:success += 1
		elif current_roll < 10:	fail += 1
	# evaluate 
	if success == 3:
		return 'stable'
# has to be equal or greater than 3, 
# fail can equal 4 if you roll a 1 with 2 fails
	if fail >= 3:		
		return 'dead'
	if revive == 1:
		return 'revived'

def prob_death_saves():
	# initialize 
	total = 0
	dead = 0
	stable = 0
	revived = 0
	current = ''

	# simulate 10000 death saves
	for i in range(100000):
		total += 1
		current = death_saves()
		if current == 'dead':
			dead += 1
		elif current == 'stable':
			stable += 1
		elif current == 'revived':
			revived += 1
	# compute and print each probability 
	print('Probability of death is', dead/total, sep=' ')
	print('Probability of reviving is', revived/total, sep=' ')
	print('Probability of stablizing is', stable/total, sep=' ')

prob_death_saves()