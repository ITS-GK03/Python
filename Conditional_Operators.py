# CONDITIONAL STATEMENTS:

# 1.Check even or odd:
 
  
# number=int(input("Enter a number1:"))

# if number%2==0:
#      print("Number is even:", number)

# elif number%2!=0:
#      print("Number is Odd:", number)


 # 2.Check if a number is divisible by 5:


# number=int(input("Enter a number2:"))


# if number%5==0:
#      print("Number is divisible by 5:", number)

# elif number%5!=0:
#      print("Number is not divisible by 5:", number)



# 3.Compare two numbers and print the larger one:


# number1=int(input("Enter a Number1:"))
# number2=int(input("Enter a number2:"))


# if number1>number2:
#     print("number1 is greater than number2")

# elif number1<number2:
#     print("number2 is greater than number1")

# else:
    # print("Both are equal")
    


# 5.Check if a number is between 1 and 10:

# number=int(input("Enter a number:"))

# if number>=1 and number<=10:
#     print("number is between 1 to 10:", number)

# else:
#     print("number is not between 1 to 10:", number)



# 6.Check if a character is a vowel:

# character=input("Enter a character:")
# print(type(character))

# if character in ("a,e,i,o,u"):
#     print("character is a vowel:", character)

# else:
#     print("charater is not a vowel:", character)


 #7.Check if a person is eligible to vote:

# age=int(input("Enter a age:"))


# if age>=18:
#     print("A person is eligibel to vote:", age)

# else:
#     print("A person is not not eligible to vite:", age)



# 8.Determine if a year is a leap year:
 
# year=int(input("Enter a year:"))


# if year%400==0 and year%100==0:
#     print("leap year with century year:", year)

# elif year%100==0:
#     print("century year:", year)

# elif year%4==0 and year%100!=0:
#     print("leap year but not century year:", year)

# else:
#     print("not a leap year:", year)



# 9.Check if a given number is a multiple of 3 and 7:

# number=int(input("Enter a number:"))


# if number%3==0 and number%7==0:
#     print("multiple by both 3 and 7")

# elif number%3==0:
#      print("multiple by 3")

# elif number%7==0:
#      print("multiple by 7")
    
# else:
#     print("both are not multiples of 3 and 7")



# 10.Check if a person is a teenager (age between 13 and 19):

# age=int(input("Enter a age:"))
# print(type(age))

# if age>=13 and age<=19:
#     print("person is a teenager:", age)

# else:
#     print("not a teenager:", age)



# 11.Find the largest of three numbers:

# number1=int(input("Enter a Number1:"))
# number2=int(input("Enter a number2:"))
# number3=int(input("Enter a number3:"))


# if number1>number2 and number1>number3:
#     print("number1 is the largest number")

# elif number2>number3 and number2>number1:
#      print("number2 is the largest number")

# elif number3>number2:
#      print("number3 is the largest number")

# else:
#      print("all are equal")



# 12.Check if a number is divisible by both 5 and 11:

# number=int(input("Enter a number:"))

# if number%5==0 and number%11==0:
#   print("divisible of by both 5 and 11:")

# elif number%5==0:
#     print("divisible by 5")

# elif number%11==0:
#     print("divisible by 11")

# else:
#      print("both are not divisible by 5 and 11:")


# 13.Determine the grade based on marks:

# mark=int(input("Enter the mark:"))

# if mark>=80 and mark<=100:
#     print("A grade")

# elif mark>=56 and mark<=79:
#     print("B grade")

# elif mark>=35 and mark<=55:
#     print("C grade")

# elif mark>100:
#     print("undifined mark")

# else:
#     print("fail")



# 15.Check if a number lies between 10 and 20:

# number=int(input("Enter the number:"))


# if number>=10 and number<=20:
#     print("Number lies between 10 and 20")

# else:
#     print("number does not lies between 10 and 20")


# 16.Determine if a string is empty:

# string=""
# if string:
#     print("The string is empty")

# else:
#     print("The string is not empty")


# 17.check the number is positive or negative:

# number=int(input("Enter a number:"))


# if number>0:
#     print("number is positive")

# else:
#     print("number is negative")    



# 18.check if a number is prime or not a prime number:

# number=int(input("Enter a number:"))

# if number<=1:
#     print("number is not prime")

# elif number==2 or number==3 or number==5 or number==7:
#     print("number is prime") 

# elif number%2==0 or number%3==0 or number%5==0 or number%7==0:
#     print("number is not prime")

# else:
#     print("number is prime")
