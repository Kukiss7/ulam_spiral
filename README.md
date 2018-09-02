Project's aim was to visualize Ulam spiral (graphical depiction of the set of prime numbers)

Python 3.66 was used here along with numpy and matplotlib libraries


Results can be seen with matplotlib.pyplot by launching **arrays_manage.py** file



While project runs, it:

 - makes first square array which is filled with integers from center to outside in a spiral path

 - builds up set with prime numbers

 - second array is created that maps previous one's data with information whether given number was a prime or not

 - finally second array with boolean data is visualized with pyplot, where every True/False information 
   corresponds to one pixel in the picture


Interesting example with start number 41 and size 200:

![Results exaple](/example/start_41size_200.png)