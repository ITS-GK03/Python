# LAMBDA FUNCTIONS:



# 1. Add Two Numbers:

# num= lambda num1, num2 : num1+num2
# print(num(3,7))



# 2.Find the Maximum of Two Numbers:

# num= lambda num1, num2 : print("Num1 is greater") if num1>num2 else print("Num2 is greater")
# print(num(3,7))



# 3.Square a Number:

# square= lambda num: print(f"{num*num}")
# square(7)



# 4.Reverse a String:

# stg= lambda name: print(f"{name}"[::-1])
# stg("deva")



# 5.Check if a Number is Even:

# chk_num= lambda num:print("Even number") if num%2==0 else print("Odd number")
# chk_num(66)



# RECURSION FUNCTIONS:


# 1.print 10 to 1:

# def revere_num(num):
#     if num>0:
#         print(num)
#         revere_num(num-1)

# revere_num(10)



# 2.Print 1 to 10:

# def revere_num(num):
#     if num<=10:
#         print(num)
#         revere_num(num+1)

# revere_num(1)



# 3.Fibonacci:

# def cal_fibo(x):
#         if x<= 0:
#             print("Please enter a positive integer.")
#         else:
#             a, b = 0, 1
#             print("Fibonacci sequence:")
#             for i in range(x):
#                 if a>10:
#                     break
#                 print(a, end=' ')
#                 a, b = b, a + b
# cal_fibo(4) 



# 4.Sum of list:

# numbers = [1,2,3,4,5,6,7]

# def sum_list(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total

# result=sum_list(numbers)
# print("Sum of list:", result)


# 5.Get a input from user as number. If user entered negative number. Throw message as invalid. If user entered  0 throw factorial of 0.  Else it has to act as recursive factorial function:


# def factorial(n):
#     if n < 0:
#         return "Invalid input, Please enter a positive number" 
#     elif n == 0:
#         return 1 
#     else:
#         return n *factorial(n - 1)  

# n=int(input("Enter a number:"))
# print(factorial(n))



