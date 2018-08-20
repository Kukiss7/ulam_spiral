import math


class Number:
	""" Represents the number
		value: int
		is_prime: bool
	"""
	def __init__(self, value, is_prime):
		self.value = value
		self.is_prime = is_prime


	def __str__(self):
		res = ''
		res = str(self.value)
		if self.is_prime:
			res += ' prime'
		return res


	def __eq__(self, other):
		return self.value == other.value and self.is_prime == other.is_prime


class PrimesSet:
	""" Represents set of prime numbers
		end: int - max value
		self.primes_set: set of prime numbers
	"""
	def __init__(self, end):
		self.end = end
		self.check_for_negative_end()
		self.primes_set = self.build_primes_set()


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
		return primes	


class NumbersGen:
	""" Represents set of Number objects
		end: int
		start: int
		primes: PrimesSet object
		gen: generator with Number objects
	"""
	def __init__(self, end, start=0):
		self.end = end
		self.start = start
		self.primes = PrimesSet(end)
		self.gen = self.numbers_gen()


	def __iter__(self):
		return self.gen


	def numbers_gen(self):
		""" Makes generator of Number objects
		"""
		for value in range(self.start, self.end+1):
			is_prime = value in self.primes
			number = Number(value, is_prime)
			yield number



if __name__ == '__main__':
	numbers = NumbersGen(15000, start=14960)
	for number in numbers:
		print(number)
