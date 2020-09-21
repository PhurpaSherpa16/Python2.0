from array import *
arr = array('i',[])
length = int(input("Enter the desire length of array: "))

for i in range(length):
    value = int(input("Enter the Value:"))
    arr.append(value)

print(arr)
arr.pop(1)#delete item index no1
arr.remove(4)#remove the no which is parse it can be done in string
print(arr)
searchValue = int(input("Enter search Number: "))
inde=0
for e in arr:
    if  e==searchValue:
        print(inde)
        break
    inde+=1
print(arr.index(searchValue))