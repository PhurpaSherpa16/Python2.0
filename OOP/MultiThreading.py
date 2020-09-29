#it will help to run the program paralley
import time as t
import threading as th
class Hi(th.Thread):
    def run(self):
        for i in range(5):
            print("hi")
            t.sleep(1)

class Hello(th.Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            t.sleep(1)

obj = Hi()
obj1 = Hello()
obj.start()
t.sleep(0.2)
obj1.start()
obj.join() #this will allow this object code execute
obj1.join()#this will allow this object execute
print("Bye")# the execute this print

"""class Hi1():
    def run(self):
        print("hi1")
        t.sleep(1)

class Hello1():
    def run(self):
        for i in range(5):
            print("Hello1")
            t.sleep(1)

obj2 = Hi1()
obj3 = Hello1()
obj2.run()
t.sleep(1)
obj3.run()
"""