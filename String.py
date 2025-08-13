# STRING


# SLICING:

# k="Vanakam da mapla"
# print(k[3:-7])

# # Slice from start:

# k="Vanakam da mapla"
# print(k[:7])

# Slice from end:
# k="Vanakam da mapla"
# print(k[3:])

# Negative Indexing:
# k="Vanakam da mapla"
# print(k[-7:-3])



# MODIFY STRING:

# Upper case:
# k="Vanakam da mapla"
# print(k.upper())

# Lower case:
# k="Vanakam da mapla"
# print(k.lower())

# Remove whitespace:
# k="         Vanakam da mapla         "
# print(k.strip())

# Replacing string:
# k="Vanakam da mapla"
# print(k.replace("Vanakam","Vaa"))

# Split string:
# k="Vanakam da mapla"
# print(k.split(","))



# CONCATENATION STRING:

# String concatenation:

# g="Vanakam da"
# k="mapla"

# gk=g + k
# print(gk)

# gk= g + " " + k
# print(gk)



# FORMAT STRING:

# F-string:

# age=27

# dialogue=f"Una kandu pudikave {age} varusam aaiduchi"
# print(dialogue)

# Placeholders and Modifiers:

# price=23000

# # phone=f"The price of phone is {price}"
# # print(phone)

# phone=f"The price of the phone is {price:.2f}"
# print(phone)

# phone=f"The price of the phone is {200*59}"
# print(phone)



# ESCAPE CHARACTERS:

# Single Quote:

# k="It\'s my game"
# print(k)

# Backslash:

# k="Yengaaaaaaa \\ (kumampati)"
# print(k)

# New Line:

# k="Paravala \nagain start pannalam"
# print(k)

# Carriage Return:

# k="Paravala \ragain start pannalam"  
# print(k)

# Tab:

# k="I play \t cricket"
# print(k)

# Backspace:

# k="Vaangoo \bvaangoo"
# print(k)



# STRING METHOD:

# capitalize() Method:

# g="onnume panna mudiyadhu prandss"
# k=g.capitalize()

# print(k)

# casefold() Method:

# g="Onnume Panna Mudiyadhu Prandss"
# k=g.casefold()

# print(k)

# center() Method:

# g="onnume panna mudiyadhu prandss"
# k=g.center(55)

# print(k)

# count() Method:

# g="onnume panna mudiyadhu prandss"
# k=g.count("panna")

# print(k)

# endswith() Method:

# g="onnume panna mudiyadhu prandss"
# k= g.endswith("!")

# print(k)

# expandtabs() Method:

# g="G\to\tw\tt\th\ta\tm"
# k=g.expandtabs(2)

# print(k)

#isalnum() Method:

# g="gowtham03"
# k=g.isalnum()

# print(k)

# isalpha() Method:
# g="gowthamK"
# k=g.isalpha()

# print(k)

# isascii() Method:

# g="gowtham2807"
# k=g.isascii()

# print(k)

# isdecimal() Method:

# g="gk"
# k=g.isdecimal()

# print(k)


# isdigit() Method:

# g="2807"
# k=g.isdigit()

# print(k)

# isidentifier() Method:

# g="Remo"
# k=g.isidentifier()

# print(k)

# islower() Method:

# g="onnume panna mudiyadhu prandss"
# k=g.islower()

# print(k)

# isupper() Method:

# g="IDHU NAMBA KAALAM NEE ERI AADU KABILA"
# k=g.isupper()

# print(k)

# upper() Method:

# g="Onnume panna mudiyadhu prandss"
# k=g.upper()

# print(k)