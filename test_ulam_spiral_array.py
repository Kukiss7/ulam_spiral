from prime_numbers import PrimesSet
from ulam_spiral_array import SquareArray, SpiralArray, UlamSpiralArray
import numpy as np
import unittest



class TestSqaureArray(unittest.TestCase):
	def setUp(self):
		self.square_int = SquareArray(7, 'int32')
		self.square_bool = SquareArray(11, 'bool')


	def test_is_square(self):
		self.assertEqual(self.square_int.array.shape[0], self.square_int.array.shape[1])		
		self.assertEqual(self.square_bool.array.shape[0], self.square_bool.array.shape[1])


	def test_attribute_odd_size(self):
		self.assertEqual(self.square_int.odd_size%2, 1)
		self.assertEqual(self.square_bool.odd_size%2, 1)


class TestSpiralArray(unittest.TestCase):
	def setUp(self):
		self.spiral_array = SpiralArray(4, 2)
		self.spiral_array.fill()


	def test_array_data_type(self):
		self.assertEqual(self.spiral_array.dtype, 'int32')


	def test_arrays_shape(self):
		""" shape should always have odd numbers
		"""
		self.assertEqual(self.spiral_array.array.shape, (5,5))


	def test_proper_values_in_array(self):
		proper_result = np.array([18, 17, 16, 15, 14, 19, 6, 5, 4, \
								  13, 20, 7, 2, 3, 12, 21, 8, 9, 10,\
								  11, 22 ,23, 24, 25, 26])
		proper_result.resize(5,5)
		self.assertEqual(self.spiral_array.array.tolist(), proper_result.tolist())


class TestUlamSpiralArray(unittest.TestCase):
	def setUp(self):
		self.ulam_spiral_array = UlamSpiralArray(3, 1)
		self.ulam_spiral_array.fill_integers()
		self.ulam_spiral_array.mark_primes()


	def test_array_data_type(self):
		self.assertEqual(self.ulam_spiral_array.dtype, 'bool')


	def test_proper_values_in_array(self):
		proper_result = np.array([True, False, True, False, False, True, True, False, False])
		proper_result.resize(3,3)
		self.assertEqual(self.ulam_spiral_array.array.tolist(), proper_result.tolist())



if __name__ == '__main__':
	unittest.main()
