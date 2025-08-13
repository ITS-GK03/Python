# ARGS AND KWARGS:

# 1. Sum of all arguments:

# def cal_sum(*num):

#     total=0
#     for i in num:
#         total+=i
#     return total
# print(cal_sum(1,2,3,4,5))



# 2: Multiply all arguments:

# def cal_multiply(*num):

#     total=1
#     for i in num:
#         total*=i
#     return total

# print(cal_multiply(1,2,3))



# 3: Concatenate all arguments:

# def con_arg(*str):

#     total=""
#     for i in str:
#         total+=i
#     return total

# print(con_arg("Enaku"),("neram"), ("seri"), ("illa"), ("da"))     



# 4.Print arguments and keywords:

# def show_details(*args, **kwargs):

#   print("Arguments:", args)  
#   print("Keywords:", kwargs) 

# show_details(1, 2, "three", name="Batman", city="Gotham city")



# 5.i/p : checkout_cart(100, 200, 150, discount=10, tax=5, shipping=50)
# o/p : Final amount to pay: ₹475.25

# def checkout_cart(*args, **kwargs):

#     subtotal = sum(args)


#     discount = kwargs.get('discount')
#     if discount:
#         subtotal -= (subtotal * discount / 100)
#     tax = kwargs.get('tax')
#     if tax:
#         subtotal += (subtotal * tax / 100)

#     shipping = kwargs.get('shipping')
#     subtotal += shipping
#     print(f"Final amount to pay: ₹{subtotal}")
# checkout_cart(100, 200, 150, discount=10, tax=5, shipping=50)



# 6.i/p: multi_calculator(10, 5, 2, operation="multiply")
# Output: 100 (10 * 5 * 2)

# def multi_calculator(*args, **kwargs):
#     operation = kwargs.get('operation')
    
#     if operation == 'multiply':
#         result = 1
#         for num in args:
#             result *= num
#         return result
#     else:
#         return ("Invalid operation")

# res=multi_calculator(10, 5, 2, operation="multiply")
# print(res)



# 7.i/p: format_employee_data(name="Ram", age=30, role="Manager", salary=80000)
# Output: "Employee Ram is 30 years old, working as Manager with a salary of ₹80000."

# def format_employee_data(*args, **kwargs):

#     name = kwargs.get("name")
#     age = kwargs.get("age")
#     role = kwargs.get("role")
#     salary = kwargs.get("salary")
    
#     return (f"Employee {name} is {age} years old, working as {role} with a salary of ₹{salary}.")


# print(format_employee_data(name="Ram", age=30, role="Manager", salary=80000))
