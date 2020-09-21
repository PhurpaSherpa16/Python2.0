

for i in range(8):
    print(i*"# ")
    i+=1
for i in range(9):
    print(i*"# ")
    i+=1

for i in range(7):
    for j in range(i):
        print("# ",end="")
    print()
for i in range(4,0,-1):
    print(i*("# "))
for i in range(8):
    for j in range(8-i):
        print("# ",end="")
    print()
