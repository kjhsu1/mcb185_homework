# 44randompi.py by Kenta Hsu
import random
import math
# estimate pi using monte carlo methods
 
def monte_carlo():
	total = 0
	count = 0
	while True:
		random_x = random.random()
		random_y = random.random()
		dist_to_origin = math.sqrt(random_x**2 + random_y**2)
		if dist_to_origin < 1:
			count += 1
		total += 1
		print(4 * (count / total))

monte_carlo()
