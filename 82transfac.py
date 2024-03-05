# 82transfac.py by Kenta Hsu 
import sys
import re
import gzip
# things to store
# prob best store this all in a dictionary
# key: (ie. ID, etc) 

# AC: 1 string (should make this the dictionary key)
# ID: 1 string 
# DE: tuple(list w/ 2 strings), 1 string)
# PO: dictionary w/ keys: number of nts in motif
				   # value: dictionary w/ keys: A, C, G, T
				   						# value: prob each base
# tax_group: 1 string
# tf_family: 1 string
# pubmed: 1 string 
# uniprot..: 1 string 
# data_type: 1 string 

# use 24lines.transfac (first 24 lines of the transfac file)
# read each line at a time 
# startswith()?
# after three 'X' starts create new dictionary

path = sys.argv[1]
with gzip.open('24lines.transfac.gz')as fp:
	transfac_dict = {} # key: AC name
	ac = '' # track ac
	
	for line in fp:
		line = line.rstrip()
		print(line)
		if line[:2] == 'AC':
			ac = line[3:]
			transfac_dict[ac] = {}
			continue
		if line[:2] == 'XX': continue
		
		# if not 'AC' or 'XX'
		tag = line[:2] 
		if tag == 'ID':
			transfac_dict[ac][tag] = line[3:]
		elif tag == 'DE':
			list1 = line.split(' ; ')
			list2 = list1[0].split()
			transfac_dict[ac][tag] = [list2[2], list1[1]]
		elif tag == 'PO':
			transfac_dict[ac][tag] = {}
		elif tag == 'CC':
			sub_str = line[3:]
			list4 = sub_str.split(':')
			transfac_dict[ac][list3[0]] = list4[1]
		else: # for all the lines with numbers
			list3 = line.split()
			print(list3)
			transfac_dict[ac]['PO'][line[:2]] = [list3[1], list3[2], 
			list3[3],list3[4]]



