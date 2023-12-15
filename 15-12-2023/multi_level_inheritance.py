class Parent():
    def func1(self):
        print("this is first function")
class child(Parent):
    def func2(self):
        print("this is seccond function")
class child2(child):
    def func3(self):
        print("this is the third function")
obj1=child2()
obj1.func1()
obj1.func2()
obj1.func3()

