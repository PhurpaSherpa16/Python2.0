name = input("Enter Name: ")
NameList = ["Phurpa","Sherpa","Harry","Carry","Mandy","Sandy","Mary"]
name1 = name.lower()
list1 = [x.lower() for x in NameList]
pos = -1
def searchName(list1,name1):
    for i in range(len(NameList)):
        if list1[i]==name1:
            globals()['pos']=i
            return True
    return False

result = searchName(list1,name1)
if result==True:
    print(name," name found which is at ",pos+1)
else:
    print("Not Found")