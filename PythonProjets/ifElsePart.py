a = input("Enter First Number:")
b = input("Enter Second Number:")
c = input("Enter Third Number:")
x,y,z = int(a),int(b),int(c)
i = 1
if x>y:
    if x>z:
        print("First Number is greater among all")
        while i<=x:
            print(i)
            i+=1
    else:
        print("Third Number is greater among all")
        while i<=z:
            print(i)
            i+=1
elif y>x:
    if y>z:
        print("Second Number is greater among all")
        while i<=y:
            print(i)
            i+=1
    else:
        print("Third Number is greater among all")
        while i<=z:
            print(i)
            i+=1
else:
    print("Worng Input")


x=int(input('enter first number:'))
y=int(input('enter second number:'))
z=int(input('enter third number:'))
num=[x,y,z]
print(max(num))
