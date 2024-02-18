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

# first thing is to find how many categories there are. Create a loop for that 
# can utilize iteration through containers 
''' 
create a new list variable, store all of the categories here

We don't want duplicates, so when checking 
3rd column of each line, do a container iteration for the list

if no matches found, then append the list 
'''

import gzip
import math
import sys

std_input_feature = sys.argv[2]
std_input_path = sys.argv[1]

# takes in path to gff file, returns alphabetically sorted list of features
def features_into_list(path_to_file):	
	features = []
	with gzip.open(path_to_file, 'rt') as file:		# now file is accessable 
		
		# first makes list with all features
		for line in file:
			# if first element is '#' it is a comment so go to next line
			if line[0] == '#': continue
			
			# if first element is not a comment, check if contains new feature
			# create list, each list element is the element in each column
			column = line.split()	
			match = False
			
			# compare with each previously found feature 
			for feature in features:
				if feature == column[2]: match = True

			# if no matches add new feature
			if match == False: features.append(column[2])
	
	features.sort()		# into alphabetical order
	return features # returns list 
# takes in numerical data set as list, returns standard deviation
def std_dev(dataset_as_list):	
	# initialize
	N = len(dataset_as_list)	# sample size
	sum = 0
	mean = 0
	sigma = 0
	sd = 0

	# in case there was only 1 match in the database for the feature
	if N == 1: 
		return 0
	else:
		for number in dataset_as_list:
			sum += number

		mean = sum / N # find mean 

		for number in dataset_as_list: sigma += (number - mean)**2

		# compute standard deviation
		sd = math.sqrt(sigma / (N - 1))
		return round(sd)
# takes in numerical data set as list, returns median
def median(dataset_as_list):
	# initialize
	median = 0

	dataset_as_list.sort() # should sort numerically 
	N = len(dataset_as_list)	# sample size

	# if N is odd
	if N % 2 != 0: median = dataset_as_list[(N // 2)]
	# if N is even
	else: 
		median = (dataset_as_list[int((N // 2 - 1))] 
		+ dataset_as_list[int(N // 2)]) / 2
	# return 
	return round(median)

def mean(dataset_as_list):
	sum = 0
	for item in dataset_as_list:
		sum += int(item)
	return round(sum / len(dataset_as_list))

def genome_stats(path_to_file, requested_feature):
	# initialize varibles used to store stats for all features
	all_features = features_into_list(path_to_file)
	all_count = []
	all_minimum = []
	all_maximum = []
	all_mean = []
	all_std_dev = []		
	all_median = []
	requested_feature_index = 0 
	# will use when returning specifically the information 
	# for the requested feature
	requested_feature_list_of_stats = [] # will use for above purpose as well

	# loop through individual features, 
	# update add to respective lists containing stats
	for feature in all_features:		
		# initialize variables for the current feature
		count = 0
		minimum = 1000000000 # or infiinity
		maximum = 0
		# will numerically sort later to find median, 
		# can also use this for std deviation
		length_list = []	
		with gzip.open(path_to_file, 'rt') as file:
			# if first element is '#' it is a comment so go to next line
			for line in file:
				if line[0] == '#': continue		
		# create list, each list element is the element in each column
				column = line.split() 

				if column[2] == feature: # see if line has feature 
					count += 1
					
					length = int(column[4]) - int(column[3]) + 1
					# add length o f seq with current feature
					length_list.append(length)
					if length > maximum: maximum = length # update max
					if length < minimum: 
						minimum = length # update min 
			# append 
			all_count.append(count)
			all_minimum.append(minimum)
			all_maximum.append(maximum)
			all_mean.append(mean(length_list))
			all_std_dev.append(std_dev(length_list))
			all_median.append(median(length_list))
	
	# all of the 'all' variables are updated, 
	# now just need to return specifically the requested_feature
	# find the index for the requested feature
	requested_feature_index = all_features.index(requested_feature)	
	
	# append list using the feature index
	requested_feature_list_of_stats.append(all_count[requested_feature_index])
	requested_feature_list_of_stats.append(all_minimum[requested_feature_index])
	requested_feature_list_of_stats.append(all_maximum[requested_feature_index])
	requested_feature_list_of_stats.append(all_mean[requested_feature_index])
	requested_feature_list_of_stats.append(all_std_dev[requested_feature_index])
	requested_feature_list_of_stats.append(all_median[requested_feature_index])
	
	# return list with stats for requested feature
	return requested_feature_list_of_stats

print(genome_stats(std_input_path, std_input_feature))

