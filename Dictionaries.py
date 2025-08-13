# DICTIONARIES:

# Dictionary:

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }

# print(mydict)

# Dictionary items:

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }

# print(mydict["Brand"])

# Does not allow dulpicate:

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023,
#     "Year":2022
# }

# print(mydict)

# Dictionary Item:

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023,
#     "Colour":["Blue", "Orange"]
# }
# print(mydict)



# ACCESS DICTIONARY ITEMS:

# Accessing Items:

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }
# x=mydict["Model"]
# print(x)

# x=mydict.get("Brand")
# print(x)

# Get Values:

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }

# x=mydict.values()
# print(x)

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }

# x=mydict.values()
# print(x)

# mydict["Year"]=2022
# print(x)

# Get Items:

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }

# x=mydict.items()
# print(x)

# Get Keys:

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }

# x=mydict.keys()
# print(x)

# mydict["Colour"]="Blue"
# print(x)

# Check if key exist:

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }

# if "Model" in mydict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")



# CHANGE DICTIONARY ITEMS:

# Change Values:

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }

# mydict["Year"]=2029
# print(mydict)

# Update Dictionary:

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }

# mydict.update({"Year":2022})
# print(mydict)



# ADD DICTIONARY ITEMS:

# Adding Items:

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }

# mydict["colour"]="Blue"
# print(mydict)

# Update Dictionary:

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }

# mydict.update({"Year":2022})
# print(mydict)



# REMOVE DICTIONARY ITEMS:

# Removing Items:

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }

# mydict.pop("Model")
# print(mydict)

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }

# mydict.popitem()
# print(mydict)

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }

# del mydict["Brand"]
# print(mydict)

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }

# mydict.clear()
# print(mydict)



# LOOP DICTIONARY ITEMS:

# Loop Through a Dictionary:

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }
# for x in mydict:
#   print(x)

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }
# for x in mydict:
#   print(mydict[x])

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }
# for x in mydict.values():
#   print(x)

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }
# for x in mydict.keys():
#   print(x)

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }
# for x, y in mydict.items():
#   print(x,":", y)



# COPY DICTIONARY:

# Copy:

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }

# thisdict=mydict.copy()
# print(thisdict)


# x=('Key1', 'key2', 'key3')
# y=7

# mydict=dict.fromkeys(x,y)
# print(mydict)

# mydict={
#     "Brand":"Ktm",
#     "Model": "Duke 390",
#     "Year": 2023
# }

# x=mydict.setdefault("Model", "Rc")
# print(x)



# NESTED DICTIONARY:

# employee1={
#     "name":"Gowtham",
#     "age":28,
#     "skill":["Python","Java"],
#     "experience":"4 years",
#     "salary":"3.5L/month"
# }

# employee2={
#     "name":"Vetric",
#     "age":26,
#     "skill":["Software develpor", "C++"],
#     "experience":"5 years",
#     "salary":"2.8L/month"
# }

# employee3={
#     "name":"Dhilip",
#     "age":35,
#     "skill":["C","C++","Java script"],
#     "experience":"2.5 years",
#     "salary":"2.5L/month"
# }

# employee4={
#     "name":"Nayeem",
#     "age":27,
#     "skill":["Python","Java"],
#     "experience":"4 years",
#     "salary":"3L/month"
# }

# employee5={
#     "name":"Sree Jeshva",
#     "age":26,
#     "skill":["Web develpor","C"],
#     "experience":"3.5 years",
#     "salary":"2.5L/month"
# }


# Employee={
#     "Employee 1":employee1,

#     "Employee 2":employee2,

#     "Employee 3":employee3,

#     "Employee 4":employee4,

#     "Employee 5":employee5
# }


# for key ,valuesDic in Employee.items():
#     print("\n",key)
#     for keynes in valuesDic:
#         print(keynes,":" ,valuesDic[keynes])
