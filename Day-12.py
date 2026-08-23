#----------------------
#Exception Handling
#----------------------
try:  # Test The Code For Errors
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
except ZeroDivisionError:  #Handle Division by zero error
    print("Error: You can't divide any number by zero!")
except ValueError:    #Handle invaild input (letters or symbols)
    print("Error: Please enter vaild integers only, no letters")
else:  #Runs if there are no errors at all
    print(f"Success! The result is: {result}")   
finally:  #Runs no matter what happens
    print("Operation finished. Thank you for using our calculator app.") 
print("#" * 50)


try:
    file_name = input("Enter the file name to read: ")
    my_file = open(file_name, "r")
    print(my_file.read())
except FileNotFoundError:   # Handle the error if the file doesn't exist
    print("Error: The file you entered does not exist. Please check the name!") 
else:  # Runs only if no exception occurred
    print("File read successfuly without any errors.")       
finally:
    print("Execution completed. Closing resources....")
    
print("#" * 50)
#-----------------------------
#Regular Expression
#-----------------------------
import re 
warehouse_data = "Items list: AB-105, xz-999, CD-504 and EF-77"
product_pattern = r"[A-Z]{2}-\d{3}"
all_codes = re.findall(product_pattern, warehouse_data)
print("All found product codes:", all_codes)
specific_search = re.search(r"CD|EF-\d{3}", warehouse_data)
if specific_search:
    print("\n---Match Found Details---")
    print("Matched Text:", specific_search.group())
    print("Span Positions:", specific_search.span())
    print("Searched String:", specific_search.string)
else:
    print("No match found for this pattern.")
print("#" * 50)


#---------------------------
#re findall()
#---------------------------
import re
user_message = input("Please Write Your Message With Phone Numbers: ")
phone_pattern = r"01[0-9]{9}"
found_numbers = re.findall(phone_pattern,user_message)
saved_numbers = []
if found_numbers != []:
    for number in found_numbers:
        saved_numbers.append(number)
    print("Numbers Added Successfully!")
    print("Here are the saved numbers:")

    for phone in saved_numbers:
        print(phone)
else:
    print("No valid phone numbers found in your message.")
print("#" * 50)
            
