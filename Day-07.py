#----------Nested Loop ------------
Numbers = [2, 3]
Multi = [2, 4, 6]
for num in Numbers:
    print(f"Table of {num}:")
    for m in Multi:
        print(f"{num} * {m}")
print("*" * 50)

#-----------Function And Return--------------
def calculate_square_area(side_length):
    area = side_length * side_length
    return area
result = calculate_square_area(10)
print(f"The Square Area is : {result}")


#--------------Parameters and Arguments-------------
def student_report(student_name, score):
    print(f"Student:{student_name} | Score:{score}/100")
student_report("Sohaila", 99)  

#-------------Function Packing (*args)---------------
def hobbies(user_name, *hobbies_list):
    print(f"Hello {user_name}, Your Hobbies are :")
    for hobby in hobbies_list:
        print(f" - {hobby}")
hobbies("Sohaila", "Read", "Programming", "Drawing") 

#-----------Function Default Parameter----------------
def register_user(username, role = "Student"):
    print(f"User:{username} | System role:{role}")
register_user("soha")
register_user("soly", "Programming Engineering")    
