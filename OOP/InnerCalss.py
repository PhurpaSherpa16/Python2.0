#inncer calss
class student:

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def show(self):
        print("Name is ",self.name," and roll is ",self.roll,".")

    class ComputerDetails:
        def __init__(self,brand,processor,RAM):
            self.brand = brand
            self.proccessor = processor
            self.ram = RAM

        def show(self):
            print("Laptop Brand Name is ",self.brand,". Processor is ",self.proccessor," and it has ",self.ram," of RAM.")

name = input("Enter Name : ")
roll = input("Enter Roll No. : ")
brand = input("Enter Laptop brand: ")
processor = input("Enter Procesor: ")
ram = input("Enter Ram : ")

studentDetailsPArse = student(name,roll) #studentDetailsPArse is a object which call student class
LaptopDetailsPArse = student.ComputerDetails(brand,processor,ram) #LaptopDetailsPArse parse the value in inncer calss
studentDetailsPArse.show()
LaptopDetailsPArse.show()


