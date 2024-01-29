# 55colorname.py by Kenta Hsu

# program provdies closest official color name given RGB values 
# all value between 0-255

import sys 

colorfile = sys.argv[1]		# file that contains official color definitions
# enter RGB values for the color you want ot identify in the CLI 
R = int(sys.argv[2])	
G = int(sys.argv[3])
B = int(sys.argv[4])

# put RGB values in a list
requested_rgb_list = []

requested_rgb_list.append(R)
requested_rgb_list.append(G)
requested_rgb_list.append(B)

# not a gff file, but need to use 'with' and 'as' keywords to iterate through every line
# what is considered the 'closest color'?
# We are not using Euclidean distance but rather taxicab distance 
# taxicab distance is defined as the absolute difference of each value summed up 
# in our instance it will be below
# taxicab_distance = abs(requested_red - official_color_red) + abs(requested_green - official_color_green) + abs(requested_blue - official_color_blue)

def rgb_taxicab_distance(requested_rgb_list, official_rgb_list):	# lists contain RGB value in RGB order
	distance = 0
	
	for requested, official in zip(requested_rgb_list, official_rgb_list):	# iterate through both lists at the same time
		distance += abs(requested - official)	# get taxicab distance
	
	return distance 

# you want to have a variable that keeps track of minimum taxicab distance
# run through each line in colorfile, get taxicab distance, update min variable accordingly 
def closest_official_color(requested_rgb_list, colorfile):
	matching_color = ''	
	min = 100000000 # infinity

	with open(colorfile) as file:
		for line in file:
			# first split line into list, delimiter is empty space
			list = line.split()
			
			# then split list[2] with ',' as delimiter to get new list that contains official RBG values 
			# elements are string objects so convert to int
			official_rgb_list = list[2].split(',')
			for i, value in enumerate(official_rgb_list):
				official_rgb_list[i] = int(value)

			
			# find taxicab distance with the current official color and update best matching color and min
			taxicab_dist = rgb_taxicab_distance(requested_rgb_list, official_rgb_list)
			if taxicab_dist < min:
				min = taxicab_dist
				matching_color = list[0]
		
		# matching_color should now store the color name of best match

	# return 
	return matching_color

# run
print(closest_official_color(requested_rgb_list, colorfile))
