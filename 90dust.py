#!/usr/bin/env python3

# 90dust.py by Kenta Hsu 

import argparse 
import mcb185
import math

# stuff for the --help
# also useful to set default values for parameters 
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20,
	help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4, 
	help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy)

# Harvesting arguments 
path = arg.file
w = arg.size
threshold = arg.entropy 
lower = arg.lower

# meat of program 

# shannon entropy
def shannon_entropy(a, c, g, t):
	# intializing
	h = 0 
	total_nuc = a+t+g+c
	
	# probability of occurance for each base
	a_prob = a / total_nuc			
	c_prob = c / total_nuc
	g_prob = g / total_nuc
	t_prob = t / total_nuc
	
	if a_prob != 0: 
		# expressions inside the sigma
		h = h + a_prob * math.log2(a_prob)
	if c_prob != 0: 
		h = h + c_prob * math.log2(c_prob)
	if g_prob != 0: 
		h = h + g_prob * math.log2(g_prob)
	if t_prob != 0: 
		h = h + t_prob * math.log2(t_prob)

	return -h	# final entropy value

# dust function with added 'lower' parameter
def dust(seq, w, threshold, lower): # added 'lower' parameter
	# so we can change char to 'N'
	seq_as_list = list(seq)
	# same idea as 62skewer 
	# only need to take a, t, g, c, count for the first frame
	# we need each nt count for entropy calc
	first_frame = seq[:w]
	a = first_frame.count('A')
	c = first_frame.count('C')
	g = first_frame.count('G')
	t = first_frame.count('T')
	# check first frame separately 
	if shannon_entropy(a, c, g, t) < 1.4:
		for i in range(w-1): seq_as_list[i] = 'N' 
	
	# now do the rest
	for i in range(1, len(seq_as_list) -w +1):
		# update counts 
		# need to do seq[i-1] not seq_as_list[i-1]
		# bc seq_as_list may contain masked nts
		if seq[i-1] == 'A': a -= 1 
		if seq[i-1] == 'C': c -= 1
		if seq[i-1] == 'G': g -= 1
		if seq[i-1] == 'T': t -= 1

		if seq[i+w-1] == 'A': a += 1
		if seq[i+w-1] == 'C': c += 1
		if seq[i+w-1] == 'G': g += 1
		if seq[i+w-1] == 'T': t += 1
		
		# calc entropy, mask accordingly
		# when lower==False, mask with 'N'
		if shannon_entropy(a, c, g, t) < 1.4 and lower == False: 
			for j in range(i, i+w): seq_as_list[j] = 'N'
		# when lower==True
		if shannon_entropy(a, c, g, t) < 1.4 and lower == True:
			for j in range(i, i+w): 
				# sorry if we can't use lower(), I can fix it
				# make it lowercase
				seq_as_list[j] = seq_as_list[j].lower()
	# join masked list
	seq = ''.join(seq_as_list)
	return seq

# print in FASTA format 
for defline, seq in mcb185.read_fasta(path):
	print(defline)
	print(dust(seq, w, threshold, lower))


# Below are just notes from the module 
#
#
#

''' 
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('size', type=int, help='window size')
parser.add_argument('entropy', type=float, help='entropy threshold')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy)
'''
# the parser is just a thing that searches the CL and checks for those 
# arguments
# another thing is that it automatically creates a help message 

'''
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('--size', type=int, default=20,
	help='window size [%(default)i]')
parser.add_argument('--entropy', type=float, default=1.4, 
	help='entropy threshold [%(default).3f]')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy)
'''

# when you set defaults for parameters, you need to enter it as
# (ie. --size 15) 
# you have to add the two dashed lines and the name of the parameter

# flags 
# can turn on or off behaviors 

'''
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('--size', type=int, default=20,
	help='window size [%(default)i]')
parser.add_argument('--entropy', type=float, default=1.4, 
	help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy)
'''

# the parameter names are too long
# just add the shortened version in front when declaring 

'''
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20,
	help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4, 
	help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()
print('dusting with', arg.file, arg.size, arg.entropy)
'''

# should do the samething as 63dust.py
# the only difference being you give the option for soft masking
# soft masking just makes the letters lowercase instead of 
# replacing with 'N'
# use the default values for size/window, entropy



# don't want to type 'python3' before running this program 
# also want to be able to call it from anywhere

# step 1 is the interpreter directive 
# one line of code at the top of this document 
# basically instructions on which interpreter to send this program to
# in our case into the python interpreter 

# step 2 is executable permission 
# read, write, execute for files and directories 
# basic permission stuff
# most of your own programs should give you all permissions right?
# times where you don't want this are like data files 
# you should only be able to read these

# 3 types of personel access
# just owner, group, or public 

# drwxr-xr-x
# d means directory 
# rwx, first triplet is owner permissions 
# r-x, second triplet is group permissions 
# r-x, third triple is public permissions 

# chmod to change permissions 
# can either do octal way
# ie. chmod 777
# or can do more user friendly way 
# ie. chmod u+rwx 

# step 3 is executable path 

# programs stored in different places 
# ex. ls command is stored in /bin/ls

# places like bin are reserved places 
# meaning we can't put stuff in there 

# the goal is to put our new programs in a place 
# we will then add that place to the executable path 

# bin is traditionally where you store these things 

# printenv PATH 
# colon separted list of places the shell looks for executables
# Code/bin is not here so we have to add it 

# export PATH=$PATH:$HOME/Code/bin
# this adds this as another place for the shell to look for executables

# library paths 
# similar to setting up PATH
# instead we change PYTHONPATH
# this is going to be where the the the python interpreter will look 
# for the python modules



