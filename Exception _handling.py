# EXCEPTION HANDLING:

# try
# except
# else
# finally


# try:
#     print(name)

# except:
#     print("except....")


# number1=int(input("Enter a number1:"))
# number2=int(input("Enter a number2:"))

# try:  
#     result=number1/number2
#     print(result)

# except:
#     print("Except")



# 1.Write a python program that asks the user to input a number and print the reciprocal of that number. Handle the exception if the user input zero.

# num=int(input("Enter a number:"))

# if num==0:
#     print("Error......")
# else:
#     print(f"1/{num}")



# 2.Modify the above program to also handle the exception if the user inputs a non-numeric value:

# num=int(input("Enter a number:"))

# if num==0:
#     print("Error......")
# else:
#     print("Value error...")



# 3.write a program that reads a number from the user and prints its square. Use the else clause tp print a success message:

# try:
#     num=int(input("Enter a number:"))
#     print(num*num)

# except:
#     print("Error..........")

# else:
#     print("Success.......")



# 4. Modify the program in task 3 to include a finally clause that print a message regardless of whether an exception occurred or not:

# try:
#     num=int(input("Enter a number:"))
#     print(num*num)

# except:
#     print("Error..........")

# else:
#     print("Success.......")

# finally:
#     print("Sum completed")      



# 5. Write a function that raises a valueError if the input number is negative:

# num=int(input("Enter a number:"))

# if num<0:
#     raise Exception ("value error.....")
# else:
#     print(num)


# 6. Write a program that repetedly asks the user for a number and handles exception. The program should continue asking until a valid number is entered:

# while True:
#     try:
#         num=int(input("Enter a number:"))
#         res=int(num)
#         print(f"Entered a valid number:{num}")
#         break

#     except ValueError:
#         print("Invalid input, enter a whole number")