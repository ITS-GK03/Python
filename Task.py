# List Task :


# 1) Reverse a list:

# mylist=[1,2,3,4,5]
# rev_list=mylist[::-1]
# print(rev_list)



# 2) Count positive and negative numbers:

# def count_num(numbers):
#     positive_num = 0
#     negative_num = 0

#     for num in numbers:
#         if num > 0:
#             positive_num += 1
#         elif num < 0:
#             negative_num += 1

#     return positive_num, negative_num

# numbers = [1, -2, 3, -4, 5, 0, -6, -7]
# positive_num, negative_num = count_num(numbers)

# print(f"Positive numbers: {positive_num}")
# print(f"Negative numbers: {negative_num}")



# 3) Print numbers divisible by 3:

# list=[3,5,6,9,16,23,26,28]

# for i in list:
#     if i%3==0:
#         print(i)



# 4) Count how many times a number appears:

# numbers = [1, 2, 2, 7 ,3, 2, 7, 4, 2, 5, 7]
# number_counts = {}
# for num in numbers:
#     if num in number_counts:
#         number_counts[num] += 1
#     else:
#         number_counts[num] = 1

# for num, count in number_counts.items():
#     print(f"The number {num} appears {count} times.")



# 5) Remove all zeros:

# list=[1,0,2,5,6,0,7,9,22,28,0]

# for i in list:
#     if i==0:
#         continue
#     else:
#         print(i)



# 6) Replace all negatives with zero:

# list=[11,2,3,4,-5,6,-7,-8,1,6]

# for i in list:
#     if i<0:
#         print(0)
#     else:
#         print(i)


# 7) Create a list of square of numbers:

# list=[1,2,3,4,5,6,7]
# square_list=[]

# for i in list:
#     square_list.append(i*2)

# print(square_list)



# 8) Print only duplicate elements:

# list=[1,4,5,3,6,7,3,4,1]
# original=[]
# duplicate=[]
# for i in list:
#     if i not in original:
#         original.append(i)
#     elif i in original:
#         duplicate.append(i)
# print(duplicate)



# 9) Find second largest number:

# numbers = [10, 5, 8, 20, 15, 20] 

# if len(numbers) < 2:
#     print("List must contain at least two numbers.")
# else:
#     largest = numbers[0]
#     second_largest = numbers[0]

#     for num in numbers:
#         if num > largest:
#             second_largest = largest
#             largest = num
#         elif num > second_largest and num != largest:
#             second_largest = num

#             print("The second largest number is:", second_largest)



# 10) Count how many elements are less than 10:

# num=[1,2,5,7,9,9,15,28,26]
# count=0

# for i in num:
#     if i>10:
#         count+=1

# print(count)



# 11) Find average of a list:

# list=[1,5,9,6,7,9]
# avg=0
# loop=0

# for i in list:
#     if i>0 or i<0:
#         avg+=i
#         loop+=1

# print(avg%loop)



# 12) Print only prime numbers in a list:

# list=[1,2,54,9,1,3,78,9,13,33]

# for i in list:
#     if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
#         print(i)



# 13) Multiply all elements in a list:

# list=[1,2,3,4,5]
# multi=1

# for i in list:
#     multi*=i
# print(multi)



# 14)  Create a list from 1 to 10:

# num=list(range(1,11))
# print(num)



# 15) Reverse only even numbers:

# list=[1,2,3,4,5,6,7,8,9,10,12,13]

# even_numbers = []
# for number in list:
#     if number % 2 == 0:
#         even_numbers.append(number)
# reversed_even_numbers = even_numbers[::-1]
# i = 0  
# j = 0  
# while i < len(list):
#     if list[i] % 2 == 0:
#         list[i] = reversed_even_numbers[j]
#         j += 1
#     i += 1

# print(list)



# 16)  Create list of all numbers divisible by 5 and 7:

# list=[2,12,78,25,5,9,1,4,14,21]
# num=[]

# for i in list:
#     if i%5==0 or i%7==0:
#         num.append(i)
# print(num)



# 17)  Count elements equal to their index:

# list=[1,2,3,4,5,5,6]
# count=0
# for i in range(len(list)):
#     if list[i]==i:
#         count+=1
# print(count)



# 18) Add 10 to all odd numbers:

# list=[1,2,3,4,5,6,7]
# num=[]
# for i in list:
#     if i%2!=0:
#         num.append(i+10)
#     else:
#         num.append(i)
# print(num)



# 19) Replace all even numbers with -1:

# list=[1,2,3,4,5,6,7]
# num=[]

# for  i in list:
#     if i%2==0:
#         num.append(-1)
#     else:
#         num.append(i)

# print(num)



# 20) Check if a number exists in the list:

# my_list = [10, 25, 33, 40, 50]
# number_to_find = 40

# if number_to_find in my_list:
#     print(f"{number_to_find} is in the list.")
# else:
#     print(f"{number_to_find} is not in the list.")

