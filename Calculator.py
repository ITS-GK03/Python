# CAL:

# def cal_add(g,k):
#     oper=g+k
#     print(oper)


# def cal_sub(g,k):
#     oper=g-k
#     print(oper)


# def cal_mul(x,y):
#     oprea=x*y
#     print(oprea)


# def cal_div(n,s):
#     opreat=n/s
#     print(opreat)







for attempts_game in range(attempt):
    if user_brand==my_brand:
        print("Your guess is correct you passed the game browww")
        print("Do you want to play another game")
        
        play_again = 'yes'
        while play_again.lower() == 'yes':
            attempts_game()
            play_again = input("Do you want to play again? (yes/no): ")
        print("Thanks for playing!")
        break

        
    elif user_brand!=my_brand:
        remaining=attempt-attempts_game-1
        print(f"You have {remaining} attempt(s) left")
        if user_brand==my_brand:
            print("Your guess is correct you passed the game browww")
            print("Do you want to play another game") 
        if remaining==0:
             print("Adhu avalo dhan time mudinji pochi, nee kelambu")
