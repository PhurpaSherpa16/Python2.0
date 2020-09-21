class Comparision:

    def __init__(self):
        self.age = 30
        self.name = "Phurpa"
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Comparision()
c1.age = 31
c2 = Comparision()
c2.name = "Rita"

if c1.compare(c2):
    print("they are same age")
else:
    print("they are different age")

print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)