#string

alert = """تحذير عزيزي الطالب
هذا الموقع خطر
اخرج فورا"""
print(alert)
#Escape character

text = 'i\'m soso'
print(text)
#Raw string

link =r"https://kfs.edu.eg\new_login"
print(link)

#strings index and slice
#[start:end:step]

text = "I Love Kim Taehyung"
print(text[::2])
print(text[1:6])
print(text[::-1])

#string methods

text = "    sohaila mohammed   "
#strip(),lstrip(),rstrip()

print(text.strip())
print(text.lstrip())
print(text.rstrip())
#upper(),lower(),title(),capitalize(),index(),find(),count()

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.index("sohaila"))
print(text.find("sohaila"))
print(text.count("sohaila"))

#max split
url = "https//kfs.edu.eg/login"

print(url.split("/"))
print(url.startswith("https"))
print(url.endswith(".edu.eg"))

#split,rsplit
myname = "sohaila mohammed saad"
print(myname.split(" ",1))
print(myname.rsplit(" ",1))

#count()
text = "ahlan sohaila ahlan"
print(text.count("ahlan",0,10))

#center
name = "sohaila"
print(name.center(15,"*"))

#isalpha(),isalnum()
user_1 = "sohaila"
user_2 = "sohaila123"
user_3 = "sohaila_mohammed"
print(user_1.isalpha())
print(user_2.isalnum())
print(user_3.isalpha())



#islower(),isupper()
msg1 = "kfs"
msg2 = "KFS"
print(msg1.islower())
print(msg2.isupper())

#Numbers types

print(type(100)) #integer
print(type(100.0)) #float
print(type(100+5j)) #complex number

#complex number

z = 15 + 20j
print(z.real)
print(z.imag)

#type conversion

print(float(19))
print(int(20.7))

#--------Arthmetic Operators-----

#addition
print(10+15)
#subtriction
print(10-15)
#multiplication
print(10*15)
#division
print(15/5)
print(int(15/5))
#modulus
print(17%2)
#exponent
print(5**3) #power
#floor division
print(100//20)

print(10+15*3)


#-----Assignment operators------

mybalance = 100
mybalance += 50
print(mybalance)

mybalance -= 30
print(mybalance)

mybalance *= 2
print(mybalance)

#old way format

myname = "sohaila mohammed"
myage = 19
myGPA = 3.8542

print("Welcome back, %s!"%myname)
print("Age: %d years old."%myage)


print("your GPA is: %f"%myGPA)
print("your GPA is: %.2f"%myGPA)

#the new way format

username = "soha"
score = 98.567
print("Welcome {}, Your exam score is {:.2f}%".format(username,score))


#f_string
print(f"Welcome {username},Your exam score is {score:.2f}%")


#------LISTS---------
urls_list = ["google.com","malicious-link.net",102,"google.com"]
print(urls_list)
print(urls_list[0])
print(urls_list[1])
print(urls_list[-1])
print(urls_list[:3])
print(urls_list[::2])

#mutable
urls_list[1] = "safe-link.com"


#lists methods part1

my_urls = ["google.com","facebook.com"]
my_urls.append("malicious-linked.net")
print(my_urls)
my_urls.insert(1,"instagram.com")
print(my_urls)
new_urls = ["yahoo.com","githup.com"]
my_urls.extend(new_urls)
print(my_urls)
my_urls.remove("facebook.com")
print(my_urls)
my_urls.sort()
print(my_urls)
my_urls.sort(reverse=True)
print(my_urls)
my_urls.reverse()
print(my_urls)
    

#-----------SETS-------
my_set = {"google.com","facebook.com","google.com",10,20,10}
print(my_set)
#عشان اعمل set فاضيه
empty_set = set()

#--------if conditions-------

current_url = "bad-site.net"

blacklist = {"malicious-link.net","bad-site.net","phishing-hub.org"}
suspicious_list = {"unknown-domain.com","test-link.xyz"}

if current_url in blacklist:
    print("warning:this link is macilious and has been blocked immediately")
elif current_url in suspicious_list:
    print("warning:the link is suspicious,please be careful.")
else:
    print("this link is completely safe; you can browse it.")


    #-----nested if------
has_login_form = True
is_verified_domain = False

if has_login_form == True:
    print("A Login page has been detected... Internal security is being checked")

    if is_verified_domain == True:
        print("The domain is official and trusted; the page is secure.")
    else:
        print("Phishing high risk!Login page on an untrusted domain") 

else:
    print("A regular page that does not request sensitive data.")   


    #------ternary operator-----
    
    score = 20
    print("phishing" if score > 50 else "safe") 
     
            
             