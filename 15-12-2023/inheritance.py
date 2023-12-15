class Person(object):
    def __init__(self,name,ids):
        self.name = name
        self.ids = ids
    def display(self):
        print(self.name,self.ids)
emp = Person("Anu",102)
emp.display()
class Emp(Person):
    def show(self):
        print("emp class called")
emp_details = Emp("manu",103)
emp_details.display()
emp_details.show()
