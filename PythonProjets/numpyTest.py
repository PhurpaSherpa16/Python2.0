from numpy import *
#suming two arrays
a = array([1,2,3,4])
b = array(([2,4,6,8]))
c = array([])
for i in range(len(a)):
    c = a+b
    break
print(c)
#finding max value
d = array([10,40,52,4,-6])
max_val=0
for i in d:
    if max_val<i:
        max_val=i
print(max_val)

# finding minimum value
min_val = 0
for i in d:
    if min_val>i:
        min_val=i
print(min_val)