num = int(input("Enter Number: "))
list=[1,2,3,4,5,6,7,8,9,10]
pos = -1
def search(list,num):
    for i in range(len(list)):
        if list[i]==num:
            globals()['pos']=i
            return True
    return False

if search(list,num):
    print("Found at ", pos+1)
else:
    print("Not Found")


