#-----------Opening Modes------------
#1- Read() => Reading Files
f = open(r"C:\Users\TECNO ZONE\OneDrive\Documents\Desktop\python\Day-01.py", "r")
print(f.readline())
print(f.readlines())
f.close()
print("#" * 50)

#2- Write() => Writing Files
f = open(r"C:\Users\TECNO ZONE\OneDrive\Documents\Desktop\python\my_data.txt", "w")
f.write("Hello! This is a new file.\n")
f.write("I am learning file Handling.")
f.close()
print("#" * 50)

#3- Append() => Appending to Files
f = open(r"C:\Users\TECNO ZONE\OneDrive\Documents\Desktop\python\my_data.txt", "a")
f.write("\nAdding a new line here!")
f.close()
print("#" * 50)

#-------File Handling---------
#1.seek(), tell()
import os
f = open(r"C:\Users\TECNO ZONE\OneDrive\Documents\Desktop\python\my_data.txt", "a")
f.write("\nI Love Python")
f.close()
f = open(r"C:\Users\TECNO ZONE\OneDrive\Documents\Desktop\python\my_data.txt", "r")
f.seek(2)
print(f.tell())
print(f.read())
f.close()
print("*" * 50)


#--------Built in Function--------
#1.all(), any()
data = [10, 0, 5]
print(all(data))
print(any(data))
print("*" * 50)

#2.sum(), round()
my_nums = [1.5, 2.7, 3.1]
total = sum(my_nums, 50) # => 50 + 1.5 + 2.7 + 3.1
print(round(total, 2)) 
print("*" * 50)

#3.range()
my_range = list(range(0, 10, 2))
print(my_range)
print("*" * 50)

#4.id(), bin()
num1 = 50
num2 = 30
print(id(num1))
print(id(num2))
print(bin(num1))
print("*" * 50)

#------Print------
print("Python", "is", "Fun", sep="_")
print("Hello", end = " ")
print("World")
print("*" * 50)

#1.abs() => asbolute
print(abs(100))
print(abs(-100))
print("*" * 50)

#2.pow(base, exp, mod) => power
print(pow(2, 6))
print(pow(2, 5, 2))
print("*" * 50)

#3.max(), min()
numbers = [10, 5, 200, -20]
print(max(numbers))
print(min(numbers))
print("*" * 50)

#slice()
letters = ["A", "B", "C", "D", "E"]
my_slice = slice(3)
print(letters[my_slice])
print("*" * 50)

#map()
names = ["ALI", "SARA", "MONA"]
newnames = list(map(lambda name : name.lower(), names))
print(newnames)
print("*" * 50)