#---------Set Methods Part2---------

#Difference()
group_a = {"VsCode", "Git", "Docker", "Postman"}
group_b = {"CodeBlocks", "VsCode"}
print(group_a.difference(group_b))
print("-" * 50)

#Difference_Update()
my_tools = {"Python", "Java", "C++", "Html"}
used_tools = {"Html", "Css", "Java"}
print(my_tools)
my_tools.difference_update(used_tools)
print(my_tools)
print("-" * 50)

#Intersection()
backend = {"Python", "NodeJS", "SQL"}
frontend = {"Python", "Css", "Html"}
print(backend.intersection(frontend))
print("-" * 50)

#Intersection_Update()
team_a = {10, 20, 30}
team_b = {30, 40, 50}
print(team_a)
team_a.intersection_update(team_b)
print(team_a)
print("-" * 50)

#Symmetric_Difference()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.symmetric_difference(set2))
print("-" * 50)

#Symmetric_Difference_Update()
x = {"A", "B", "C"}
y = {"C", "D", "B"}
print(x)
x.symmetric_difference_update(y)
print(x)
print("-" * 50)

#issuperset()
all_permissions = {"read", "write", "excute", "delete"}
user_permissions = {"read", "write"}
print(all_permissions.issuperset(user_permissions))
print("-" * 50)

#issubset()
basic_colors = {"red", "blue"}
rainbow_colors = {"red", "blue", "green", "yellow"}
print(basic_colors.issubset(rainbow_colors))
print("-" * 50)

#isdisjoint()
group1 = {1, 2, 3}
group2 = {4, 5, 6}
group3 = {3, 9, 10}
print(group1.isdisjoint(group2))
print(group1.isdisjoint(group3))
print("-" * 50)

#---------  Boolean ----------

#isspace()
text1 = " "
text2 = "Hello Python"
print(text1.isspace())
print(text2.isspace())
print("-" * 50)

#-------- Boolean & True/False Value ------------

print(100 > 100)
print(100 > 200)
print(100>90)
print("-" * 50)

#True Values
print(bool("Hi"))
print(bool(300))
print(bool(200.09))
print(bool(True))
print(bool([1, 2, 3]))
print("-" * 50)

#False Values
print(bool(""))
print(bool(0))
print(bool(''))
print(bool([]))
print(bool(100>200))
print("-" * 50)

#------- Boolean Operators --------

score = 50
subject = "Math"

#And
print(score<100 and subject == "English" ) #False
print(score<100 and subject == "Math" ) #True

#Or
print(score<100 or subject == "English" ) #True
print(score<100 or subject == "Math" ) #True

#Not
print( not( subject == "English") ) #True
print("-" * 50)

#------- Comparison Operators ---------

#Equal => ==
print(100 == 100)
print(100 == 200)

#Not Equal => !=
print(100 != 200)
print(9 != 3)

#Greater Than & Less Than => < & >
print(7 < 9)
print(15 > 20)

#Greater Than or Equal &  or Equal Less Than => & =<
print(100 <= 200)
print(500 >= 500)
print("-" * 50)