class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"


class Employee(Person):
    def __init__(self, name, age, rate, num_of_hours):
        Person.__init__(self, name, age)
        self.rate = rate
        self.num_of_hours = num_of_hours

    def show_finance(self):
        return self.rate * self.num_of_hours


class Student(Person):
    def __init__(self, name, age, scholarship):
        Person.__init__(self, name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship

    #  class method has access to cls variable witch represents current Class
    @classmethod
    def create_from_string(cls, sentence):
        name, age, scholarship = sentence.split()
        age, scholarship = int(age), float(scholarship)
        if cls.is_name_correct(name):
            return cls(name, age, scholarship)

    #  static method is just a simple function, that is only useful within this class
    #  and does not change the state of the class instance
    @staticmethod
    def is_name_correct(name):
        if name[0].isupper() and len(name) > 3:
            return True
        return False


#  Multiple Inheritance
class WorkingStudent(Employee, Student):
    def __init__(self, name, age, rate, num_hours, scholarship):
        Employee.__init__(self, name, age, rate, num_hours)
        Student.__init__(self, name, age, scholarship)

    def show_finance(self):
        return self.rate * self.num_of_hours + self.scholarship


human1 = Person("John", 54)
human2 = Employee("Jack", 36, 20, 160)
human3 = Student("Agatha", 20, 9000000)
human4 = WorkingStudent("Monica", 24, 70, 550, 900000)

student_from_string = Student.create_from_string("Max 21 600")

print(human1)
print(human2)
print(human3)
print(human4)
print(student_from_string)


#  Polymorphism
def check_finance(obj):
    print(obj.show_finance())


check_finance(human2)
check_finance(human3)
check_finance(human4)
