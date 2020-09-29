#method over riding is simple, it that until you have ur own function which behave you will use parent class behaviour
class A:
    def show(self):
        print("This is A show")

class B(A): # it don't have its own behaviour so it inherite from super class
    pass

class C(A): # thouh it inherit from super class it create it's own behaviour
    def show(self):
        print("This is C Show")

c = B()
c.show()
d = C()
d.show()
#these are called method over riding