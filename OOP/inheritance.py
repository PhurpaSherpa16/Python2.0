class GrandParents:
    def name1(self):
        print("GrandParents is Kami")
    def cast1(self):
        print("Cast is Sherpa")

class Fathername:
    def name2(self):
        print("Father is Kami")
    def cast2(self):
        print("Cast is Sherpa")
    def location(self):
        print("Living in Dhading")

class Mother(Fathername):#single inheritance
    def name4(self):
        print("Name Putali maya")

class me(GrandParents, Fathername): #multiple inheritance by using , in betweeen
    def name3(self):
        print("My name is Phurpa")

mydetaisl = me()
mydetaisl.name3()
mydetaisl.cast1()
mydetaisl.location()

motherdetails = Mother()
motherdetails.name4()
motherdetails.cast2()
motherdetails.location()
