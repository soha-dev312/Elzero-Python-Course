user_input = input("Enter your name: ")
score = 0
print("Question 1:")
print("What is the output of:")
print("print(2 + 3)\n")

print("A) 23")
print("B) 5")
print("C) Error")
print("D) None of the above")
answer1 = input("Enter your answer (A/B/C/D): ").strip().upper()
if answer1 == "B":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is B) 5.\n")

print("Question 2:")
print("What is the type of:")
print("print(type(10.5))\n")

print("A) <class 'int'>")
print("B) <class 'str'>")
print("C) <class 'float'>")
print("D) <class 'bool'>")
answer2 = input("Enter your answer (A/B/C/D): ").strip().upper()
if answer2 == "C":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is C) <class 'float'>.\n")

print("Question 3:")
print("What is the output of:")
print("print('Hello' + 'World')\n")

print("A) Hello World")
print("B) HelloWorld")
print("C) Hello+World")
print("D) Error")
answer3 = input("Enter your answer (A/B/C/D): ").strip().upper()
if answer3 == "B":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is B) HelloWorld.\n")

print("Question 4:")
print("What is the output of:")
print("Which method is used to add an item to the end of a list in Python?\n")

print("A) append()")
print("B) add()")
print("C) insert()")
print("D) extend()")
answer4 = input("Enter your answer (A/B/C/D): ").strip().upper()
if answer4 == "A":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is A) append().\n")

print("Question 5:")
print("What is the output of:")
print("What is the correct file extension for Python files?\n")

print("A) .pyth")
print("B) .pt")
print("C) .py")
print("D) .pyt")
answer5 = input("Enter your answer (A/B/C/D): ").strip().upper()
if answer5 == "C":
    print("Correct!\n")
    score += 1
else:
    print("Incorrect. The correct answer is C) .py.\n")

print(f"{user_input}, your final score is: {score}/5")

if score == 5:
    print("Excellent! You got all the answers correct!")
elif score >= 4:
    print("Very Good! You got most of the answers correct!")
elif score >= 3:
    print("Good! You got a few answers correct!")
else:
    print("Keep practicing! You'll get better.")