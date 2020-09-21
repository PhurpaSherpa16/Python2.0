def shortList(namelist):
    short = 0
    long = 0

    for i in nameList:
        if len(i)>4:
            short+=1
        else:
            long+=1
    return long,short

shorNameList = []
longNameList= []
def nameList1(namelist):
    for i in nameList:
        if len(i)>4:
            longNameList.append(i)
        else:
            shorNameList.append(i)

popu = int(input("How many Names are there: "))
name = input("Enter Names : ")
nameList = []
nameList.append(name)
for i in range(popu-1):
    elements = input()
    nameList.append(elements)
#print(nameList)
short,long = shortList(nameList)
nameList1(nameList)
print(long,' have Long name and ',short,' have Short name.')
print('Long name list: ',longNameList,' ShortName list : ',shorNameList)


