from noAgrsPackage import fun_file as dec  # function decorator
from noAgrsPackage import class_file as dwa  # class decorator
from agrsPackage import fun_file as dwia  # function decorator
from agrsPackage import class_file as cdwia  # class decorator

def dec(fnc):
    def helper(*args):
        print("first...")
        fnc(*args)
        print("last...")
    return helper
class dwa:
    def __init__(self,name):
        self.name=name
    def __call__(self,*args):
        self.name(*args)
def dwia(name1,name2,name3):
    print(name1,name2,name3)
    def function(fnc):
        def helper(*args):
            print("first..")
            fnc(*args)
            print("last..")
        return helper
    return function

class cdiwa:
    def __init__(self,name4,name5,name6):
        self.name4=name4
        self.name5=name5
        self.name6=name6
    def __init__(self,name):
        self.name=name
    def __call__(self,*args):
            self.name(*args)



@dec.begin_end
def fun2(a, b):
    print(f"We Will win the soccer WC {a} {b}")

fun2(111, 222)




@dwa.StartStop
def fun3(x, y, z):
    print(f"Happy sunday fun3 {x} {y} {z}")


fun3(10, 20, 30)



@dwia.dec_with_arg("sachin", "Suarav", "Rahul")
def fun4(x, y):
    print(f"fun4 ..... {x} {y}")


fun4(88, 77)



@cdwia.StartStopwitharguement("Dhoni", "Kohli", "Rohith")
def fun5(x, y):
    print(f"I am from fun5 {x} {y}")


fun5(678, 567)

