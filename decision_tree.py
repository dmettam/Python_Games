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
        elif computer == "Fire":
            e.insert(0, str("You Win! " + player + " pounds out " + computer))
        elif computer == "Water":
            e.insert(0, str("You lose... " + computer + " erodes " + player))
        elif computer == "Sponge":
            e.insert(0, str("You Win! " + player + " crushes " + computer))
        elif computer == "Air":
            e.insert(0, str("You lose... " + computer + " erodes " + player))
        else:
            e.insert(0, str("You win! " + player  + " smashes " + computer))
    elif player == "Paper":
        if computer == "Scissors":
            e.insert(0, str("You lose... " + computer + " cuts " + player))
        elif computer == "Spock":
            e.insert(0, str("You win! " + player + " disproves " + computer))
        elif computer == "Lizard":
            e.insert(0, str("You lose... " + computer + " eats " + player))
        elif computer == "Fire":
            e.insert(0, str("You lose... " + computer + " burns " + player))
        elif computer == "Water":
            e.insert(0, str("You Win! " + player + " floats on " + computer))
        elif computer == "Sponge":
            e.insert(0, str("You lose... " + computer + " soaks " + player))
        elif computer == "Air":
            e.insert(0, str("You Win! " + player + " fans " + computer))
        else:
            e.insert(0, str("You win! " + player + " covers " + computer))
    elif player == "Scissors":
        if computer == "Rock":
            e.insert(0, str("You lose... " + computer + " smashes " + player))
        elif computer == "Spock":
            e.insert(0, str("You lose... " + computer + " uses " + player))
        elif computer == "Lizard":
            e.insert(0, str("You win! " + player + " decapitates " + computer))
        elif computer == "Fire":
            e.insert(0, str("You lose... " + computer + " melts " + player))
        elif computer == "Water":
            e.insert(0, str("You lose... " + computer + " rusts " + player))
        elif computer == "Sponge":
            e.insert(0, str("You Win! " + player + " cuts " + computer))
        elif computer == "Air":
            e.insert(0, str("You lose... " + computer + " swishes through " + player))
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
    elif player == "Fire": 
        if computer == "Rock":
            e.insert(0, str("You lose... " + computer + " pounds out " + player))
        elif computer == "Paper":
            e.insert(0, str("You Win " + player + " burns " + computer))
        elif computer == "Scissors":
            e.insert(0, str("You win! " + player + " melts " + computer))
        elif computer == "Water":
            e.insert(0, str("You lose... " + computer + " puts out " + player))
        elif computer == "Sponge":
            e.insert(0, str("You Win! " + player + " burns " + computer))
        elif computer == "Air":
            e.insert(0, str("You lose... " + computer + " blows out " + player))
    elif player == "Water": 
        if computer == "Rock":
            e.insert(0, str("You Win! " + player + " erodes " + computer))
        elif computer == "Paper":
            e.insert(0, str("You lose... " + computer + " floats on " + player))
        elif computer == "Scissors":
            e.insert(0, str("You win! " + player + " rusts " + computer))
        elif computer == "Fire":
            e.insert(0, str("You Win! " + player + " puts out " + computer))
        elif computer == "Sponge":
            e.insert(0, str("You lose... " + computer + " absorbs " + player))
        elif computer == "Air":
            e.insert(0, str("You lose... " + computer + " evaporates " + player))
    elif player == "Air": 
        if computer == "Rock":
            e.insert(0, str("You Wins! " + player + " erodes " + computer))
        elif computer == "Paper":
            e.insert(0, str("You lose... " + computer + " fans " + player))
        elif computer == "Scissors":
            e.insert(0, str("You win! " + player + " swishes through " + computer))
        elif computer == "Fire":
            e.insert(0, str("You Win! " + computer + " blows out " + player))
        elif computer == "Water":
            e.insert(0, str("You Win! " + computer + " evaporates " + player))
        elif computer == "Sponge":
            e.insert(0, str("You Win! " + player + " uses " + computer + " pockets"))
    elif player == "Sponge":#############################
        if computer == "Rock":
            e.insert(0, str("You lose... " + computer + " smashes " + player))
        elif computer == "Paper":
            e.insert(0, str("You Win! " + computer + " soaks " + player))
        elif computer == "Scissors":
            e.insert(0, str("You win! " + player + " cuts " + computer))
        elif computer == "Fire":
            e.insert(0, str("You lose... " + computer + " burns " + player))
        elif computer == "Water":
            e.insert(0, str("You Win! " + computer + " absorbs " + player))
        elif computer == "Air":
            e.insert(0, str("You lose... " + computer + " uses " + player + " pockets"))
    elif player == "exit": 
        print("game over") 
    else:
        print("That's not a valid play. Check your spelling!")
        e.insert(0, str("That's not a valid play. Check your spelling!")) 
    #player was set to True, but we want it to be False so the loop continues
    player = False
    #computer = t[randint(0,2)]