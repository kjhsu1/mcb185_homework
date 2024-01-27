# 53genomestats.py by Kenta Hsu

# reads GFF file and reports info about length of GFF features
'''
- features are in the 3rd column
- intron, exon, gene,etc 
- find all of the below for each feature in the 3rd column
'''
# count, min, max, mean, standard deviation, median

# run program on files for A.thaliana, C.elegans, and D.melanogaster
# all files are gzipped 

import gzip
import math

# first write path to A.thaliana, C.elegans, and D.melanogaster gzipped files 
path_a_thaliana = '/Users/kentahsu/Code/MCB185/data/A.thaliana.gff.gz'
path_c_elegans = '/Users/kentahsu/Code/MCB185/data/C.elegans.gff.gz'
path_d_melangaster = '/Users/kentahsu/Code/MCB185/data/D.melanogaster.gff.gz'

def features_into_list(path_to_file):		# takes in path to gff file, returns alphabetically sorted list of features
	features = []
	with gzip.open(path_to_file, 'rt') as file:		# now file is accessable 
		
		# first makes list with all features
		for line in file:
			if line[0] == '#': continue 	# if first element is '#' it is a comment so go to next line
			
			# if first element is not a comment, check if contains new feature
			column = line.split() 			# create list, each list element is the element in each column (ie. words[0] == column 1)
			match = False
			
			for feature in features:		# compare with each previously found feature 
				if feature == column[2]: match = True

			# if no matches add new feature
			if match == False: features.append(column[2])
	
	features.sort()		# into alphabetical order
	return features 	# returns list 

def std_dev(dataset_as_list):			# takes in numerical data set as list, returns standard deviation
	# initialize
	N = len(dataset_as_list)	# sample size
	sum = 0
	mean = 0
	sigma = 0
	sd = 0
	
	for number in dataset_as_list:
		sum += number

	mean = sum / N 		# find mean 

	for number in dataset_as_list: sigma += (number - mean)**2

	# compute standard deviation
	sd = math.sqrt(sigma / (N - 1))
	return sd

def median(dataset_as_list):			# takes in numerical data set as list, returns median
	# initialize
	median = 0

	dataset_as_list.sort() 		# should sort numerically 
	N = len(dataset_as_list)	# sample size

	# if N is odd
	if N % 2 != 0: median = dataset_as_list[(N // 2)]
	# if N is even
	else: median = median = (dataset_as_list[int((N // 2 - 1))] + dataset_as_list[int(N // 2)])

	# return 
	return median

def genome_stats(path_to_file):
	# initialize varibles used to store stats for all features
	features = features_into_list(path_to_file)
	count = []
	minimum = []
	maximum = []
	std_dev = []		
	median = []

	with gzip.open(path_to_file, 'rt') as file:	# now file is accessable
		for feature in features:				# loop through individual features, update add to respective lists containing stats
			
			# initialize variables for the current feature
			count = 0
			minimum = 0
			maximum = 0
			length_list = []					# will numerically sort later to find median, can also use this for std deviation

			for line in file:					# if first element is '#' it is a comment so go to next line
				if line[0] == '#': continue 			

				column = line.split() 			# create list, each list element is the element in each column (ie. words[0] == column 1)
				
				if column[2] == feature:		# see if line has feature 
					count += 1
					length = int(column[4]) - int(column(3)) + 1
					length_list.append(length)		# add length of seq with current feature 
					if length > max: max = length 	# update max
					if length < min: min = length 	# update min 

			# append 
			count.append(count)
			minimum.append(minimum)
			maximum.append(maximum)
			std_dev.append(std_dev(length_list))
			median.append(median(length_list))
	# return 
	return features, count, minimum, maximum, std_dev, median


# first thing is to find how many categories there are. Create a loop for that 
# can utilize iteration through containers 
''' 
create a new list variable, store all of the categories here

We don't want duplicates, so when checking 3rd column of each line, do a container iteration for the list

if no matches found, then append the list 
'''
data = [4, 3, 2, 1]
print(median(data))

