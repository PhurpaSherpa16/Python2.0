num = int(input("Enter Number: "))

f = lambda a : a*a #lambda function only use for one experession
add = lambda a,b:a+b
print('Square ',f(num))
result = add(5,6)
print("Adding ", result)
