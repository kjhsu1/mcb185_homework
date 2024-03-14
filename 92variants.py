# 92variants.py by Kenta Hsu

# ASK HOW WE CAN ADJUST THE COORDS OF START/END OF FEATURE IN GFF WHEN 
# STRAND IS MINUS
# A: WE DON'T NEED TO ADJUST COORDINATES
 # reason is that even if the strand is '-', the coordinate numbrs are still
 # relative to the + strand
 # this is also probably the reason why we are not getting the correct numbers 
 # for the 8*.py assignments

# use vcf and gff file
# TESTED ON C.ELEGANS FILES
# extract variant nt position and chromosome
# iterate through gff file and find in which feature the variant is in

# first go through the vcf and extract nt coords and chromosome number 
import sys
import gzip

vcf = sys.argv[1]
gff = sys.argv[2]

# list stores tuple with three elements
# chrom, coords, and feature

# extracts chrom and coords for each variance
# in: path of vcf file 
# out: list of tuples, (chrom, coords)
def variants(path):
	# tuple with (chrom, coords)
	variants = []

	with gzip.open(path, 'rt') as file:
		for line in file:
			words = line.split()
			# chromosome number 
			chrom = words[0]
			# nt coords 
			coords = int(words[1])
			# append variants
			variants.append((chrom, coords))
	# return
	return variants

# for each variant, search which feature it belongs in 
def variant_features(path, variants):
	# store dictionaries
	# key: variant coordinate
	# value: dictionary
		# keys: ex. chrom: I, features: [intron, transcript_region]
	var_feat = {}
	# run through each line of gff file 
	with gzip.open(path, 'rt') as file:
		for line in file:
			# if comment line then skip
			if line.startswith('#'): continue
			# if it is not a comment line...
			words = line.split()

			# if feature is intron, gene, snoRNA, exon, etc
			# kinda works for transcript region
				# strand just equals '.' for this feature
			
			# feature 
			feature = words[2]
			# start and end 
			start = int(words[3])
			end = int(words[4])
			# chrom
			chrom = words[0]
			# strand
			strand = words[6]

			# Even if strand is '-' you don't have to adjust anything
			# b/c feature start and end coords are already relative to '+' strand
			
			# for each line in gff, iterate through all of variants
			for variant in variants:
				variant_chrom = variant[0]
				variant_coord = int(variant[1])
				
				# if chrom # doesn't match, continue
				if variant_chrom != chrom: continue
				# now see if variant SNP is within the start/end of feature
				if variant_coord >= start and variant_coord <= end:
					# if variant not yet in dictionary
					if variant_coord not in var_feat:
						var_feat[variant_coord] = {
							'chrom': chrom, 
							'features': [feature]
						}
					if variant_coord in var_feat:
						# make sure you don't append the same feature twice
						if feature not in var_feat[variant_coord]['features']:
							var_feat[variant_coord]['features'].append(feature)
	# return
	return var_feat 

# run 
variant_list = variants(vcf)
variant_dict = variant_features(gff, variant_list)

# print nicely
for key in variant_dict:
	chrom = variant_dict[key]['chrom']
	coord = key	
	features_list = variant_dict[key]['features']
	print(f'{chrom:<8}{coord:<8}', end='')
	for i, feature in enumerate(features_list):
		print(feature, end='')
		if i != len(features_list)-1:
			print(',', end='')
	# change line
	print()




