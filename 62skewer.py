# 62skewer.py by Kenta Hsu 

# 61skewer is computationally inefficient 
# as you move the window over by 1 each time there is no need to count everything in the middle again
# it's just the beginning and the end that is changing 

# more efficient is to only read the first window
# after the first, drop off one nucleotide on left and then add one to right 

# write program and test on e.coli genome with 1000 nt window 

# import 
import dogma
import sys
import mcb185 # this python script is in the mcb185_homework directory
# the soft link for the mcb_185 library is in there as well, thus no error

# get path to genome file from CLI argument
# file will be in fasta format 
path = sys.argv[1]	# should be GCF_000005845.2_ASM584v2_genomic.fna.gz (use soft link ecoli.fna.gz)
# read_fasta function returns a single tuples with each element as a defline and seq in a tuple

def fasta_to_lists(path):	# returns two lists with defline and seq
	# store defline and sequence in a list 
	# not working with multiple records for this problem
	defline_list = []
	seq_list = []
	
	# append above lists using fasta reader in mcb185 library 
	for defline, seq in mcb185.read_fasta(path):						
		defline_list.append(defline)
		seq_list.append(seq)
	# both lists should now contain deflines and seqs 

	# return 
	return defline_list, seq_list 

def better_skewer(path, w):
	# defline list and seq list, contains all 
	defline_list_all, seq_list_all = fasta_to_lists(path)
	# intialize 2 lists to store gc_comp, gc_skew from each window
	gc_comp_from_windows = []
	gc_skew_from_windows = []
	# first string sequence from the first fasta record
	seq = seq_list_all[0]	
	first_window = seq[:w]	
	# store g and c counts for first window (will use same var for each frame)
	g_count = first_window.count('G')
	c_count = first_window.count('C')
	# append first gc comp and skew
	gc_comp_from_windows.append(dogma.gc_comp(first_window))
	gc_skew_from_windows.append(dogma.gc_skew(first_window))

	
	# now we can actually run the loop starting at second window
	current_gc_comp = gc_comp_from_windows[0]
	for i in range(1, len(seq) -w + 1):
		# update gc counts and gc_comp based 
		if seq[i-1] == 'G': 
			current_gc_comp -= (1/w)
			g_count -= 1
		if seq[i-1] == 'C':
			current_gc_comp -= (1/w)
			c_count -= 1
		if seq[i+w-1] == 'G':
			current_gc_comp += (1/w)
			g_count += 1
		if seq[i+w-1] == 'C':
			current_gc_comp += (1/w)
			c_count += 1
		gc_comp_from_windows.append(current_gc_comp)
		skew = round((g_count - c_count)/(g_count + c_count), 4)
		gc_skew_from_windows.append(skew)

	return gc_comp_from_windows, gc_skew_from_windows

# run 
comps, skews = better_skewer(path, 1000)
for i, (comp, skews) in enumerate(zip(comps, skews)):
	print(i, comp, skews)
	









