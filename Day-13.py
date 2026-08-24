#----------------------------
#   Regulare Expressions
#----------------------------

# re.split() & re.sub()
import re
text_data = "Python_Programming,is-Very-Powerful"
#re.spilt() => (Patter, String, Maxsplit)
words_list = re.split(r"[_|-]", text_data)
print("Splitted List:", words_list)

# enumerate() => (Iterable, Start)
for index, w in enumerate(words_list, 1):
    print(f"Word {index}: {w.upper()}")
print("#" * 30)

#re.sub() => (Pattern, Replace, String, Replacecount)
clean_text = re.sub(r"[_,-] ", " ", text_data)
print("Cleand Text:", clean_text)
print("#" * 30)

# Flags() & Groups()
user_info = "User: Ahmed_Ali | ID: 98765 |Role: Admin"
pattern = r"User:\s*(\w+)\s*\|\s*ID:\s*(\d+)\s*\|Role:\s*([A-Za-z]+)"
# re.IGNORECASE
match_result = re.search(pattern, user_info, re.IGNORECASE)
# group(index)
if match_result:
    print("Full Match:", match_result.group(0))
    print("All Groups:", match_result.groups())
    print("_" * 30)
    print(f"Username : {match_result.group(1)}")
    print(f"User ID : {match_result.group(2)}")
    print(f"User Role: {match_result.group(3)}")
else:
    print("No Match Found!")    