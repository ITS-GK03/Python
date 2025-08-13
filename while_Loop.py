# WHILE LOOP:

# 1.Print numbers 1 to 10:

# i=0
# while i<10:
#     i=i+1
#     print(i)


# 2.Print the square of each number from 1 to 10:

# i=0
# while i<10:
#     i=i+1
#     print(i*i)g


# 3.Print each character in a string:

# name="gowtham"

# i=0
# while i <(len(name)):

#     print(name[i])
#     i=i+1

# 4.Print each element in a list:

# list=[3,7,9,1]

# i=0
# while i < (len(list)):
#     print(list[i])
#     i=i+1


# 5.Sum of numbers from 1 to 10:

# i=1

# number=0

# while i<=10:
#     number+=i
#     i+=1
#     print(number)


# 6.Print numbers from 10 to 1 (reverse order):

# i=11                                            

# while i in range(11,1,-1):
#     i-=1
#     print(i)


# 7.Print only even numbers from 10 to 20:

# i=10

# while i<=20 and i%2==0:
#     print(i)
#     i+=2


# 8.Print the multiples of 5 between 20 to 50:

# i=20

# while i<=50 and i%5==0:
#     print(i)
#     i+=5


# 9.Print numbers from a list that are greater than 10:

# list = [7,20,30,50]
# i= 0

# while i < len(list):
#     if list[i] > 10:
#         print(list[i])
#     i += 1


# 10.Print all prime numbers between 10 and 20:

# i=10

# while i in range(10,21):
#     if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
#         print(i)
#     i +=1


# 11.Find the largest number in a list:

# list=[7,3,20,23]

# largest_number=list[0]
# i=0

# while i< len(list):
#         if list[i] > largest_number:
#             largest_number = list[i]
#         i += 1
# print(largest_number)


# 12.Count the number of vowels in a string:

# name="gowtham"
# count=0
# i=0
# while i<len(name):
#     if name[i] in ("a","e","i","o","u"):
#         count+=1
#     i+=1
# print("Number of vowels:",count)


# 13.Reverse a number:

# number=int(input("Enter a number:"))
# rev=0

# while number>0:
#     digit=number%10
#     rev=rev*10+digit
#     number=number//10
# print("Reverse number", rev)

