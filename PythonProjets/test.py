a = int(input("Enter Numbers : "))
i = 1
while i<=a:
    if i%3!=0 or i%5!=0:
        print(i)
    i+=1


j = 1
while j<=a:
    z = j
    while z<=a:
        print(z,end=" ")
        z+=1
    j+=1
    print()
