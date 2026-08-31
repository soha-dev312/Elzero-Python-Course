class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    # Getter
    def get_grade(self):
        return self.__grade

    # Setter
    def set_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
        else:
            print("Invalid Grade!")
s = student1 = Student("Ali", 85)
print(s.get_grade())
s.set_grade(95)
print(s.get_grade())
        