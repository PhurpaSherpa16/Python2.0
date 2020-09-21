list  = ['Apple','Ball','Cat','Mango','Papaya','Carrot','Ap']
longlist = []
shortlist= []
def lengthNameList(list):
    for i in list:
        if len(i)<4:
            shortlist.append(i)
        else:
            longlist.append(i)


lengthNameList(list)
print(longlist)
print(shortlist)

