# SETS:

# SET:

# myset={"Hitman", "Free fire", "World war z"}
# print(myset)

# Duplicate not allowed:

# myset={"Hitman", "Free fire", "World war z", "Hitman"}
# print(myset)

# myset={"Hitman", "Free fire", "World war z", 1,0,2,3,True,False}
# print(myset)

# Length of the set:

# myset={"Hitman", "Free fire", "World war z"}
# print(len(myset))

# Set():
# myset=set(("Hitman", "Free fire"))
# print(myset)


# ACCESS ITEMS:

# Access Items:

# myset={"Hitman", "Free fire", "World war z"}
# for x in myset:
#     print(myset)

# myset={"Hitman", "Free fire", "World war z"}
# print("Hitman" in myset)

# myset={"Hitman", "Free fire", "World war z"}
# print("Hitman" not in myset)



# ADD SET ITEMS:

# Add Items:

# myset={"Hitman", "Free fire", "World war z"}
# myset.add("Red redempt")
# print(myset)

# Add Sets:

# myset={"Hitman", "Free fire", "World war z"}
# newset={"Red redempt"}
# myset.update(newset)
# print(myset)

# Add Any Iterable:

# myset={"Hitman", "Free fire", "World war z"}
# mylist=["Red redempt"]

# myset.update(mylist)
# print(myset)



# REMOVE SET ITEMS:

# Remove Item:

# myset={"Hitman", "Free fire", "World war z"}

# myset.remove("Free fire")
# print(myset)

# myset={"Hitman", "Free fire", "World war z"}
# myset.discard("Free fire")
# print(myset)


# LOOP SET ITEMS:

# Loop Items:

# myset={"Hitman", "Free fire", "World war z"}

# for x in myset:
#     print(myset) 


# JOIN SET ITEMS:

# Union:

# myset={"Hitman", "Free fire", "World war z"}
# newset={"Red redempt", "Gta v"}

# k=myset.union(newset)
# print(k)

# myset={"Hitman", "Free fire", "World war z"}
# newset={"Red redempt", "Gta v"}
# schset={"Fall guys"}
# freeset={"Elite"}

# k=myset|newset|schset|freeset
# print(k)


# myset={"Hitman", "Free fire", "World war z"}
# newset={"Red redempt", "Gta v"}

# k=myset.union(newset)
# print(k)


# myset={"Hitman", "Free fire", "World war z"}
# newset={"Red redempt", "Gta v"}

# myset.update(newset)
# print(myset)

# myset={"Hitman", "Free fire", "World war z"}
# newset={"Red redempt", "Gta v", "Free fire"}

# k=myset.intersection(newset)
# print(k)

# myset={"Hitman", "Free fire", "World war z"}
# newset={"Red redempt", "Gta v", "Free fire"}

# k=myset.difference(newset)
# print(k)

# myset={"Hitman", "Free fire", "World war z"}
# newset={"Red redempt", "Gta v"}

# myset.difference_update(newset)
# print(myset)







# 1.largest & smallest number in a list without using min , max functions:

# myset={16,9,3,4,5,6,7,18,8}

# smallest=0
# largest=0

# for x in myset:
#     if smallest is 0 or x<smallest:
#         smallest=x
        
#     elif largest is 0 or x>largest:
#         largest=x

# print("Largest number:", largest)
# print("Smallest number:", smallest)