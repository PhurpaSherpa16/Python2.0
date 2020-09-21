from functools import reduce

num = [1,2,3,4,5,6,7,8,9,11,12,14,16,15,21,41]
def updateEven(even): #customize function
  return even+10

even = list(filter(lambda n: n%2==0, num))# filter will only filter values
odd = list(filter(lambda o:o%2!=0, num))
square=list(map(lambda s:s*s, num)) #map will helps to update values
doubleEven = list(map(lambda e:e+2,even)) #here even is the chunk of value that we update
makingOdd = list(map(lambda e:e-1,even))
addingEvenFromCustomDef = list(map(updateEven,even)) #customize function calling in map

#reduce
def doub(a,b):
    return a*b
doubleEven = reduce(doub,even)
doubles = reduce (lambda a,b : a+b, even)

print('Even list ',even)
print('odd List ',odd)
print('Square numbers ',square)
print('Adding 2 in each even value ',doubleEven)
print('Making even to odd numbers ',makingOdd)
print('Custom function adding 2 in each ',addingEvenFromCustomDef)

print("Double while using reduce : ", doubles)
print("Custom Function Multiplying while using reduce : ", doubleEven)

