#take 2 arrays randomly and compare if they are equal
import numpy as np
A = np.random.randint(0,5,2)#between 0 to 5, we will randomly take 2 numbers
print("First array:")
print(A)
B = np.random.randint(0,5,2)
print("Second array:")
print(B)
print("Test above two arrays are equal or not!")
array_equal = np.allclose(A, B)#allclose() method compares 2 array
print(array_equal)