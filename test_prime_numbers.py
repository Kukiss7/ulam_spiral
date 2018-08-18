from prime_numbers import is_prime
import unittest

class TestIsPrime(unittest.TestCase):
	def test_values_under_0(self):
		numbers_under_0 = [-991, -11, -5, -1]
		for number in numbers_under_0:
			self.assertFalse(is_prime(number))


	def test_values_0_and_1(self):
		self.assertFalse(is_prime(0))
		self.assertFalse(is_prime(1))


	def test_values_primes_under_20(self):
		primes_under_20 = [2,3,5,7,11,13,17,19]
		for number in primes_under_20:
			self.assertTrue(number)


	def test_values_composite_numbers_under_11(self):
		composite_numbers_under_11 = [4,6,8,10]
		for number in composite_numbers_under_11:
			self.assertTrue(number)


	def test_given_data_types(self):
		with self.assertRaises(TypeError):
			is_prime('string')
			is_prime(None)
			is_prime((1,2))
			is_prime(1.5)
			is_prime(True)
			is_prime(3+5j)


if __name__ == '__main__':
	unittest.main()
