import numpy as np
import random

while True:

    user_action = input("Enter a choice (rock, paper, scissors): ")

    print ('user choice was ' + user_action)

    number = np.random.randint(1,4)

    if number == 1 :
        computer_Choice = "rock"
    elif number == 2 :
        computer_Choice = "paper"
    else :
        computer_Choice = "scissors"

    print ('computer choice was ' + computer_Choice)

    if user_action == computer_Choice :
        print ("It's a drawer!")
    elif user_action == 'rock' and computer_Choice == 'scissors' : 
        print ('You win!')
    elif user_action == 'paper' and computer_Choice == 'rock' :
        print ('You win!')
    elif user_action == 'scissors' and computer_Choice == 'paper' :
        print ('You win!')
    else :
        print ('Computer wins!')

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
            break