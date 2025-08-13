# TUPLE:


# PYTHON TUPLE:

# Tuple:

# thistuple=("Hitman", "Free fire", "World war z")
# print(thistuple)

# Allow Duplicate:

# thistuple=("Hitman", "Free fire", "World war z", "Hitman", "Red redempt")
# print(thistuple)

# Tuple Length:

# thistuple=("Hitman", "Free fire", "World war z")
# print(len(thistuple))

# Create tuple with one item:

# thistuple=("Hitman",)
# print(type(thistuple))

#Tuple constructor:

# thistuple=tuple(("Hitman", "Free fire", "World war z"))
# print(thistuple)



# ACCESS TUPLE:

# Access tuple item:

# thistuple=("Hitman", "Free fire", "World war z")

# print(thistuple[1])
# print(thistuple[-3])

# Range of index:

# thistuple=("Hitman", "Free fire", "World war z")
# print(thistuple[-3:-1])
# print(thistuple[1:3])

# Check if items exist:

# thistuple=("Hitman", "Free fire", "World war z")
# mytuple=input("Enter a game:")

# if mytuple in thistuple:
#     print("Yess it is there...")
# else:
#     print("No it is not there...")


# UPDATE TUPLE:

# Change tuple values:

# mytuple=("Hitman", "Free fire", "World war z")
# newtuple=list(mytuple)
# newtuple[1]="Red redemt"
# mytuple=tuple(newtuple)

# print(mytuple)

# Add items convert into list:

# mytuple=("Hitman", "Free fire", "World war z")
# newtuple=list(mytuple)

# newtuple.append("Red redemt")
# mytuple=tuple(newtuple)

# print(mytuple)

# Add tuple to a tuple:

# mytuple=("Hitman", "Free fire", "World war z")
# newtuple=("Red redempt",)

# mytuple+=newtuple

# print(mytuple)


# UNPACK TUPLE:

# Unpacking a tuple:

# mytuple=("Hitman", "Free fire" ,"Red redempt", "World war z")

# (red,*yellow, black) = mytuple

# print(yellow)


# LOOP TUPLE:

# Loop Through the Index Numbers:

# mytuple=("Hitman", "Free fire", "World war z")

# for i in range(len(mytuple)):
#     print(mytuple[i])

# Using a While Loop:

# mytuple=("Hitman", "Free fire", "World war z")

# i=0

# while i<len(mytuple):
#     print(mytuple[i])
#     i=i+1


# JOIN TUPLE:

# Add:

# mytuple=("Hitman", "Free fire", "World war z")
# newtuple=("Red redempt", "Gta v", "Evil dead")

# thistuple=mytuple+newtuple

# print(thistuple)

# Multiple:

# mytuple=("Hitman", "Free fire", "World war z")
# newtuple=mytuple*2

# print(newtuple)