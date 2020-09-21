def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd

lst = []
number = int(input("How many numbers Do you want to input:"))
for i in range(number):
    ele = int(input())
    lst.append(ele)
even,odd = count(lst)

print('There are ',even,' Even and ',odd,' numbers of odd')





