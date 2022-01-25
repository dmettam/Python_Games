# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 05:15:37 2022

@author: Dane Mettam (デイン　メッタム)
"""

def decision_tree(player, computer, e): 
    #assign a random play to the computer
    #computer = t[randint(0,4)]
    #current = e.get()
    #e.delete(0, END)

    if player == computer:
        e.insert(0, str("Tie!")) 
    elif player == "Rock":
        if computer == "Paper": 
            e.insert(0, str("You lose... " + computer + " covers " + player))
        elif computer == "Spock":
            e.insert(0, str("You lose... " + computer + " vaporizes " + player))
        elif computer == "Lizard":
            e.insert(0, str("You Win! " + player + " crushes " + computer))
        else:
            e.insert(0, str("You win! " + player  + " smashes " + computer))
    elif player == "Paper":
        if computer == "Scissors":
            e.insert(0, str("You lose... " + computer + " cuts " + player))
        elif computer == "Spock":
            e.insert(0, str("You win! " + player + " disproves " + computer))
        elif computer == "Lizard":
            e.insert(0, str("You lose... " + computer + " eats " + player))
        else:
            e.insert(0, str("You win! " + player + " covers " + computer))
    elif player == "Scissors":
        if computer == "Rock":
            e.insert(0, str("You lose... " + computer + " smashes " + player))
        elif computer == "Spock":
            e.insert(0, str("You lose... " + computer + " uses " + player))
        elif computer == "Lizard":
            e.insert(0, str("You win! " + player + " decapitates " + computer))
        else:
            e.insert(0, str("You win! " + player + " cuts " + computer))
    elif player == "Lizard":
        if computer == "Spock":
            e.insert(0, str("You win! " + player + " poisons " + computer))
        elif computer == "Paper":
            e.insert(0, str("You win! " + player + " eats " + computer))
        elif computer == "Scissors":
            e.insert(0, str("You lose... " + computer + " decapitates " + player))
        else:
            e.insert(0, str("You lose... " + computer + " crushes " + player))
    elif player == "Spock":
        if computer == "Lizard":
            e.insert(0, str("You lose... " + computer + " poisons " + player))
        elif computer == "Paper":
            e.insert(0, str("You lose... " + computer + " disproves " + player))
        elif computer == "Scissors":
            e.insert(0, str("You win! " + player + " uses " + computer))
        else: 
            e.insert(0, str("You win! " + player + " vaporizes " + computer))
    elif player == "exit": 
        print("game over") 
    else:
        print("That's not a valid play. Check your spelling!")
        e.insert(0, str("That's not a valid play. Check your spelling!")) 
    #player was set to True, but we want it to be False so the loop continues
    player = False
    #computer = t[randint(0,2)]