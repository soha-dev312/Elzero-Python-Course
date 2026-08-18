age = int(input("Enter your age?"))
if age >= 18:
    has_id = input("Do you have an ID?(YES/NO)")
    if has_id == "Yes":
        print("Access Granted")
    else:
        print("ID Rquired")
else:
    print("Access Denied")        