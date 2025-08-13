# LIST:

# LIST:

# List:

# mylist=["Samsung", "iQoo", "Redmi"]
# print(mylist)

# Allow Duplicate:

# mylist=["Samsung", "iQoo", "Redmi", "iQoo", "Redmi"]
# print(mylist)

# List Lenght:

# mylist=["Samsung", "iQoo", "Redmi"]
# print(len(mylist))

# List items:

# mylist=["Samsung",125000, "iQoo", 23000, "Redmi", 20000 ]
# print(mylist)

# Type:

# mylist=["Samsung", "iQoo", "Redmi"]
# print(type(mylist))

# List constructor:

# mylist=list(("Samsung", "iQoo", "Redmi"))
# print(mylist)



# ACCESS LIST ITEMS:

# Access Items:

# mylist=["Samsung", "iQoo", "Redmi"]
# print(mylist[1])

# Negative Indexing:

# mylist=["Samsung", "iQoo", "Redmi"]
# print(mylist[-2])

# Range of index:

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# print(mylist[2:6])

# Range og Negative index:

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# print(mylist[-5:-2])

# Check if item exist:

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# if "iPhone" in mylist:
#     print("Yes, 'iphone' is in the list")



# CHANGE ITEM LIST:

# Change item value:

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# mylist[2]="Vivo"
# print(mylist)

# Change a range of item value:

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# mylist[2:4]=["Vivo", "Oppo"] 
# print(mylist)



# ADD ITEM LIST:

# Append item:

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# mylist.append("Vivo")
# print(mylist)

# Insert item:

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# mylist.insert(2,"Oppo")
# print(mylist)

# Expand list:

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# ulist=["Hitman", "Gta v", "Evil resident", "Elite sniper"]

# mylist.extend(ulist)
# print(mylist)

# Add any iterable:

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# ulist=("Hitman", "Gta v")

# mylist.extend(ulist)
# print(mylist)



# REMOVE LIST ITEMS:

# Remove specific items:

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# mylist.remove("Redmi")
# print(mylist)

# Remove specific index:

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# mylist.pop(3)
# print(mylist)

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# mylist.pop()
# print(mylist)

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# del mylist[0]
# print(mylist)

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# del mylist

# Clear the list:

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# mylist.clear()
# print(mylist)


# LOOP LIST:

# Loop through a list:

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# for x in mylist:
#     print(x)

# Loop through the index number:

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# for i in range(len(mylist)):
#     print(mylist[i])

# Using while loop:

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# i=1
# while i < len(mylist):
#     print(mylist[i])
#     i=i+1

# Looping Using List Comprehension:

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# [print(x) for x in mylist]



# SORT LIST:

# Sort list Alphanumerically:

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# mylist.sort()
# print(mylist)


# Sort decending:
# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# mylist.sort(reverse=True)
# print(mylist)


# Reverse sort:

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# mylist.reverse()
# print(mylist)



# COPY LIST:

# Use the copy() method:

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# ulist=mylist.copy()
# print(ulist)

# Use the list() method:

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# ulist= list(mylist)
# print(ulist)

# Use the slice Operator:

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# ulist=mylist[:]
# print(mylist)



# JOIN LIST:

# mylist=["Samsung", "iQoo", "Redmi", "Realme", "iPhone", "Huawai"]
# ulist=["Hitman", "Gta v", "Evil resident", "Elite sniper"]

# for x in ulist:
#     mylist.append(x)

# print(mylist)

