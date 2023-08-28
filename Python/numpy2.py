#taking an array and print an array of its odd rows and even columns
import numpy as np
a=np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], 
[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
print("printing input array:\n",a)
b=np.array([[a[0,1],a[0,3]],[a[2,1],a[2,3]],[a[4,1],a[4,3]]])
print("printing array of odd rows and even columns:\n",b)