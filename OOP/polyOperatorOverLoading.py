#over loading means altering inbuilt operator like add, sub, greater than etc as we desire
class student:
    def __init__(self,m1,m2,m3):
        self.m1= m1
        self.m2 = m2
        self.m3 = m3

    def __add__(self, other): #adding two numbers #this is also a inbuilt operator
        m1 = self.m1+other.m1
        m2 = self.m2+other.m2
        m3 = self.m3+other.m3
        s3 = student(m1,m2,m3)

        return s3

    def __gt__(self, other): #it's a inbuilt operator whihc is alter as desire
        s1 = self.m1+self.m2
        s2 = other.m1+other.m2

        if s1>s2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {} {}'.format(self.m1, self.m2, self.m3) #for tuple displaying


s1 = student(41,45,50)
s2 = student(65,55,60)
s3 = s1+s2
print(s3.m1)
print(s3.m2)

if s1>s2:
    print("S1 wins")
else:
    print("S2 wins")

print(s3)