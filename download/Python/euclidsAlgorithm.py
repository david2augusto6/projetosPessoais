def gcd(a, b):
	c = a % b # Let c = a mod b
	if c == 0:
		return b # If c == 0, the answer is b
	else:
		return gcd(b, c) # Else, c != 0 and the answer is gcd(b, c)
