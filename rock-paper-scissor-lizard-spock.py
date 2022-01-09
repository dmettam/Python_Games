"""
simple game application 

Created on Fri Jan 7
@author: デイン　メッタム 
"""

from random import randint
from tkinter import * 

root = Tk() 
root.title("Rock Paper Scissors Lizard Spock")

e = Entry(root, width=35, borderwidth=3) 
e.grid(row=0, column=1, columnspan=3, padx=10, pady=10) 

def myClick():
    myLabel = Label(root, text="You clicked a button.", fg="green") 
    myLabel.pack() 

#create a list of play options
t = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]


#set player to False
player = False 

#while player == False:
#set player to True
def shoot(player): 
    #assign a random play to the computer
    computer = t[randint(0,4)]
    current = e.get()
    e.delete(0, END) 
    
    #player = input("Rock, Paper, Scissors, Lizard, Spock, exit? ") 
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
    computer = t[randint(0,2)]


#create buttons
rockButton = Button(root, text="ROCK", width=25, command=lambda: shoot("Rock")) 
paperButton = Button(root, text="PAPER", width=25, command=lambda: shoot("Paper")) 
scissorsButton = Button(root, text="SCISSORS", width=25, command=lambda: shoot("Scissors")) 
lizardButton = Button(root, text="LIZARD", width=25, command=lambda: shoot("Lizard"))
spockButton = Button(root, text="SPOCK", width=25, command=lambda: shoot("Spock")) 


#place buttons
rockButton.grid(row=1,column=0)
paperButton.grid(row=1,column=1)
scissorsButton.grid(row=1,column=2)
lizardButton.grid(row=1,column=3)
spockButton.grid(row=1,column=4)


root.mainloop() 