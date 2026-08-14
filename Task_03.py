math = int(input("Enter your math mark:"))
english = int(input("Enter your english mark:"))
arabic = int(input("Enter your arabic mark:"))

total_marks = math + english + arabic
avarage_mark = total_marks / 3

print("#" * 50)
print(f"Total Marks:{total_marks}")
print(f"Avarage Marks:{avarage_mark:,}")
print("#" * 50)