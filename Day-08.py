#------------Keyword Arguments(**Kwargs)---------------
def student_grades(**grades):
    print("Student Semester Grades Report:")
    for subject, score in grades.items():
        print(f"- {subject} : {score} Marks")
student_grades(Math = 99, Physics = 95, Programming = 98)
print("*" * 50)

def employee_summary (emp_name, * projects, ** details):
    print(f"Employee Name : {emp_name}")
    print("Completed Projects : ")
    for proj in projects:
        print(f"* {proj}")
    print("Additional Details : ")
    for key, val in details.items():    
        print(f"- {key} : {val}")
employee_summary("Sohaila", "Python APP", "Data Analysis", Department = "IT", Level = "Junior")
print("*" * 50)

#------------Function Scope------------
score = 50 #Global Variable
def update_score():
    global score
    score =100
    print(f"Inside Function Score : {score}")
update_score()
print(f"Outside Function Score (After Update) : {score}") 
print("*" * 50)  

#----------Function Recursion--------------
def countdown(n):
    if n<=0:
        print("Time's UP!")
        return
    print(n)
    countdown(n-1)
countdown(3)
print("*" * 50) 

def power(base, exp):
    if exp == 0:
        return 1
    return base * power (base, exp-1)
print(power(2, 3))
print("*" * 50) 


#-------------Lambda Function-----------
def rect_area(length, width):
    return length * width
print(rect_area(5, 4))

clac_area = lambda length, width : length * width
print(clac_area(5, 4))

print(type(clac_area))
print(clac_area.__name__)