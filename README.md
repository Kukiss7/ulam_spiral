Project's aim was to visualize Ulam spiral (graphical depiction of the set of prime numbers)

Python 3.66 was used here along with numpy and matplotlib libraries


Results can be seen with matplotlib.pyplot by launching **ulam_spiral_array.py** file


Short description.

While project runs, it:

 - makes 2 square arrays

 - fills first array with integers from center to outside in a spiral path

 - builds up set with prime numbers

 - fills second (main) array while mapping first array and trying to find numbers in primes set

 - finally second array with boolean data is visualised with pyplot, where every True/False information 
   corresponds to one pixel in the picture


Interesting example with start number 41 and size 200:

![Results exaple](/example/start_41size_200.png)

Format: ![Alt Text](url)