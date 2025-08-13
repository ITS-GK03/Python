# Task



# 1. In a paragraph replace a “is” with “was” . then count no of “a” in a paragraph.

# sentence="2011 is the peak of indian cricket "

# new_sentence=sentence.replace("is", "was")
# print(new_sentence)

# count_a=new_sentence.count("a")

# print(f"count of a:{count_a}")



# 2.Get a input from user check its a Email id:

# email=input("Enter a email: ")

# if "@gmail.com" in email:
#     valid_email=email.index("@")
#     valid_email1=email.index(".")
    
#     if valid_email<valid_email1 and valid_email1<len(email) -1:
#         print("Email is valid")

#     if valid_email>valid_email1:
#         print("Invalid email")

# elif "@" in email and "." not in email:
#         print("Invalid email: '.' is missing")
    
# elif "." in email and "@" not in email:
#         print("Invalid email: '@' is missing")

# elif "." and "@" not in email:
#       print("Invalid email:'.' and '@' are missing " )

# else:
#       print("Invalid Email")



# 3.Get a input from user also check  its valid password:

# password=input("Enter the password:")

# special_characters = "~!@#%^&*"
# upper_count = 0
# lower_count = 0
# special_count = 0
# for char in password:
#     if char != char.lower():  
#         upper_count += 1
#     if char != char.upper():
#         lower_count += 1
#     if char in special_characters:
#         special_count += 1

# if len(password) < 8:
#     print("Password Invalid: Must have least 8 characters long.")
# elif upper_count == 0:
#     print("Password Invalid: Must contain at least one uppercase letter.")
# elif lower_count == 0:
#     print("Password Invalid: Must contain at least one lowercase letter.")
# elif special_count == 0:
#     print("Password Invalid: Must contain at least one special character.")
# else:
#     print("It is a Valid Password.")



# 4.login task - get input from user name & password its align with your previous data.throw a login successful message.otherwise its a Invalid input. ( with specific attempts):

# main_user="gowtham"
# main_password="nambathan03"

# attempt=3

# for attempts in range(attempt):
#     username=input("Enter username:")
#     if username==main_user:
#         print("Login successful")
#     else:
#         print("User not found")
#         break

#     password=input("Enter the password:")
#     if password==main_password:
#         print("Login successful")
#     else:
#        print("Password is incorrect, Try again")

#        remaining=attempt-attempts-1

#        if remaining > 0:
#             print(f"You have {remaining} attempt(s) left")
#        else:
#             print("No attempts left. Unable to Login")