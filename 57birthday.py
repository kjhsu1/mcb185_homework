# 57birthday.py by Kenta Hsu

import random 
import sys

# number of trials
# number of days in calendar 
# number of people in classroom
trials = int(sys.argv[1])
days = int(sys.argv[2])
students = int(sys.argv[3])


# make calendar list, calendar = [0] * 365 
# for loop through # of people
# in each loop birthd = random.choose(0, 364)
# then calendar[birthd] += 1

# at the end iterate through the calendar list
# if any element is greater than 1, then there is match

# takes in # of days in calendar 
# also takes in # of students
def birthday_paradox_single_trial(days, students):
	calendar = [0] * days
	# for each student in the classroom...
	for i in range(students):
		bday = random.randint(0, days - 1)
		calendar[bday] += 1

	# calendar should be updated with all students bday
	# iterate through list calendar
	# check for values above 1 
	match = False
	for days in calendar:
		if days > 1:
			match = True
	# return True or False
	return match

def birthday_paradox(trials, days, students):
	match = 0

	# get data for trials
	for i in range(trials):
		if birthday_paradox_single_trial(days, students) == True:
			match += 1

	# calculate probability of birthday match in requested number of classrooms
	p = match / trials

	# return
	return p

# run 
print(birthday_paradox(trials, days, students))




