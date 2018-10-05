def is_prime(x):
	if x < 2:
		return False
	else:
		for n in range(2,(x/2)+1):
			if x%n == 0:
				return False
		return True


inp=(input("enter nth no."))
print(sum(x for x in range(inp+1) if is_prime(x)))
