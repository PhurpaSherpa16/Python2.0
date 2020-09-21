from numpy import *
import array as arr
a = array([18,16,20,40,6,94])
b = array([45,20,30,40,21,2,404])
c = arr.array('i',[1,2])
a = append(a,[404]) #adding value in array
print(a)
print(a+b, end=" adding both array and b") #adding a and b
print()
print(a+5,end=" Sum by 5 in each") #adding 5 in each
print()
print("sum of all A array elements is ",sum(a))
print("Square of A elements is ",sqrt(a))
print("Minimum value of A is ", min(a))
print("Maximum value of A is ", max(a))
print("Average value of A is ", mean(a))
print("Middle value is ",median(a))
print("Sorted value is ", sorted(a))
print("Joining two Arrays ",concatenate([a,b]))

num = array([1,2,3,4])
num2 = num.view() #view will create a different address in memory though copy of arry is same it called shallo copy it means updating source effec can be find in branch
num2 = num.copy() # it will copy but updating source, effect will not seen in branch it called deep copy
num[1]=7 #it will update the value
print(num)
print(num2)
print(id(num))
print(id(num2))