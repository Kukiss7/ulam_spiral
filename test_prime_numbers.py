from prime_numbers import Number, PrimesSet, NumbersGen
import unittest

class TestNumber(unittest.TestCase):
	def test_equal_method_compare_non_prime(self):
		num_0a = Number(0, False)
		num_0b = Number(0, False)
		num_6a = Number(6, False)
		num_6b = Number(6, False)

		self.assertTrue(num_0a==num_0b)
		self.assertTrue(num_6a==num_6b)
		self.assertTrue(num_0a!=num_6a)
		self.assertTrue(num_6b!=num_0b)

		self.assertFalse(num_0a!=num_0b)
		self.assertFalse(num_6a!=num_6b)
		self.assertFalse(num_0a==num_6a)
		self.assertFalse(num_6b==num_0b)


	def test_equal_method_compare_primes(self):
		num_11a = Number(11, True)
		num_11b = Number(11, True)
		num_3a = Number(3, True)
		num_3b = Number(3, True)

		self.assertTrue(num_11a==num_11b)
		self.assertTrue(num_3a==num_3b)
		self.assertTrue(num_11a!=num_3a)
		self.assertTrue(num_3b!=num_11b)

		self.assertFalse(num_11a!=num_11b)
		self.assertFalse(num_3a!=num_3b)
		self.assertFalse(num_11a==num_3a)
		self.assertFalse(num_3b==num_11b)


	def test_equal_method_compare_only_is_prime(self):
		num_11a = Number(11, True)
		num_11b = Number(11, False)

		self.assertTrue(num_11a!=num_11b)
		self.assertFalse(num_11a==num_11b)



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
		self.assertFalse(0 in test_prime_set)
		self.assertFalse(6 in test_prime_set)
		self.assertFalse(10 in test_prime_set)
		self.assertFalse(91 in test_prime_set)
		


class TestNumberGen(unittest.TestCase):
	test_proper_numbers = {'num_0': Number(0, False),
							'num_1': Number(1, False),
							'num_2': Number(2, True),
							'num_3': Number(3, True),
							'num_4': Number(4, False),
							'num_5': Number(5, True),
							'num_6': Number(6, False),
							'num_7': Number(7, True),
							'num_8': Number(8, False),
							'num_9': Number(9, False),
							'num_10': Number(10, False),
							'num_89': Number(89, True),
							'num_91': Number(91, False)}

	test_wrong_numbers = {'num_0': Number(0, True),
							'num_2': Number(2, False),
							'num_3': Number(3, True),
							'num_8': Number(8, True),							
							'num_89': Number(89, False),
							'num_91': Number(91, True)}


	def test_number_objects_quality_with_single_input(self):
		test_number_gen = NumbersGen(91)
		for num in self.test_proper_numbers.values():
			self.assertTrue(num in test_number_gen.gen)

		test_number_gen = NumbersGen(91)
		for num in self.test_wrong_numbers.values():
			self.assertFalse(num in test_number_gen.gen)


	def test_number_objects_quality_with_2_attributes_input(self):
		test_numbers_gen = NumbersGen(91, 7)
		for num in [self.test_proper_numbers['num_7'],
					self.test_proper_numbers['num_8'],
					self.test_proper_numbers['num_9'],
					self.test_proper_numbers['num_10'],
					self.test_proper_numbers['num_89'],
					self.test_proper_numbers['num_91']]:
			self.assertTrue(num in test_numbers_gen.gen)

		test_numbers_gen = NumbersGen(91, 7)
		for num in [self.test_wrong_numbers['num_8'],
					self.test_wrong_numbers['num_89'],
					self.test_wrong_numbers['num_91']]:
			self.assertFalse(num in test_numbers_gen.gen)


	def test_input_start_lower_then_end(self):
		test_numbers_gen = NumbersGen(3, 10)
		self.assertFalse(list(test_numbers_gen.gen))



if __name__ == '__main__':
	unittest.main()
