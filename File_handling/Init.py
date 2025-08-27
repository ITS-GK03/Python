import random
# FILE HANDLING

# open - parameters - filename , mode
# r - read
# a - append
# w - write
#  x - create 

# myfile=open("task.txt","w")

# myfile.write("hi......\n")

# myfile.write("Pudhu file create pannikrom prandsssss\n")
# myfile.close()

# myfile=open("task.txt","a")
# myfile.write("Onnume panna mudiyadhu prandsss")





# 1) Word Frequency Counter:
# Read a text file (say a story).Count how many times each word appears.Save the result into another file like:
# the -> 15
# cat -> 4
# jumped -> 2


# with open("first.txt", "w") as myfile:
#     myfile.write("Later, the stork decided jumped to return the favor. She invited the fox to her house and served a delicious meal in a tall, narrow-necked jar. The stork was able to enjoy her food by dipping her beak into the jar, but the fox could not reach the food and went home hungry.")
# count_the = 0
# count_cat = 0
# count_jumped = 0

# with open("first.txt", "r") as myfile:
#     text = myfile.read().lower().replace(".", "").replace(",", "")
#     words = text.split()
#     for word in words:
#         if word == "the":
#             count_the += 1
#         elif word == "cat":
#             count_cat += 1
#         elif word == "jumped":
#             count_jumped += 1

# with open("first.text", "w") as myfile:
#     myfile.write("Count of 'the': " + str(count_the) + "\n")
#     myfile.write("Count of 'cat': " + str(count_cat) + "\n")
#     myfile.write("Count of 'jumped': " + str(count_jumped) + "\n")



# 2.2)Random Story Picker
# File has 10 small stories/quotes.Each time you run the program, pick a random one and save it into a new file like a "Quote of the Day".Mixes randomness + file handling.


# quote=("The only way to do great work is to love what you do.","Believe you can and you're halfway there", "The greatest glory in living lies not in never falling, but in rising every time we fall.","Do something today that your future self will thank you for.")

# with open("first.txt", "w") as myfile:
#     my_quote=random.choice(quote)

# with open("first.txt", "r") as myfile:
#     text = myfile.read().lower().replace(".", "").replace(",", "")
#     words = text.split()
#     quote=words

# with open("Quote of the day.text", "w") as myfile:
#     myfile.write(my_quote)



# 3)Word Length Analyzer.Read words from a file.Create another file grouping words by length:
# 2 letters: is, an
# 3 letters: cat, dog, sun
# 4 letters: love, code


# with open("first.txt", "w") as myfile:
#     myfile.write("Later, the stork decided jumped to return the favor. She invited the fox to her house and served a delicious meal in a tall, narrow-necked jar. The stork was able to enjoy her food by dipping her beak into the jar, but the fox could not reach the food and went home hungry.")

# length_dict={}

# with open("first.txt", "r") as myfile:
#     text = myfile.read().lower().replace(".", "").replace(",", "")
#     words = text.split()
#     for word in words:
#         l = len(word)
#         if l not in length_dict:
#             length_dict[l] = []
#         length_dict[l].append(word)


# with open("first.text", "w") as myfile:
#     for length in sorted(length_dict.keys()):
#         myfile.write(str(length) + " letters: " + ", ".join(length_dict[length]) + "\n")



# 4)Transfer data from one file to another file using a loop:

with open ("first.txt","w") as myfile:
    myfile.write("Content refers to any information—such as text, images, videos, or audio—created and shared to inform, entertain, or engage an audience online. Common examples include blog posts, infographics, social media posts, and videos. Effective content is often original, answers a question, is properly formatted and sourced, and is easy to consume")

with open("first.text","w") as myfile:
    myfile.read("first.txt","r")
    myfile.close
