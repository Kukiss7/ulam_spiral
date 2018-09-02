from prime_numbers import PrimesSet
from special_arrays import SquareArray, SpiralArray
import numpy as np
import unittest


class TestSquareArray(unittest.TestCase):
	def setUp(self):
		self.square_int = SquareArray(7, 'int32')
		self.square_bool = SquareArray(10, 'bool')


	def test_is_square(self):
		self.assertEqual(self.square_int.shape[0], self.square_int.shape[1])		
		self.assertEqual(self.square_bool.shape[0], self.square_bool.shape[1])


class TestSpiralArray(unittest.TestCase):
	def setUp(self):
		self.spiral_array = SpiralArray(4, 2)
		self.spiral_array.fill()


	def test_array_data_type(self):
		self.assertEqual(self.spiral_array.dtype, 'int32')


	def test_arrays_shape(self):
		""" 
		Array should always be square shaped with odd size
		In setUp size was set to 4, it should be automatically changed to 5
		"""
		self.assertEqual(self.spiral_array.shape, (5,5))


	def test_proper_values_in_array(self):
		proper_result = np.array([18, 17, 16, 15, 14, 19, 6, 5,\
				 				  4, 13, 20, 7, 2, 3, 12, 21, 8,\
				 				  9, 10,11, 22 ,23, 24, 25, 26])
		proper_result.resize(5,5)
		self.assertEqual(self.spiral_array.tolist(), proper_result.tolist())


class TestFilteredArray(unittest.TestCase):
	pass # TODO


if __name__ == '__main__':
	unittest.main()
