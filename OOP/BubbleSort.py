def sort(numlist):
    for i in range(len(numlist)-1,0,-1):
        for j in range(i):
            if numlist[j]>numlist[j+1]:
                temp = numlist[j]  #swap logic
                numlist[j]= numlist[j+1]
                numlist[j+1]= temp

numlist = [8,56,7,89,4,2,3,5,897,654,12,23,45,65]
result = sort(numlist)
print(numlist)