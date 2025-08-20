# RANDOM MODULE:

import random

# mylist=[1,2,3,4,5,6,7,8,9,10]
# res=random.choice(mylist)
# print(res)


# print(random.randrange(7,19))

# print(random.random())


# my_list = ["ktm", "yamaha", "re"]
# random.shuffle(my_list)
# print(my_list)


# print(random.uniform(45,75))





# 1.RANDOM PUZZLE TASK:

Chocolates=["5 Star","Diary Milk","Milky Bar","Crispello","KitKat","Perk",]

Total_Attempts=5
Play_again="Yes"
while Play_again=="Yes":
    Target=random.choice(Chocolates)
    print("Guess a Chocolate from the list:",Chocolates)
    Attempt=0
    for i in range(1,Total_Attempts+1):
        Player=input("Enter the choclate in the list:")
        Attempt+=1
        if Target==Player:
            print("You Guessed correctly you won the Game")
            break
        elif Attempt<Total_Attempts:
            print("wrongly Guessed, try again")
        else:
            print(f"No attempts left you Lost the Game, The correct answer is {Target}")

    Play_again=input("Do you want to play this Game again(Yes/No):")
    
            

    
        
    
