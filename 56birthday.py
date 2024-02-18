# 56birthday.py by Kenta Hsu

import random
import sys 

# fill up classroom with randomly chosen birthdays 
# simulate probability that at least two people will 
# share birthdays in a classroom with 23 people 
# command line argument should be, 
# trails = # days in calendar - # people in classroom 

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

def birthday_paradox_single_trial(days, people):
	# first make list with the days in a calendar year
	calendar_list = []
	for i in range(1, days+1):
		calendar_list.append(i)
	# should now have list containing all possible birthdays

	# now simulate if match or no match in a classroom 
	match = False
	match_count = 0
	classroom_list = []
	
	for i in range(people):
		# append classroom list with number from 1 to number of calendar days
		classroom_list.append(random.choice(calendar_list))

	# iterate through classroom list for more than 1 match 
	# (guranteed 23 match, match with self)
	for student_in_question in classroom_list:
		for student in classroom_list:
			if student_in_question == student:
				match_count += 1
	
	# if match count is greater than 1, then match = True 
	if match_count > people:
		match = True

	# return either True or False
	return match

def birthday_paradox(trials, days, people):
	match = 0

	# get data for trials
	for i in range(trials):
		if birthday_paradox_single_trial(days, people) == True:
			match += 1

	# calculate probability of birthday match in requested number of classrooms
	p = match / trials

	# return
	return p

# run 
# print(birthday_paradox(trials, days, people))
print(birthday_paradox(trials, days, people))






