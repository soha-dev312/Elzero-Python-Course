#ATM

correct_pin = 194007
balance = 1000
attempts = 3

while attempts > 0:
    User = int(input("Please Enter The Correct PIN?"))
    if User == correct_pin:
        print("PIN is correct!\n")
        break
    else:
        attempts -= 1
        print(f"Wrong PIN! You have {attempts} attempts left.")
if attempts == 0:
    print("Too many incorrect attempts. Account locked!")
else:
    while True:            
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = int(input("choose: "))
        if choice == 1:
            print(f"Your Balance is : {balance}")
        elif choice == 2:
            deposite = int(input("Enter a mount deposite: "))
            balance += deposite
            print(f"New Balance is : {balance}")
        elif choice == 3:
            withdraw_money = int(input("Enter a mount withdraw_money: "))
            if withdraw_money > balance:
                raise ValueError ("Insufficient Balance!")
            else:
                balance -= withdraw_money
                print(f"New Balance is : {balance}")
        elif choice == 4:
            print("Exiting.....")
            break
        else:
            raise SyntaxError ("please enter choice!")
                    

