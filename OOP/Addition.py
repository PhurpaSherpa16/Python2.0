import AddLogic as a
num = int(input("Enter Number: "))
num2 = int(input("Enter Number: "))
result = a.AddLogic() #or you can parse arguments in class direct, and you need to use __init__method in other class
#result = a.AddLogic(num,num2)
#final = result.sum()
final = result.sum(num,num2)
print("Sum is ",final)



