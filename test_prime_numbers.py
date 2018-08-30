from prime_numbers import PrimesSet
import unittest



class TestPrimesSet(unittest.TestCase):
	def test_inputs_negative_int(self):
		test_primes_set = PrimesSet(-100)
		test_primes_set.build_primes_set()

		self.assertFalse(test_primes_set.primes_set)

		test_primes_set2 = PrimesSet(-7)
		test_primes_set2.build_primes_set()

		self.assertFalse(test_primes_set2.primes_set)


	def test_inputs_0_and_1(self):
		test_primes_set = PrimesSet(0)
		test_primes_set.build_primes_set()

		self.assertFalse(test_primes_set.primes_set)

		test_primes_set2 = PrimesSet(1)
		test_primes_set2.build_primes_set()

		self.assertFalse(test_primes_set2.primes_set)


	def test_input_23(self):
		test_primes_set = PrimesSet(23)
		test_primes_set.build_primes_set()

		self.assertEqual(test_primes_set.primes_set, {2,3,5,7,11,13,17,19,23})


	def test_contain_method_true(self):
		test_primes_set = PrimesSet(100)
		test_primes_set.build_primes_set()

		self.assertTrue(3 in test_primes_set)
		self.assertTrue(11 in test_primes_set)
		self.assertTrue(23 in test_primes_set)
		self.assertTrue(89 in test_primes_set)


	def test_contain_method_false(self):
		test_primes_set = PrimesSet(100)
		test_primes_set.build_primes_set()
		
		self.assertFalse(0 in test_primes_set)
		self.assertFalse(6 in test_primes_set)
		self.assertFalse(10 in test_primes_set)
		self.assertFalse(91 in test_primes_set)


if __name__ == '__main__':
	unittest.main()
