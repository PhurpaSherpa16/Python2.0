import array as arr
num = arr.array('i',[1,2,3,4,8,6,7,5])
for i in range(len(num)):
    print(num[i],end=" ") #print value with same as down but slight different
print()

for i in num:
    print(i,end=" ") # print value same but lesser code
print()

name = arr.array('u',['P','H','U','R','P','A'])
j= 0
while j<len(name):
    print(name[j],end=" ") #same but in while loop
    j+=1
print()

for a in range(len(name)):
    print(name[a],end=" ") # same code using length of array
print()

for k in name:
    print(k,end=" ") #same code but not using length
print()

#copy whole array in another array

new_num=arr.array(num.typecode,(a*a for a in num)) #copying whole and making it's square
for e in new_num:
    print(e,end=", ")
print()
ij=0
while ij<len(new_num):
    print(new_num[ij],end=" ")
    ij+=1
print()
print("Assending Numbers: ",sorted(num))
print(num)
print(num.buffer_info())
print(num.typecode)
print(len(num))