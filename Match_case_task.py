#  MATCH CASE TASK:

# 1.Check a day as weekday or weekend:

# day=input("Enter the day:")

# match day.lower():
#     case day if day=="monday" or day=="tuesday" or day=="wednesday" or day=="thursday" or day=="friday":
#         print("It is a weekday")

#     case day if day=="saturday" or day=="sunday":
#         print("It is a weekend")
    
#     case _:
#         print("Invalid day")


# 2.Print a no of days in a month:

# month=input("Enter a month:")

# match month.lower():
#     case month if month=="january" or month=="march" or month=="may" or month=="july" or month=="august" or month=="october" or month=="december":
#         print("The month has 31 days")

#     case month if month=="february":
#         print("The month has 28 days, In leap year 29 days")

#     case month if month=="april" or month=="june" or month=="september" or month=="november":
#         print("The month has 30 days")

#     case _:
#         print("Invalid month")


# 3.Print a entered input is vowels or consonants:

# character=input("Enter a character:")

# match character.lower():
#     case character if character in (" a,e,i,o,u"):
#         print("Charater is vowel")
    
#     case character if character in (" b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z"):
#         print("Charater is consonant")
    
#     case _:
#         print("Both vowel and consonant")


#  4.Grade by percentage:

# percentage=int(input("Enter the percentage:"))

# match percentage:
#     case percentage if percentage>=90 and percentage<=100:
#         print("A grade")
    
#     case percentage if percentage>=70 and percentage<=89:
#         print("B grade")

#     case percentage if percentage>=50 and percentage<=69:
#         print("C grade")

#     case percentage if percentage>=35 and percentage<=49:
#         print("D grade")

#     case percentage if percentage>=0 and percentage<=34:
#         print("Fail")

#     case _:
#         print("Invalid percentage")



#  5.Season based on month name:


# month=input("Enter the month:")

# match month.lower():
#     case month if month in ("december,january,february"):
#         print("It is winter season")
    
#     case month if month in ("march,april,may"):
#         print("It is a spring")
    
#     case month if month in ("june,july,august"):
#         print("It is a summer season")

#     case month if month in ("september,october,november"):
#         print("It is a autumn")

#     case _:
#         print("Plase enter a valid input")


# 6.Positive or negative:

# number=int(input("Enter a number:"))

# match number:
#     case number if number>=1:
#         print("Positive Number")

#     case number if number<0:
#         print("Negative Number")

#     case number if number==0:
#         print("Neither positive nor negative")


# 7.Get input from user print if it is between 1-50:

# number=int(input("Enter a number:"))

# match number:
#     case number if number>=1 and number<=50:
#         print("Number is in the range")
  
#     case _:
#         print("Number is not in the range")






          



