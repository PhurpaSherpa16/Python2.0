import math
x = int(input("Enter Number:"))
for i in range(x):
    if i%5!=0:
        print(i)

for j in range(30,x+1,+1):
    print(j)

for k in range(x,50):
    x = math.sqrt(k)
    if k%x==0:
        print(k)
