#w = write, a= append , r =read
def write():
    createFile = open('MyData1', 'w')
    createFile.write("Hello we write data here")

def append():
    append = open('MyData1', 'a')
    append.write(". Work Succesfully\n")

def read():
    f1 = open('MyData1','r')
    print(f1.read())

def copyData():
    f = open('Mydata', 'r')
    f1 = open('MyData1', 'a')
    for data in f:
        f1.write(data)


write()
append()
copyData()
read()





