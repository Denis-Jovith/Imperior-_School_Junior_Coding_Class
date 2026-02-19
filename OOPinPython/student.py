#file name is student.py

#Create class
class Student:
    def _init_(self, name, age):
        self.name = name
        self.age = age

#method
def display(self):
    print("Name: ", self.name)
    print("Age: ", self.age)

#creating object
s1= Student("Denis", 22)

#call method
s1.display()