num1 = int(input("Enter your first number?"))
num2 = int(input("Enter your second number?"))
op = input("Operation (+, -, *, /, %, **, //):")

if op == "+":
    print(f"Result = {num1+num2}")
elif op == "-":
    print(f"Result = {num1-num2}")
elif op == "*":
    print(f"Result = {num1*num2}")
elif op == "/":
    print(f"Result = {num1/num2}")
elif op == "%": 
    print(f"Result = {num1%num2}")
elif op == "**":
    print(f"Result = {num1**num2}")
elif op == "//":
    print(f"Result = {num1//num2}")
else:
    print("Invaild Operation!")               

