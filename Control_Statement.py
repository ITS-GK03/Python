# CONTROL STATEMENTS:

# 1.Print numbers from 1 to 10, but stop when the number is 5:

# for i in range(1,10):
#    print(i)
#    if i==5:
#     break
    

# 2.Find the first negative number in a list:

# my_list=[7,3,-20,23,-26]

# for i in my_list:
#     if i<0:
#         print(i)
#         break
        

# 3.Iterate over a list and stop if you encounter a zero:

# list=[7,3,28,0,18]

# for i in list:
#      print(i)
#      if i==0:
#           break
       

# 4.Print numbers from 1 to 10, skipping 5:

# for i in range(11):
#     if i==5:
#         continue
#     print(i)


# 5.Print only even numbers from 1 to 10:

# for i in range(1,11):
#     if i%2==0:
#         print(i)
#         pass


# 6.Iterate over a list and skip negative number:

# list=[7,3,28,21,-26,10]

# for i in list:
#     if i<0:
#         continue
#     print(i)
        

# 7.Print characters of a string, skipping vowels:

# name="gowtham sanjay"

# for i in name:
#     if i in ("a,e,i,o,u"):
#         continue
#     print(i)


# 8.Iterate over numbers from 1 to 20, but skip multiples of 3:

# for i in range(1,21):
#     if i%3==0:
#         continue
#     print(i)


# 9.Iterate over a list and use pass for future implementation:

# list=[7,3,28,21,-26,10]

# pass


# 10.Iterate over numbers from 1 to 10, skip 5 and stop at 8:

# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)

#     if i==8:
#         break


# 11.Print only odd numbers from 1 to 10, but use pass for even numbers:

# for i in range(1,11):
#     if i%2!=0:
#         print(i)
       
#     if i%2==0:
#         pass


# 12.Iterate over a list, skip negatives, print positives, stop at zero:

# list=[7,3,-28,21,-26,10,0,90]

# for i in list:
#     if i<0:
#         continue
#     print(i)

#     if i==0:
#         break


# 13.Skip the first half of a list, process the second half, use pass for future:

# list=[1,2,3,4,5,6]
# half_list=len(list)//2
# for i in list[half_list:]:
#     pass


# 14.Get a input from user like number until user enter zero after that have to print the product of numbers:

# product=1
# while True:
#     number=int(input("Enter a number(or 0 to stop):"))

#     if number==0:
#         break
   
#     product *=number

# print("The product of numbers:", product)


# 15.Get input from a user like number until user enter negative number after that have to print the sum of numbers:

# sum=0
# while True:
#     number=int(input("Enter a number(or negative number to stop):"))

#     if number<0:
#         break

#     sum+=number

# print("The sum of numbers:", sum)