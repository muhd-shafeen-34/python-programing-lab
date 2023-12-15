class Parent():
    def func1(self):
        print("this is the first function")
class Parent2():
    def func2(self):
        print("this is the seccond function")
class child(Parent,Parent2):
    def func3(self):
        print("this is the third function")
obj1=child()
obj1.func1()
obj1.func2()
obj1.func3()

