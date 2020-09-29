num = int(input("Enter Number you want to search "))
list = [1,2,3,4,7,5,8,9]

pos = -1
def search(list, num):
    i = 0
    while i< len(list):
        if list[i]==num:
            globals()['pos']=i
            return True
        i+=1
    return False

result = search(list,num)

if result==True:
    print("Found at ",pos+1)
else:
    print("Not Found")