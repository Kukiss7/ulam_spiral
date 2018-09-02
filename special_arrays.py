import numpy as np


class SquareArray(np.ndarray):
    """ Square shaped array with sides lengths of given "size" """


    def __new__(subtype, size, dtype=float, buffer=None, offset=0,
                strides=None, order=None):
        """ 
        Inheritance is based on example from numpy documantation
        https://docs.scipy.org/doc/numpy-1.13.0/user/basics.subclassing.html

        Create the ndarray instance of SquareArray type, given the usual
        ndarray input arguments except shape, where square shaped 2d array is given
        with int number as its lengths. 
        This will call the standard ndarray constructor and return an object of new type.

        size: int
        """

        obj = super(SquareArray, subtype).__new__(subtype, shape=(size, size), 
                                                dtype=dtype, buffer=buffer, offset=offset, 
                                                strides=strides, order=order)
        return obj


class SpiralArray(SquareArray):
    """
    Generates square shaped array with numbers positioned from center to the outside
    in a spiral path. Numbers are stored as np.int32 type and start with given start
    value. Highest value is always positioned in bottom right corner

    size: int; will be automatically changed to odd number (if %2==0: size +=1)
    start: int
    self.halved_size if often used in calculations in several methods
    """


    def __new__(subtype, size, start=1, dtype='int32'):

        def odd_number(number):
            """ Returns odd number """
            if number % 2 == 0:
                number += 1
            return number


        odd_size = odd_number(size)


        obj = super(SpiralArray, subtype).__new__(subtype, size=odd_size, dtype=dtype)


        obj.start = start
        obj.halved_size = odd_size // 2
        obj.fill()

        return obj


    def fill(self):
        """ 
        Fills self with numbers
        Firstly the center cell is filled with start value
        Then the main loop iterates through the array from the center to the outside
        In every iteration one layer is filled divided in four quaters 
        (in order: right, top, left, bottom)

        T T T T R   where:  C - Center
        L T T R R           T - Top
        L L C R R           L - Left    
        L L B B R           R - Right
        L B B B B           B - Bottom
        """
        axes = ('column', 'row')
        orders = (-1, 1)
        self._set_center_value()
        for layer in range(1, self.halved_size+1):
            splitted_layer_arrays = np.split(self._calculate_layer(layer),4)
            self._fill_quarter(layer, axes[0], orders[0], splitted_layer_arrays[0])
            self._fill_quarter(layer, axes[1], orders[0], splitted_layer_arrays[1])
            self._fill_quarter(layer, axes[0], orders[1], splitted_layer_arrays[2])
            self._fill_quarter(layer, axes[1], orders[1], splitted_layer_arrays[3])


    def _set_center_value(self):
        """ Fills center cell with start value """
        self[self.halved_size, self.halved_size] = self.start


    def _calculate_layer(self, layer):
        """ 
        Calculates range of numbers included in given layer
        Returns np.arange array
        """
        layer_start_number = self.start + (layer*2-1)**2
        layer_end_number = self.start + (layer*2+1)**2
        layer_array = np.arange(layer_start_number, layer_end_number)
        return layer_array


    def _fill_quarter(self, layer, axis, order, quarter_array):
        """
        Fills given part (column or row) of self.array with given numbers
        with needed order. Exceptions are found in final steps when trying to rich
        boundary cells and put values in descending order
        """
        if axis == 'column':
            try:
                self[self.halved_size-order*layer+order:self.halved_size+order*layer+order:order,
                     self.halved_size-order*layer] = quarter_array
            except ValueError:
                self[self.halved_size+layer-1::-1,
                     self.halved_size+layer] = quarter_array
        else:
            try:
                self[self.halved_size+layer*order,
                     self.halved_size-order*layer+order:self.halved_size+order*layer+order:order] = quarter_array
            except ValueError:
                self[self.halved_size+layer*order,
                     self.halved_size+layer-1::-1] = quarter_array



class FilteredArray(np.ndarray):
    """ 
    Adter operation: type of np.ndarray with boolean values

    Takes an array and a container with data i.e. set
    Iterates through given array and marks if concerned element is in provided container
    Updates self with boolean data of this operation

    input_array = any np.ndarray or object that can be interpreted
                  as np.ndarray with np.asarray method

    true_set = data container to check if some data is in it
    """


    def __new__(cls, input_array, true_set):
        obj = np.asarray(input_array).view(cls)


        obj = obj.is_in_true_set(true_set)
        return obj
        

    def is_in_true_set(self, true_set):
        """ 
        Iterates through self values and maps if given value 
        can be found in provided true_set container

        Before this process self's data is the same as in provided array
        After this  process self is an array with boolean data
        """
        print(type(self))
        is_in_true_set = lambda n: n in true_set
        vfunc = np.vectorize(is_in_true_set)
        return vfunc(self)


if __name__ == '__main__':
    from prime_numbers import PrimesSet

    
    primes_set = PrimesSet(49)
    primes_set.build_primes_set()
    spiral = SpiralArray(7, 1)
    marked_primes = FilteredArray(spiral, primes_set)


    print(f'Spiral with integers:\n\n{spiral}')
    print('\n\n')
    print(f'The same spiral with marked prime numbers:\n\n{marked_primes}')