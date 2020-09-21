#import datetime
#today = datetime.datetime.now()
#print(str(today))
#print(repr(today))
l1, l2, n = 100, 200, 13
j = l1
while j < l2:
    if j%n == 0:print(repr(j) + ', ')
    j += 1



