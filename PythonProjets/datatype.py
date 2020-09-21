a = ['apple','cat'] #list
b =('apple','cat') #tuple
c ={'apple','cat'} #set
d = {
    "name":"apple",
    "food":"cat"
} #dictionaries
print(a)
print(b)
print(c)
d.update([("type","fruit"),("age",9)])
for x,y in d.items():
    print(x+"="+y)