Grades = {
    "Ahmed" : 95,
    "Sohaila" : 98,
    "Menna" : 85,
    "Tasneem" : 90,
    "David" : 70,
    "Adrien" : 47 
}

user = input("Enter a name: ").title()

if user in Grades:
    print(f"The grade is: {Grades[user]}")
else:
    print("Student not found!")
def total(Grades):
    return sum(Grades.values())
print(f"Total Grades: {total(Grades)}")
highest = max(Grades.values())
lowest = min(Grades.values())
print(f"Highest Grade:{highest}")
print(f"Lowest Grades: {lowest}")

sorted_students = sorted(Grades.items(), key=lambda x: x[1], reverse=True)
print("\nSorted Students (Highest to lowest):")
for name, grade in sorted_students:
    print(f"{name}: {grade}")

