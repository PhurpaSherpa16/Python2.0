for i in range(1,50):
    if i%5==0 or i%3==0:
        continue #it will skip the above result number
    print(i)

print()

for i in range(1,50):
    if i%5==0 and i%3==0:
        print(i) #it will print ony the value divisible by both.
print()

for i in range(1,50):
    if i%2!=0:
        pass # it will pass this block to another
    else:
        print(i)