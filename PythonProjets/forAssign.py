for j in range(5):
    for i in range(j+1,5):
        print(i,end=" ")
    print()

s = 'ABCD'
b = 'PQR'

for i in range(4):
    print(s[:i+1]+b[:i])

l = ['A','B','C','D','P','Q','R']
for i in range(4):
    for j in range(4):
        if j<=i:
            print(l[j],end=" ")
        else:
            print(l[j+3],end=" ")
    print()

