#--------- Generators---------
def temp_generator():
    yield 25
    yield 30
    yield 35
my_temps = temp_generator()
print(next(my_temps))
print(next(my_temps))   
print("*" * 50) 

#---------Decorators-----------
def my_decorator(func):
    def inner_wrapper():
        print("---The start of the process---")
        func()
        print("---The end of the process---")
    return inner_wrapper
@my_decorator
def say_welcome():
    print("Welcome To The World Of Programming")
say_welcome()    
print("*" * 50)

#decorator with (*args, **kwargs)
def check_positive_num(func):
    def wrapper(*args):
        for num in args:
            if num < 0:
                print("Warning , a number has been entered in the negative.")
        func(*args)
    return wrapper
@check_positive_num
def multiply_numbers(n1, n2):
    print(f"Multiplication = {n1 * n2}")
multiply_numbers(5, -2)
print("*" * 50)                

#decorator (speed test)
from time import time
def calculate_time(func):
    def wrapper():
        start_time = time()
        func()
        end_time = time()
        print(f"{end_time - start_time}")
    return wrapper
@calculate_time
def count_to_ten_thousand():
    for i in range(1, 10000):
        pass
count_to_ten_thousand()
print("*" * 50)

#Iterable => zip()
subjects = ["Math", "Physics", "Programming"]
grades = ["Excellent", "Very Good", "Good"]
for subject, grade in zip(subjects, grades):
    print(f"Your grade in {subject} is {grade}.")
print("*" * 50)

#---------DOCSTRINGS---------
def calculate_area(length, width):
    """This function calculates the area of a rectangle.
    parameters:
    length => The length of the rectangle
    width => The width of the rectangle
    Return:
    Returns the final calculated area."""
    return length * width
print(calculate_area(2, 5))
print(calculate_area.__doc__)
help(calculate_area)
print("*" * 50)

#Errors and Exceptions and raise
def set_user_age(age):
    if age < 0 or age > 120:
        raise ValueError("Your age must be between 0, 120")
    print(f"Age was successfully recorded : {age}")
set_user_age(150)
print("*" * 50)

