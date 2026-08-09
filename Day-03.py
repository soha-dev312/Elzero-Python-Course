#---Membership Operator-----
name = "Sohaila"
print("S" in name)
print("o" not in name)

friends = ["SOHAILA", "SABER","NOUR"]
print("SOHAILA" in friends)
print("SABER" not in friends)


#-----practicat membership control-----

admins = ["Ahmed", "Sohaila","Soha", "Soo", "Thv"]
name = input("please type your name: ").strip().capitalize()

if name in admins:
    print(f"hello {name}, welcome back to dashboard.")
    option = input("do you want to update your name? Y/N: ").strip().upper()
    if option == "Y" or option == "Yes":
        new_name = input("type new name: ").strip().capitalize()
        admins[admins.index(name)] = new_name
        print(f"name updated successfully to {new_name}! ")
        print(admins)


else:
    print(f"status: access denied, {name} is not an admin!" )        
              

      
      #-----While Loop-----

a = 0
while a < 3:
    print(f"Number is: {a}")
    a += 1
else:
    print("Loop is Done!")

    #----while loop training----
    my_friends = ["Soha", "Tasneem", "Malak", "Shahd"]
    a = 0
    while a < len(my_friends):
        print(f"{my_friends[a]}")
        a +=1
    print("Loop is Done!")    


    # bookmark manager traning---
    my_websites = []
    max_websites = 3
    while len(my_websites) < max_websites:
        url = input("type the website URL:").strip()
        my_websites.append(url)
        print(f"Website added. Total now: {len(my_websites)}")
    else:
        print("Bookmark is full!")
    print("Your saved websites:")
    print(my_websites)  



    #password guess traning---
    secret_password = "SohaSecurity2026"
    tries = 3
    user_input = input("Enter Your Password!").strip()
    while user_input != secret_password and tries> 1:
        tries -= 1
        print(f"Wrong Password! You have {tries} tries left.")
        user_input = input("Try again: ").strip()
    if user_input == secret_password:
        print("Access Granted. Welcome back!")
    else:
        print("Acces Denied! No more tries. ")       




#------For in loop------
# 
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num %2 == 0:
     print(f"{num} is Even")
    else:
     print(f"{num} is Odd") 

else:
   print("All numbers checked successfuiiy!")

   #-----nested loop----
   categories = ["Social Media", "Gaming"]
   websites = ["Facebook", "Steam"]

   for cat in categories:
      print(f"----Category: {cat} ----")
      for web in websites:
         print(f"Checking website: {web}")



   #break and continue
   for x in range(1, 8):
      if x == 3:
         continue
      if x == 5:
         break
      print(f"Number: {x}")      

                                        #-------dictionary-------

ai_result = {
    "url": "https://www.amazon.eg",
    "success": True,
    "trustScore": 40,
    "risklevel": "high",
    "analysis": "The URL is for amazon,eg, which is the official domain." 

}
#get() function
site_url = ai_result.get("url")
score = ai_result.get("trustScore")
level = ai_result.get("risklevel")
comment = ai_result.get("analysis")

print("=" * 50)
print(f"Examing Site: {site_url}")
print(f"Trust Score from AI: {score}/100 ({level} Risk)")
print(f"AI Comment: {comment}")
print("=" * 50)

if score >= 75:
    print("Result: This website is SAFE You can trust it.")
else:
    print("ALERT: This website is DANGEROUS! Block immediatly.")
print("=" * 50)        
      