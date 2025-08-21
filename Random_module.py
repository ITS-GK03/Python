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

# brands = ["ktm", "yamaha", "royal", "ducati", "bajaj", "honda", "hero", "kawasaki"]

# def play_game():
#     my_brand = random.choice(brands)
#     attempts = 5

#     while attempts > 0:
#         user_brand = input("Guess the bike brand: ").strip().lower()

#         if user_brand == my_brand:
#             print("Your guess is correct! You passed the game browww ")
#             return True  
#         else:
#             attempts -= 1
#             print(f" Wrong guess! You have {attempts} attempt(s) left.")

#     print(f"Out of attempts! The correct brand was: {my_brand}")
#     return False  


# def main():
#     while True:
#         play_game()
#         play_again = input("Do you want to play again? (yes/no): ").strip().lower()
#         if play_again != 'yes':
#             print(" Thanks for playing! Come back again.")
#             break


# if __name__ == "__main__":
#     main()




# 2. ROCK, PAPER, SCISSORS:

# game = ["Rock", "Paper", "Scissor"]
# play_again = "Yes"

# while play_again == "Yes":
#     player1_win = 0
#     player2_win = 0
#     print("Game Started! Best of 3 Wins.")
#     print("Select your item from:", game)
#     while player1_win < 3 and player2_win < 3:
#         Player1 = random.choice(game)   
#         Player2 = input("\nEnter your choice (Rock/Paper/Scissor): ").lower()
#         print(f"Player1 chose: {Player1}, Player2 chose: {Player2}")

#         if Player1 == Player2:
#             print("It's a Tie!")
        
#         elif Player1 == "Rock" and Player2 == "Paper":
#             print("Paper beats Rock, {Player2 wins this round}")
#             player2_win += 1

#         elif Player1 == "Paper" and Player2 == "Rock":
#             print("Paper beats Rock, Player1 wins this round")
#             player1_win += 1

#         elif Player1 == "Paper" and Player2 == "Scissor":
#             print("Scissor beats Paper, Player2 wins this round")
#             player2_win += 1

#         elif Player1 == "Scissor" and Player2 == "Paper":
#             print("Scissor beats Paper, Player1 wins this round")
#             player1_win += 1

#         elif Player1 == "Rock" and Player2 == "Scissor":
#             print("Rock beats Scissor, Player1 wins this round")
#             player1_win += 1

#         elif Player1 == "Scissor" and Player2 == "Rock":
#             print("Rock beats Scissor, Player2 wins this round")
#             player2_win += 1

#         print(f"Score = Player1: {player1_win}, Player2: {player2_win}")

    
#     if player1_win > player2_win:
#         print("\n Player1 wins the Game!")
#     else:
#         print("\n Player2 win the Game!")
#     play_again = input("\nDo you want to play again? (Yes/No): ").lower()




# 3. TREASURE HUNT:


# locations = ["Cave", "River", "Mountain", "Forest", "Desert"]

# hints = {
#     "Cave": "It's dark and hidden... but maybe not here!",
#     "River": "Treasure is not near water.",
#     "Mountain": "It's not that high up!",
#     "Forest": "Too many trees around, treasure might not be here.",
#     "Desert": "Treasure is in a dry place."
# }

# max_attempts = 3

# play_again = "Yes"
# while play_again.lower() == "yes":
#     treasure = random.choice(locations)
#     print("\n Game started!")
#     print("Possible locations:", locations)

#     attempts = 0
#     while attempts < max_attempts:
#         player = input("Enter the location where the treasure is hidden: ").strip().capitalize()
#         attempts += 1

#         if player == treasure:
#             print(" You found the treasure! You won the game!")
#             break
#         else:
#             if attempts < max_attempts:
#                 print(" Wrong guess! Here's a hint:", hints[treasure])
#             else:
#                 print(f" No attempts left! You lost the game. The treasure was in {treasure}.")

#     play_again = input("Do you want to play again? (Yes/No): ").strip()


