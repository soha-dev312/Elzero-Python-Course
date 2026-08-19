#Built in Function Part2
#1.map()
subjects = ["python", "c++", "data analytics"]
def make_upper(text):
    return text.upper()
result = map(make_upper, subjects)
print(list(result))
print("#" * 50)

#2.filter()
scores = [45, 80, 30, 95, 50, 20]
def is_passed (score):
    return score >= 50
passed_scores = filter(is_passed, scores)
print(list(passed_scores))
print("#" * 50)

#3.reduce()
from functools import reduce
numbers = [1, 2, 3, 4]
def multiply (n1, n2):
    return n1 * n2
result = reduce(multiply, numbers)
print (result)
print("#" * 50)

#4.enumerate()
subject = ["pyython", "java", "c++", "html"]
numbered_subject = enumerate(subject, 10)
for index, name in numbered_subject:
    print(f"Course ID:c{index} => {name}")
print("#" * 50)

#5.reversed()
secret_word = "Gemini"
for char in reversed(secret_word):
    print(char, end=" ")

#Built-in Modules

import random as rnd
lucky_number = rnd.randint(1, 10)
print(f"\nLucy Number : {lucky_number}")
from random import choice
colors = ["Black", "Blue", "Green", "Red"]
chosen_color = choice(colors)
print(f"Your random color is : {chosen_color}")
print("#" * 50)

#External package and PIP

import pyfiglet
from termcolor import colored
banner = pyfiglet.figlet_format("Sohaila")
colored_banner = colored(banner, color = "blue")
print(colored_banner)
print("#" * 50)


#Date and Time Introduction
import datetime
current_dt = datetime.datetime.now()
print(f"Date and Time : {current_dt}")
print(f"Current Year : {current_dt.year}")
print(f"Current Month : {current_dt.month}")
print(f"Current Day : {current_dt.day}")
print("#" * 50)

#Time
import datetime
current_time = datetime.datetime.now().time()
print(f"Current Time : {current_time}")
print(f"Hour : {current_time.hour}")
print(f"Minute  : {current_time.minute}")
print(f"Second : {current_time.second}")
print("#" * 50)

#Specific Dates and Operations
import datetime
my_birthday = datetime.datetime(2007, 4, 19)
now = datetime.datetime.now()
age_duration = now - my_birthday
print(f"{age_duration.days} Days.")
print("#" * 50)

#strftime Formating Dates with
import datetime
event_date = datetime.datetime(2007, 4, 19)
print(event_date.strftime("Months : %B"))
print(event_date.strftime("Days : %A"))
print("#" * 50)

import datetime
conference_date = datetime.datetime(2026, 11, 10)
print(conference_date.strftime("%A, %B, %Y"))
print(conference_date.strftime("%d/ %m/ %y"))