# python inheritance is simply the meaning of the name.
# so we have child class that allows us to define  a class to inherit from the a parent class 

#PARENT CLASS
class Person:
    def __init__(self, fname, lname, age):
        self.firstname =fname 
        self.lastname = lname
        self.age = age
    def xtics(self):
        print(self.firstname, self.lastname, self.age)

x = Person("Musa", "John", 17)
x.xtics()

# to create the child class 
# class Student(Person):
#     pass #for when you dont want it to get its own characteristics
class Student(Person):
    def __init__(self, name, tname, age):
        Person.__init__(name, tname, age)
        # readup on super methods for init. you dont need the self

x = Student("Ayo", "Adeleke", 20)
x.xtics()