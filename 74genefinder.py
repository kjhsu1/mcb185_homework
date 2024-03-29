# 74genefinder.py by Kenta Hsu

import sys
import mcb185 # for fasta reader

path = sys.argv[1]
orf_min_length = sys.argv[2]

# input: FASTA fna file 
# output: GFF formatted gene features 
# maybe something like:

'''
CDS		start	stop 
1 
2
3
'''

# minimum ORF is 300 nt including stop codon
# e.coli so no introns
# meaning just locate all ATGs 
# sliding window with w = 3, move by 1
# ribosomes only read 5' to 3'

# function that finds all coordinates for A in ATG in a strand 
# takes in: seq (as a string), reading frame(1,2,3)
# returns: list of start codons (coords relative to input strand)
def list_of_starts(seq, frame):
	starts = [] # store start codon coords
	w = 3 # window
	if frame == 1:
		# sliding window, k = 3
		for i in range(0, len(seq) -w +1, w):
			window = seq[i:i+w]
			if window == 'ATG':
				starts.append(i+1) # +1 to adjust to 1-index coords
	if frame == 2:
		for i in range(1, len(seq) -w +1, w): # skip first nt, start at second
			window = seq[i:i+w]
			if window == 'ATG':
				starts.append(i+1)
	if frame == 3:
		# skip first and second nt, start at 3rd
		for i in range(2, len(seq) -w +1, w): 
			window = seq[i:i+w]
			if window == 'ATG':
				starts.append(i+1)
	return starts

# function that finds all coordinates for the 3rd letter in stop codon
# takes in: seq (as a string), frame (1, 2, 3)
def list_of_stops(seq, frame):
	stops = [] # store all coords of 3rd letter in stop codon
	w = 3 # window
	if frame == 1:
		# sliding window, k = 3
		for i in range(0, len(seq) -w +1, w):
			window = seq[i:i+w]
			if window == 'TAG' or window == 'TGA' or window == 'TAA':
				stops.append(i+3) # +2 b/c 3rd nt, +1 to adjust to 1-index
	if frame == 2:
		for i in range(1, len(seq) -w +1, w): # skip first nt, start at second
			window = seq[i:i+w]
			if window == 'TAG' or window == 'TGA' or window == 'TAA':
				stops.append(i+3)
	if frame == 3:
		# skip first and second nt, start at 3rd
		for i in range(2, len(seq) -w +1, w): 
			window = seq[i:i+w]
			if window == 'TAG' or window == 'TGA' or window == 'TAA':
				stops.append(i+3)
	return stops

# make sure both starts and stop lists are numerically sorted
# *note think function doesn't handle some situations
# 1. No stop or start codons
# 2. Some stop but no start codons
# 3. No stop but no start codons
# may need to fix?

# takes in: start and stop codon coords as lists
# returns: dict with all CDS regions
def best_start_stop(starts, stops):
	cds_dict = {} # collect start stop pair, if just start no end then end = none

	# iterate through all stop codon
	# track the last stop codon
	prev_stop = 0
	for stop in stops:
		best_start = float('inf') # track start of best match
		for start in starts:
			# find the most upstream start codon 
			# between prev stop codon and current
			if start > prev_stop and start < stop and start < best_start:
				best_start = start
		prev_stop = stop  # update prev_stop
		# after checking all start codons, add start-stop pair to dictionary
		if best_start == float('inf'): # when no matching start codon
			continue
		else:
			cds_dict[best_start] = stop

	# with above algorithm we miss situations where there are start codons
	# after the most downstream stop codon 
	# add CDS of for these occasions 
	for start in starts:
		# if start is greater than most 3' stop codon
		if start > stops[-1]:
			cds_dict[start] = ' to the end of seq'
			# return right away 
			# first start codon that satisfies if conds. is the one we want
			return cds_dict
	# return here if we didn't miss any CDS with first algorithm 
	return cds_dict	

# function that checks if ORF is 300 nt
# takes in: dictionary with all CDS regions
# returns: dictionary with CDS regions w/ length >= 300nt
def orf_filter(cds_dict, orf_min_length, seq):
	filtered_dict = {} # store only CDS region >300
	for start, stop in cds_dict.items():
		if type(stop) == int:
			length = int(stop) - int(start) + 1 
			if length >= int(orf_min_length): # if CDS >= 300
				filtered_dict[start] = stop # add to new dict
		# if CDS goes all way to the end
		elif type(stop) == str:
			length = len(seq) - int(start) + 1
			if length >= int(orf_min_length):
				filtered_dict[start] = len(seq)

	return filtered_dict


# dictionary stores CDS for each reading frame
# ie. keys = 1, 2, 3, -1, -2, -3
cds_all_frames = {} 

# harvest len(seq)
# will use at the end
seq_length = 0

# for frames 1, 2, 3
for i in range(1, 4):
	for defline, seq in mcb185.read_fasta(path):
		seq_length = len(seq)
		starts = list_of_starts(seq, i)
		stops = list_of_stops(seq, i)
		cds = best_start_stop(starts, stops)
# filtered cds regions (start-end dictionaries)
		cds = orf_filter(cds, orf_min_length, seq)
		cds_all_frames[i] = cds 
# for frames -1, -2, -3
# have to adjust coordinates so it's relative to + strand 
for i in range(1, 4):
	for defline, seq in mcb185.read_fasta(path):
		seq = mcb185.anti_seq(seq) # reverse-comp
		starts = list_of_starts(seq, i)
		stops = list_of_stops(seq, i)
		cds = best_start_stop(starts, stops)
# filtered cds regions (start-end dictionaries)
		cds = orf_filter(cds, orf_min_length, seq)
		cds_all_frames[-i] = cds 
		# key: -1, -2, -3
		# value: dictionary w/ start: stop as keys

# convert CDS dictionary into GFF format 
# cds_all_frames is a dictionary containing 6 dictionaries for each frame
print('frame\tCDS\tstart\tstop')

# iterate through 6 dictionaries for each frame
# keys: frame # (ie. 1, 2, 3, -1, -2, -3)
# values: dictionaries w/ start-stop for particular frame
for frame_number, cds_in_frame in cds_all_frames.items(): 
	cds_number = 1
	for start, stop in cds_in_frame.items():
		# if frame # is less than 0 as in the - strand...
		if frame_number < 0:
			# adjusted start and stops
			# now relative to + strand
			adj_start = seq_length-stop 
			adj_stop = seq_length-start
			print(f'{frame_number}\t{cds_number}\t{adj_start}\t{adj_stop}')
		# if frame # is greater than 0 as in the + strand...
		# you don't have to adjust the coords
		elif frame_number > 0:
			print(f'{frame_number}\t{cds_number}\t{start}\t{stop}')
		cds_number += 1

















