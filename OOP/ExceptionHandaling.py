try:
    a = int(input("Enter Number: ")) #to catch eror statement should be written in try block
    b = int(input("Enter Number: "))
    print("resource open")
    print(a/b)
except ZeroDivisionError as e: #handle only zero divission error
    print("You cannot divide by zero")
    print(e) #message given by machine
except ValueError as f: #handle only value error
    print("You need to input numbers")
    print(f)
except Exception as g: # this will handel all the errors but with same messages
    print("Invalid Inputs")
finally:
    print("resource close")
print("Bye")
