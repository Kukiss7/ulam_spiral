from prime_numbers import Number, PrimesSet, NumbersGen
import unittest

class TestPrimesSet(unittest.TestCase):
	def test_inputs_negative_int(self):
		test_prime_set = PrimesSet(-100)
		self.assertFalse(test_prime_set.primes_set)

		test_prime_set2 = PrimesSet(-7)
		self.assertFalse(test_prime_set2.primes_set)


	def test_inputs_0_and_1(self):
		test_prime_set = PrimesSet(0)
		self.assertFalse(test_prime_set.primes_set)

		test_prime_set2 = PrimesSet(1)
		self.assertFalse(test_prime_set2.primes_set)


	def test_input_23(self):
		test_primes_set = PrimesSet(23)
		self.assertEqual(test_primes_set.primes_set, {2,3,5,7,11,13,17,19,23})


	def test_contain_method_true(self):
		test_prime_set = PrimesSet(100)
		self.assertTrue(3 in test_prime_set)
		self.assertTrue(11 in test_prime_set)
		self.assertTrue(23 in test_prime_set)
		self.assertTrue(89 in test_prime_set)


	def test_contain_method_false(self):
		test_prime_set = PrimesSet(100)
		self.assertFalse(6 in test_prime_set)
		self.assertFalse(10 in test_prime_set)
		self.assertFalse(0 in test_prime_set)
		self.assertFalse(91 in test_prime_set)


if __name__ == '__main__':
	unittest.main()
