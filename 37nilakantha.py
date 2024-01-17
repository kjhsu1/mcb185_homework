# 37nilakantha.py by Kenta Hsu

# estimate pi with Nilakantha series 

def nilakantha(n):
	a = 2
	b = 3
	c = 4
	counter = 0
	pi_estimate = 3
	for i in range(n):
		if counter % 2 == 0:
			pi_estimate = pi_estimate + 4/(a*b*c)
		else:
			pi_estimate = pi_estimate - 4/(a*b*c)
		a = a + 2 
		b = b + 2 
		c = c + 2
		counter = counter + 1
	return pi_estimate

print(nilakantha(3))

print(nilakantha(100))

print(nilakantha(1000))

