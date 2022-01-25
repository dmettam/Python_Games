"""
Rock Paper Scissors Lizard Spock  

Created on Fri Jan 7
@author: Dane Mettam (デイン　メッタム)
"""

from random import randint
from tkinter import * 
from decision_tree import * 

root = Tk() 
root.title("Rock Paper Scissors Lizard Spock")

# create a frame 
frame = LabelFrame(root, text="Rock Paper Scissors Lizard Spock...", padx=50, pady=50) 
frame.pack(padx=10, pady=10) 

e = Entry(frame, width=35, borderwidth=3) 
e.grid(row=0, column=1, columnspan=3, padx=10, pady=10) 

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
    decision_tree(player, computer, e) 
    



#create buttons
rockButton = Button(frame, text="ROCK", width=25, command=lambda: shoot("Rock")) 
paperButton = Button(frame, text="PAPER", width=25, command=lambda: shoot("Paper")) 
scissorsButton = Button(frame, text="SCISSORS", width=25, command=lambda: shoot("Scissors")) 
lizardButton = Button(frame, text="LIZARD", width=25, command=lambda: shoot("Lizard"))
spockButton = Button(frame, text="SPOCK", width=25, command=lambda: shoot("Spock")) 
quitButton = Button(frame, text="EXIT PROGRAM", width=50, command=root.destroy) 

#place buttons
rockButton.grid(row=1,column=0)
paperButton.grid(row=1,column=1)
scissorsButton.grid(row=1,column=2)
lizardButton.grid(row=1,column=3)
spockButton.grid(row=1,column=4)
quitButton.grid(row=2, column=1, columnspan=3, pady=10)




root.mainloop() 