'''
import mymodule

#mymodule.greeting("Aman")

a = mymodule.person1
print(a)

'''

'''
Renaming module
import mymodule as mn

a = mn.person1
print(a)


#built-in module
import platform
x = platform.system()
print(x)
x = dir(platform)
print(x)


'''



import numpy as np

array2d = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9 ,10, 11, 12]])

two_2d_to_3darray = array2d.reshape(3, 2, 2)
print(two_2d_to_3darray)
