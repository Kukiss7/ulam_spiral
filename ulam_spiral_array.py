from prime_numbers import PrimesSet
import numpy as np


class SquareArray:
	""" 
		Base for UlamSpiralArray and SpiralArray classes
		Represents 2d array with with equal sides lengths
		Must have an odd size, if given even number, 1 is added to provide it

		size: int
		dtype: np.dtype
		start: int; center (start point number) of the spiral
		odd_size: int; size ensured to be odd
		halved_size: int; odd_size // 2 very often used in calculations
	"""
	def __init__(self, size, dtype, start=1):
		self.size = size
		self.dtype = dtype
		self.start = start
		self.odd_size = SquareArray.odd_number(self.size)
		self.array = self.set_array()
		self.halved_size = self.odd_size // 2


	def __str__(self):
		return str(self.array)


	def set_array(self):
		""" Creates zeros array with square shape and given dtype
		"""
		array = np.zeros((self.odd_size, self.odd_size), dtype=self.dtype)
		return array


	@staticmethod
	def odd_number(number):
		""" Checks provided size, adds +1 to its value if it's even number
			returns odd number
		"""
		if number % 2 == 0:
			number += 1
		return number


class SpiralArray(SquareArray):
	"""
		Generates array with numbers positioned from center to outside in a spiral path
		Numbers are stored as np.int32 type and start with given start value
		Hghest value is always positioned in bottom right corner
		size: int
		start: int
	"""
	def __init__(self, size, start):
		super().__init__(size, dtype='int32', start=start)


	def fill(self):
		""" 
			Fills self.array with numbers
			Firstly the center cell is filled with start value
			Then the main loop iterates through the array from the center to the outside
			In every iteration one layer is filled divided in four quaters (in order: right, top, left, bottom)

			T T T T R   where:  C - Center
			L T T R R 			T - Top
			L L C R R 			L - Left	
			L L B B R   		R - Right
			L B B B B   		B - Bottom
		"""
		axes = ('column', 'row')
		orders = (-1, 1)
		self.set_center_value()
		for layer in range(1, self.halved_size+1):
			splitted_layer_arrays = np.split(self.calculate_layer(layer),4)
			self.fill_quarter(layer, axes[0], orders[0], splitted_layer_arrays[0])
			self.fill_quarter(layer, axes[1], orders[0], splitted_layer_arrays[1])
			self.fill_quarter(layer, axes[0], orders[1], splitted_layer_arrays[2])
			self.fill_quarter(layer, axes[1], orders[1], splitted_layer_arrays[3])


	def set_center_value(self):
		""" Fills center cell with start value
		"""
		self.array[self.halved_size, self.halved_size] = self.start


	def calculate_layer(self, layer):
		""" Calculates range of numbers included in given layer
			Returns np.arange array
		"""
		start_number = self.start + (layer*2-1)**2
		end_number = self.start + (layer*2+1)**2
		layer_array = np.arange(start_number, end_number)
		return layer_array


	def fill_quarter(self, layer, axis, order, quarter_array):
		"""
			Fills given part (column or row) of self.array with given numbers, with needed order
			exceptions are found in final steps when trying to rich boundary cells and put values in descending order
		"""
		if axis == 'column':
			try:
				self.array[self.halved_size-order*layer+order:self.halved_size+order*layer+order:order,
						   self.halved_size-order*layer] = quarter_array
			except ValueError:
				self.array[self.halved_size+layer-1::-1,
						   self.halved_size+layer] = quarter_array
		else:
			try:
				self.array[self.halved_size+layer*order,
						   self.halved_size-order*layer+order:self.halved_size+order*layer+order:order] = quarter_array
			except ValueError:
				self.array[self.halved_size+layer*order,
						   self.halved_size+layer-1::-1] = quarter_array



class UlamSpiralArray(SquareArray):
	""" 
		Generates an array as a base for Ulam Spiral visualisation

		Based on spirally positioned numbers in self.SpiralArray object it marks in 
		self.array only if given number is a prime number or not. Does it by comparing it with 
		generated earlier set with primes in PrimesSet object

		Data is hold as np.bool type

		attributes:
		max_value: int; max value found in spiral (bottom right) - quickly calculated
				   not taken from generated array
		primes_set: PrimesSet object
		spiral_array: SpiralArray object
	"""
	def __init__(self, size, start=0):
		super().__init__(size, start=start, dtype='bool')
		self.max_value = self.start + (self.size+1)**2 - 1
		self.primes_set = PrimesSet(self.max_value)
		self.primes_set.build_primes_set()
		self.spiral_array = SpiralArray(self.size, start=self.start)


	def fill_integers(self):
		""" Builds up self.spiral_array object with integers
		"""
		self.spiral_array.fill()


	def mark_primes(self):
		""" Builds up self.array with marked prime numbers
		"""
		is_prime = lambda n: n in self.primes_set
		vfunc = np.vectorize(is_prime)
		self.array = vfunc(self.spiral_array.array)


if __name__ == '__main__':

	from matplotlib import pyplot

	start = 41
	size = 200
	ulam_spiral = UlamSpiralArray(size, start)
	ulam_spiral.fill_integers()
	ulam_spiral.mark_primes()
	pyplot.figure(figsize=(5, 5))
	pyplot.imshow(ulam_spiral.array, cmap=pyplot.cm.winter, interpolation='nearest')
	pyplot.xticks([]), pyplot.yticks([])
	pyplot.show()