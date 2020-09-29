class super:
    def __init__(self):
        print("Super init features")
    def feature1(self):
        print("Fetaure 1 is working")

    def feature2(self):
        print("Fetaure 2 is working")

class subClass(super):
    def __init__(self):
        print("SubClass Init features")
        super.__init__(self) #super will helps to call any function

    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

a = subClass()