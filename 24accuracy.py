# 24accuracy.py by Kenta Hsu 

# compute F1 score 
def performance(tp, fp, tn, fn):
	precision = tp / (tp + fp)
	recall = tp / (tp + fn)
	f1_score = 2 * ((precision * recall) / (precision + recall))
	accuracy = (tp + tn) / (tp + fp + tn + fn)
	return f1_score, accuracy

print(performance(5, 5, 5, 5))			# should get 0.5

print(performance(1, 2, 3, 4))			# should get 0.25

print(performance(3, 5, 8, 10))