import random
def winorlose (player , computer, lifes ):
    if player == computer:
        print("tied")
        lifes = lifes 
        return lifes
    elif player == "Rock" and computer == "Scissors":
        print("You win!")
        lifes = lifes
        return lifes
    elif player == "Scissors" and computer == "Rock":
        print("You lose!")
        lifes = lifes - 1
        return lifes  
    elif player == "Paper" and computer == "Rock":
        print("You win!")
        lifes = lifes
        # print("You have " +str(lifes) + " lifes")
        return lifes
    elif player == "Rock" and computer == "Paper":
        print("You lose!")
        lifes = lifes - 1
        # print("You have " +str(lifes) + " lifes")
        return lifes
    elif player == "Scissors" and computer == "Paper":
        print("You win!")
        lifes = lifes
        # print("You have " +str(lifes) + " lifes")
        return lifes
    elif player == "Paper" and computer == "Scissors":
        print("You lose!")
        lifes = lifes - 1
        # print("You have " +str(lifes) + " lifes")
        return lifes

def game():
    lifes = 3
    total = 0
    while lifes != 0 :
        choices = ["rock" , "paper" , "scissors"]
        player = None
        computer = random.choice(choices)
        player = input("Which one would you choose rock, paper, or scissors?: ")
        player = player.capitalize()
        computer = computer.capitalize()
        print(player)
        print(computer)
        lifes =  winorlose(player, computer, lifes)
        print("You have " +str(lifes) + " lifes")

game()
