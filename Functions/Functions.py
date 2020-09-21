def sum(a, b):
    c = a + b
    return c


def sub(a, b):
    c = a - b
    return c


num = int(input("Enter the Number "))
num2 = int(input("Enter another Number "))
sign = input("Enter sign ")
if sign == "+":
    add = sum(num, num2)
    print("Sum is ", add)
elif sign == "-":
    subt = sub(num, num2)
    print("Subtraction is ", subt)
else:
    print("You have input wrong sign")
