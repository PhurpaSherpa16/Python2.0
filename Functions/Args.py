def person(name,age=18):#formal arguments
    print("My name is ",name,end=". ")
    print("I'm ", age, " old.")

#person('Phurpa',25) #actual arguments, #actual arguments have 4 types
#postion
#person(name='Phurpa',age=25) #keyword arguments
person("Phurpa") #defult, as we can see age is not parse but in function it's set 18 as default.
#variable length is the types where arguments are not fixed
def sum(*b):
    c = 0
    for  i in b:
        c = c+i
    print(c)
sum(5,6,7,8,9)

#variable length
nam = input("Whats your name? ")
ag = input("whats your age?" )
addr= input("whats your address? ")

def personal_details(*b):
    c = 0
    for i in b:
        print(nam)
        print(ag)
        print(addr)
        break

personal_details(nam,ag,addr)


#key word variable length

def details(name, **data): # ** means key word and un fixed variable parse
    print(name)
    for i,j in data.items():
        print(i,' is ', j,'.')

details("Phurpa",age=25,address="KTM",mobile="9813")



