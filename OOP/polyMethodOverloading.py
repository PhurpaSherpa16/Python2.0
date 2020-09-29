class math:
    def __init__(self,n,n1):
        self.n = n
        self.n1= n1

    def add(self,a=None,b=None,c=None):
        s = 0
        if  a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        elif a!=None:
            s= a
        else:
            return "Input in first"
        return s




a = math(5,6)
result = a.add(7,8,9)
print(result)