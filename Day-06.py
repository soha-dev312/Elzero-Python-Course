#---------- Type Conversion ----------

#str()
price = 450
print(type(price))
print(type(str(price)))
print("*" * 50)

#list()
mystring = "manosha"
myset = {"A", 1, True}
mytuple = (1, 2, 3)
mydict = {"tasnemoo" : 1, "manon" : 2}

print(list(mystring))
print(list(myset))
print(list(mytuple))
print(list(mydict))
print("*" * 50)

#set()
mystring = "manosha"
mylist = ["A", 1, True]
mytuple = (1, 2, 3)
mydict = {"tasnemoo" : 1, "manon" : 2}

print(set(mystring))
print(set(mylist))
print(set(mytuple))
print(set(mydict))
print("*" * 50)

#tuple()
mystring = "manosha"
mylist = ["A", 1, True]
myset = {1, 2, 3}
mydict = {"tasnemoo" : 1, "manon" : 2}

print(tuple(mystring))
print(tuple(mylist))
print(tuple(myset))
print(tuple(mydict))
print("*" * 50)

#dict()
mylist = [["A" , 1], ["B" , 5]]
mytuple = (("S" , 1),("D" , 2))

print(dict(mylist))
print(dict(mytuple))
print("*" * 50)

#--------- User Input---------
city = input('What\'s your favorite city?')
print(f"I would love to visit {city.strip().capitalize()} soon!")
print("*" * 50)

#--------- Practical Slice Email -----------
user_email = input('What\'s your email?').strip()
username = user_email[:user_email.index("@")]
domain = user_email[user_email.index("@")+1 :]
print(f"Username:{username}")
print(f"Domain:{domain}")
print("*" * 50)

#-------- Your Age Full Details ---------
years = int(input("How many years of experience?").strip())
months = years * 12
days = months * 365
print(f"your experience in months is : {months} months")
print(f"your experience in days is : {days} days")
print("*" * 50)

#----------F String Formmating----------
total_seconds = 525600000
print(f"Total seconds : {total_seconds:,}")
print("*" * 50)

#--------Conditional: if, elif, else------------
grade = 88
if grade >= 80 :
    print("Grade is Excellent")# Condition is True
else:
    print("Need To Improve")#Condition is False
print("*" * 50)

#Ternary Conditional Operator
# Condition is True | if condition | else | Condition is False
print("Grade is Excellent" if grade >= 80 else "Need To Improve" )
print("*" * 50)

