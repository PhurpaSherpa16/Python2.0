#ways of defining arrays in numpy
from numpy import *
array1=array([1,2,3,4])
print(array1)

array2=linspace(0,10,2) #(Start,Range,Parts) #this will print the all part as defines

array3 = arange(0,10,2) #(Start,Range,Space) this will jump number as define in space
array4 = zeros(5,int) #(range)it will create all the 5 number zeros
print(array4)
print(array2)
print(array3)
print(array2.dtype)