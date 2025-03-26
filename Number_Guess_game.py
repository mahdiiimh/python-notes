from random import randint
more_play = 'yes'
players = {}
while more_play == 'yes':
    count = 0
    computer_number = randint(1,20)
    user_guess = -1
    while user_guess != computer_number :
        user_guess = int(input("please enter your guess : "))
        count += 1
        if user_guess > computer_number:
            print("ohh you go to high. ")
        elif computer_number > user_guess:
            print("my number is bigger than yours. ")
        else :
            print(f"you got it,my number is {computer_number},you have {count} tries to find the answer")
    player_name = input("please enter your name : ")
    if players.get(player_name,0) == 0:
        players[player_name]= count
    else:
        players[player_name] = count
    more_play = input("Do you want to play more? (yes/no)")
print(players)
best = min(players,key=players.get)
print(f"best player is {best} with {players[best]} tries.")