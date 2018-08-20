

def is_prime(number):
	""" Checks if given number is a prime number"""
	if not isinstance(number, int):
		raise TypeError("The number must be an int number")
	elif number < 0:
		return False
	elif number in [0,1]:
		return False

	for n in range(2, number):
		if number % n == 0:
			return False
		else:
			continue
	else:
		return True


