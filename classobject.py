
from sys import stdin


class Person(  ):
    """docstring for Person."""
    def __init__(self, name, age):
        self.name = name
        self.age =  age
        
    def show(self):
        print("my name is ", self.name)
        print("my age is ", self.age)

    def set_school(self, school):
        self.school = school
    
    def get_school(self):
        return self.school

# demo_p1 = Person("kajol", 22)
# demo_p2 = Person("renuka", 25)

# demo_p2.set_school("Oxford")

# print(demo_p1.show())
# print(demo_p2.age)

# print(demo_p2.get_school())

''' Input from argument'''
in_a = input("enter name and age ").partition(" ")
inp_cus = Person(in_a[0], in_a[2])
inp_cus.show()
