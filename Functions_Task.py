# FUNCTIONS:

# 1.Calculate Square:

# def cal_square(num):
#     if num:
#         print("Square of the number:", num*num)

# cal_square(7)



# 2.Calculate Area of Rectangle:

# def cal_areaofrectangle(length, breadth):

#     if length>0 and breadth>0:
#         print("Area of rectangle:", length*breadth)
#     else:
#         print("Invalid input ")

# cal_areaofrectangle(3,7)



# 3.Check Even or Odd:

# def che_evenorodd(num):

#     if num%2==0:
#         print("It is Even number")
#     else:
#         print("It is Odd number")

# che_evenorodd(28)



# 4.Calculate Factorial:

# def calculate_factorial(num):
#     factorial = 1
#     for i in range(1, num + 1):
#         factorial *= i
#     return factorial

# calculate_factorial(5)
# print("Factorial is:", calculate_factorial(5))



# 5.Check Prime Number:

# def che_primenumber(num):

#     if num>0:
#         if num==2 or num==3 or num==5 or num==7:
#             print("It is Prime number")
        
#         elif num%2==0 or num%3==0 or num%5==0 or num%7==0:
#             print("It is not Prime number")
    
#     else:
#         print("Not Prime number")

# che_primenumber(77)



# 6.Reverse a String:

# def rev_string(stg):
    
#     rev = ""
#     i = len(stg) - 1
#     while i >= 0:
#         rev += stg[i]
#         i -= 1

#     print("Reversed string:", rev)

# rev_string("Gowtham")



# 7.Count Characters:

# def count_chr(name):

#     count = 0
#     for char in name:
#         count += 1
#     print("Number of characters:", count)

# count_chr("Gowtham")



# 8.In a list print Sum of Squares:

# list=[1,2,3,4,5,6]

# def sum_square():
#     sum=0
#     for i in list:
#         sum+=i*i
#     print(sum)

# sum_square()



# 9.Check Palindrome:

# def check_num(x):
#     orignal = x  
#     reverse = 0
#     while x > 0:
#         digit = x % 10
#         reverse = reverse * 10 + digit
#         x = x // 10
#     if orignal == reverse:
#         print("It is Palindrome Number")
#     else:
#         print("It is not a Palindrome Number")

# check_num(77)



#10. Calculate Fibonacci:

# def cal_fibo(x):
#     if x<= 0:
#         print("Please enter a positive integer.")
#     else:
#         a, b = 0, 1
#         print("Fibonacci sequence:")
#         for _ in range(x):
#             print(a, end=' ')
#             a, b = b, a + b

# cal_fibo(7)



#11.Check Armstrong Number:

# def check_num(x):
#     total=0
#     digits=str(x)
#     if digits:
#         power=len(digits)
#         if power:
#             total = 0
#             for digit in digits:
#                 total += int(digit) ** power
#     if x==total:
#         print("It is Armstrong number.")
#     else:
#         print("It is not Armstrong number.")

# check_num(7863)



#12.Check Leap Year:-

# def check_year(year):
#     if year%4==0 or year%400==0:
#         print("Leap Year")
#     else:
#         print("It is not Leap Year")

# check_year(2023)



# 14.I/P - 3 list ,O/P - Matrix:


# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = [7, 8, 9]

# def create_matrix(list1, list2, list3):
#     return [list1, list2, list3]   

# matrix = create_matrix(list1, list2, list3)

# print("Matrix:")
# for row in matrix:
#     print(row)



# 15.I/P - paragraph, O/P - list and also count words:

