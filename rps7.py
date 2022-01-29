# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 14:08:34 2022

@author: Dane Mettam (デイン　メッタム)
"""

from random import randint
from tkinter import * 
from decision_tree import * 

root = Tk() 
root.title("RPS")

# create a rps7 frame 
rps7 = LabelFrame(root, text="RPS7", padx=50, pady=50) 
rps7.pack(padx=10, pady=10) 

e = Entry(rps7, width=35, borderwidth=3) 
e.grid(row=0, column=1, columnspan=6, padx=10, pady=10) 

#create a list of play options
t = ["Rock", "Paper", "Scissors", "Fire", "Water", "Air", "Sponge"]
     

#set player to False
player = False 

#while player == False:
#set player to True
# move this function to the game_gui script for this file to call 
def shoot(player): 
    #assign a random play to the computer
    computer = t[randint(0,6)]
    current = e.get()
    e.delete(0, END) 
    decision_tree(player, computer, e) 
    

#create buttons
rockButton = Button(rps7, text="ROCK", width=25, command=lambda: shoot("Rock")) 
paperButton = Button(rps7, text="PAPER", width=25, command=lambda: shoot("Paper")) 
scissorsButton = Button(rps7, text="SCISSORS", width=25, command=lambda: shoot("Scissors")) 
fireButton = Button(rps7, text="FIRE", width=25, command=lambda: shoot("Fire"))
spongeButton = Button(rps7, text="SPONGE", width=25, command=lambda: shoot("Sponge")) 
waterButton = Button(rps7, text="WATER", width=25, command=lambda: shoot("Water")) 
airButton = Button(rps7, text="AIR", width=25, command=lambda: shoot("Air")) 
quitButton = Button(rps7, text="EXIT PROGRAM", width=50, command=root.destroy) 

#place buttons
rockButton.grid(row=1,column=1, columnspan=2)
paperButton.grid(row=1,column=3, columnspan=2)
scissorsButton.grid(row=1,column=5, columnspan=2)
fireButton.grid(row=2,column=0, columnspan=2)
waterButton.grid(row=2,column=2, columnspan=2)
airButton.grid(row=2,column=4, columnspan=2)
spongeButton.grid(row=2,column=6, columnspan=2)
quitButton.grid(row=3, column=2, columnspan=4, pady=10)




root.mainloop() 