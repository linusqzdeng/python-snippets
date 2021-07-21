from o3 import Human

class Student(Human):
    def __init__(self, age, name):
        self.name = name
        self.age = age

student1 = Student(23, "Linus")
print(student1.name)
print(student1.age)
print(Student.sum)
student1.get_name()
