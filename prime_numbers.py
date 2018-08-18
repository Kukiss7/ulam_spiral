

def is_prime(number):
	if number < 0:
		return False
	elif number in [0,1]:
		return False
	elif not isinstance(number, int):
		raise TypeError("The number must be an int number")
	for n in range(2, number):
		if number % n == 0:
			return False
		else:
			continue
	else:
		return True


