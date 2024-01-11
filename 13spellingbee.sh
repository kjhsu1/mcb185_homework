# Use dictionary.gz from Code/data/
# 'R' must be in every word 
# 4 or more letters 
# "Z" "O" "N" "I" "A" "C" can be used as many times as you want 

# dictionary.txt is a gzipped/compressed file so just stdout using gunzip command

# First grep all lines in dictionary.txt with "R"
# Now stdout should just be words with R 

# Then pipe stdout grep -v "[INSERT ALL ALPHABET CHARACTERS EXCEPT FOR ZONIAC]+"
# This deletes all lines containing alphabets other than ZONIAC one or more times. 

# All characters are either RZONIAC now 
# So all that is left is to grep ".{4}" to now be left with stdout with all words over 4 characters

gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "r" | grep -v -E "[bdefghjklmpqstuvwxy]+" | grep -E ".{4}" 