import numpy
from numpy import *
multiArr= array([[1,2,3,4,5,6],[4,5,6,7,8,9]])
print(multiArr)
print("Dimension of array ",multiArr.ndim) #it will show the types of dimension like 2D,3D etc
print("Shape of array ",multiArr.shape)#it will show the rows and column number
print("Size of array ",multiArr.size) # it will show the number of elements present in array
multiArr1= multiArr.flatten() #it will convert 2D to 1D
print(multiArr1)

newarr = multiArr1.reshape(2,2,3) #it will convert into desire Dimesnion matrix , (number of dimesion into parts, rows and column)
print(newarr)

m = matrix('1 2 3;3 4 5;5 6 7') #converting array into matrix
print(m.diagonal())
print(m.min())