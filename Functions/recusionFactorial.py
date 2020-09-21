num = int(input("Enter Number: "))
def fact(num):#recursion function
     if num==0:
         return 1
     return num*(fact(num-1))

result = fact(num)
print(result)