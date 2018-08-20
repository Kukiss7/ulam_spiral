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
		if self.end < 0:
			self.end = 0


	def build_primes_set(self):
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


	def numbers_gen(self):
		for value in range(self.start, self.end):
			is_prime = value in self.primes
			number = Number(value, is_prime)
			yield number



if __name__ == '__main__':
	num_set = PrimesSet(23)
	print(num_set.primes_set)
	numbers = NumbersGen(25)
	for n in numbers.gen:
		print(n)

