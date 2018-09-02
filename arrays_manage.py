from prime_numbers import PrimesSet
from special_arrays import SquareArray, SpiralArray, FilteredArray

class UlamSpiralBuilder:
    """
    Sequence of processes needed to provide the base for Ulam Spiral array

    With SpiralArray object there is made a path with integers from a center
    to the outside of an array. 

    Prime numbers are calculated with PrimesSet in self.primes_set variable. 

    Finaly self self.ulam_spiral_array is a spiral array with marked 
    prime(True) and composite(False) numbers
    """


    def __init__(self, size, start):
        self.start = start
        self.size = size
        self.spiral_array = SpiralArray(size=self.size, start=self.start)
        self.max_value = self.start + (self.size)**2 - 1
        self.primes_set = PrimesSet(self.max_value)
        self.primes_set.build_primes_set()
        self.ulam_spiral_array = FilteredArray(self.spiral_array, self.primes_set)


if __name__ == '__main__':

    from matplotlib import pyplot

    us_base = UlamSpiralBuilder(size=150, start=1)

    pyplot.figure(figsize=(5, 5))
    pyplot.imshow(us_base.ulam_spiral_array, cmap=pyplot.cm.cool, interpolation='nearest')
    pyplot.xticks([]), pyplot.yticks([])
    pyplot.show()