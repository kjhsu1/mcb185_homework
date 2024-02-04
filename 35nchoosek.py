# 35nchoosek.py by Kenta Hsu

import math

# n choose k just means the number of combinations 
# of picking k elements from set of n elements


def nchoosek(n, k):
	return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

print(nchoosek(100, 4))

print(nchoosek(5, 4))

print(nchoosek(50, 6))
