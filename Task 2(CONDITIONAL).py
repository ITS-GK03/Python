# TASK 2:


# 1)Find First N Prime Numbers:

# N = int(input("Enter N: "))

# for num in range(2, N + 1):
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             break
#     else:
#         print(num, end=" ")



# 2)Fibonacci Series Up to N Terms:

# n = int(input("Enter the number of terms: "))
# a, b = 0, 1

# for n in range(n):
#     print(a, end=' ')
#     a, b = b, a + b



# 3)Check Armstrong Number:

# num = int(input("Enter a number: "))
# total=0
# digits=str(num)
# if digits:
#     power=len(digits)
#     if power:
#         total = 0
#         for digit in digits:
#          total += int(digit) ** power
# if num==total:
#     print(f"{num} is an Armstrong number.")
# else:
#     print(f"{num} is not an Armstrong number.")


# 4)Count the Digits of a Number:

# user=input("Enter number:")

# number=int(user)
# count=0

# while number!=0:
#     number//=10
#     count+=1

# print("number of digit:", count)



# 5.Palindrome Number Check:-

# x = int(input("Enter a number: "))
# orignal = x  
# reverse = 0
# while x > 0:
#     digit = x % 10
#     reverse = reverse * 10 + digit
#     x = x // 10

# if orignal == reverse:
#     print(f"{orignal} is a palindrome")
# else:
#     print(f"{orignal} is not a palindrome")



# 6)Sum of Digits Until Single Digit:

# n = int(input("Enter a non-negative integer: "))

# while n > 9:
#     total = 0
#     i = n
#     while i > 0:
#         total += i % 10
#         i //= 10
#     print("Sum:", total)
#     n = total
# print("Result:", n)



#7.Reverse a String Without Using Built-in Functions:-

# s = input("Enter a string: ")
# rev = ""
# i = len(s) - 1
# while i >= 0:
#     rev += s[i]
#     i -= 1

# print("Reversed string:", rev)



# 2)Library Fine System:

# day=int(input("Enter days late:"))

# if day==0:
#     print("No fine")

# elif day>=1 and day<=5:
#     print(day*5, "Rupees fine")   

# elif day>=6 and day<=10:
#     print(day*10,"Rupees fine") 

# elif day<0:
#     print("Invalid day ")




# 3)Electricity Bill Slab System:

# unit=int(input("Enter no of unit:"))

# if unit>=0 and unit<=100:
#     print(unit*3, "Rupees")

# elif unit>=101 and unit<=300:
#     print(unit*5, "Rupees" )

# elif unit>=301 and unit<=500:
#     print(unit*7, "Rupees")

# elif unit==500:
#     print(unit*10,"Rupees" ) 

# elif unit<0:
#     print("Invalid unit")

# elif unit>700 and unit<=899:
#     print(unit*70, "Rupees")

# else:
#     print(unit*100, "Rupees")



# 1.Allow max 3 attempts to guess a password:

# main_password="nambathan03"

# attempt=3

# for attempts in range(attempt):
#     password=input("Enter the password:")
#     if password==main_password:
#         print( "Access Granted")
#         break
#     else:
#        print("Password is incorrect, Try again")

#        remaining=attempt-attempts-1

#        if remaining > 0:
#             print(f"You have {remaining} attempt(s) left")
#        else:
#             print("No attempts left. 'Account Blocked'")


# 2.Find the first number greater than 100 that is divisible by both 7 and 13 and is a palindrom:

# num=101
# found = 0 

# while found == 0:
#     if num % 7 == 0 and num % 13 == 0:
#         digit = num % 1
#         reverse = found * 1+ digit
#         num = num // 1
#         print("The first palindrome number greater than 100 divisible by 7 and 13 is:", num)
#         found = 1  
#     num = num + 1



# 3.Count the number of vowels and consonants in a given string using a loop:

# name = input("Enter a name: ")
# vowels = 0
# consonants = 0 
# for char in name:
#     if char.isalpha():
#         if char.lower() in 'aeiou':
#             vowels += 1
#         else:
#             consonants += 1
# print("Vowels:", vowels)
# print("Consonants:", consonants)