import functools
# MAP, REDUCE , FILTER FUNCTION :


# 1.Square all numbers in a list:

# mylist=[4,5,6,7]

# def squ_num(x):
#     return x**2

# res=map(squ_num, mylist)
# print(list(res))



# 2.Convert all strings in a list to uppercase :

# mylist=["kavin", "deva", "akash"]

# def upper_case(x):
#     return x.upper()

# res= map(upper_case, mylist)
# print(list(res))



# 3.Add 10 to each number in a list:

# mylist=[7,3,18,12,6,7]

# def add_ext(k):
#     return k+10

# res=map (add_ext, mylist)
# print(list(res))



# 4.Double each number in a list:


# mylist=[1,2,3,4]

# def double_num(x):
#     return x*2

# res=map(double_num, mylist)
# print(list(res))



# 5.Capitalize the first letter of each string in a list:

# mylist = ["vetric", "dhilip", "gowtham"]

# def upper_first(x):
#     return x.capitalize()

# res=map(upper_first,mylist)
# print(list(res))



# 6.Filter out even numbers from a list:

# mylist=[1,2,3,4,5,6,7,8,9,10]

# def fil_even(g):
#     return g%2==0

# res=filter(fil_even, mylist)
# print(list(res))



# 7.Filter out numbers greater than 10:

# mylist=[3,7,12,18,28,26,13]

# def fil_gre(g):
#     return g>10

# res=filter(fil_gre, mylist)
# print(list(res))



# 8.Filter out words shorter than 4 characters:

# mylist=["gowtham", "leo", "anto"]

# def fil_sho(x):
#     return len(x)<4

# res=filter(fil_sho, mylist)
# print(list(res))



# 9.Filter out strings containing the letter 'a':

# mylist=["gowtham","monieesh","dhilip","vetric","nayeem"]

# def check_a(x):
#     return "a"in x

# res=filter(check_a,mylist)
# print(list(res))



# 10.Filter out numbers that are not divisible by 3:

# mylist=[1,2,3,4,5,6,7,8,9]

# def fil_nd(x):
#     return x%3!=0

# res=filter (fil_nd, mylist)
# print(list(res))



# 11.Filter out negative numbers from a list:

# mylist=[1,2,-3,4,5,6,-7,-28]

# def fil_neg(k):
#     return k<0

# res=filter (fil_neg, mylist)
# print(list(res))



# 12.Filter out numbers that are not divisible by 3:

# mylist=[1,2,3,4,5,6,7,8,9]

# def fil_nd(x):
#     return x%3!=0

# res=filter (fil_nd, mylist)
# print(list(res))



# 13.Find the product of all numbers in a list:

# mylist=[1,2,3,4,5,6,7]

# def pro_num(x,y):
#     return x*y

# res=functools.reduce(pro_num, mylist)
# print(res)



# 14.Concatenate a list of strings:

# mylist=["Onnume"," panna"," mudiyadhu"," prandsss"]

# def con_list(x,y):
#     return x+y

# res= functools.reduce (con_list, mylist)
# print(res)



# 15.Find the maximum number in a list:

# mylist=[3,7,12,18,26,28]

# def max_num(x,y):
#     return x if x>y else y

# res=functools.reduce(max_num,mylist)
# print(res)



# 16.Compute the sum of squares of numbers in a list:

# mylist=[1,2,5,6,7,8]

# def sum_squ(x,y):
#     return x+y**2

# result=functools.reduce(sum_squ,mylist)
# print(result)



#17.Compute the factorial of a number using reduce:

# num = 7

# def factorial_num(x, y):
#     return x * y
# if num < 0:
#     print("Invalid input, Please enter a positive number")
# elif num == 0:
#     print(1)

# result = functools.reduce(factorial_num, range(1, num + 1))
# print(result)



