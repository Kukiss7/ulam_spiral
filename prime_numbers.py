

class PrimesSet:
	""" Represents set of prime numbers
		end: int - max value
		self.primes_set: set of prime numbers
	"""
	def __init__(self, end):
		self.end = end
		self.check_for_negative_end()
		self.primes_set = set()


	def __contains__(self, item):
		return item in self.primes_set


	def check_for_negative_end(self):
		""" Checks self.end class input and resets it to 0 if given negative
		"""
		if self.end < 0:
			self.end = 0


	def build_primes_set(self):
		""" Builds set with prime int numbers
			from 2 to self.end including self.end
		"""
		primes = set()
		for number in range(2, self.end+1):
			for prime in primes:
				if number % prime == 0:
					break
			else:
				primes.add(number)
		self.primes_set = primes



if __name__ == '__main__':
	primes = PrimesSet(100)
	primes.build_primes_set()
	print(sorted(primes.primes_set))
