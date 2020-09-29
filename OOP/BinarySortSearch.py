num = int(input("Enter Number: "))
l = [1,2,34,5,6,85,69,5,4,7,62,58,10,30,63,89,455,223,14]
l.sort()
pos = -1
def search(list, num):
    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u)//2

        if list[mid]==num:
            globals()['pos']= mid
            return True
        else:
            if list[mid]<num:
                l = mid+1
            else:
                u = mid+1
    return False

result = search(l,num)
if result == True:
    print("Found", pos+1)
else:
    print("Not found")