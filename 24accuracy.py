# 24accuracy.py by Kenta Hsu 

# compute F1 score 
def f1(tp, fp, tn, fn):
	precision = tp / (tp + fp)
	recall = tp / (tp + fn)
	f1_score = 2 * ((precision * recall) / (precision + recall))
	return f1_score

print(f1(5,5,5,5))			# should get 0.5

print(f1(1,2,3,4))			# should get 0.25

