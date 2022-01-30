"""
Rock Paper Scissors Lizard Spock  

Created on Fri Jan 7
@author: Dane Mettam (デイン　メッタム)
"""

from random import randint
from tkinter import *  
from decision_tree import *
import PIL as p 
import PIL.ImageTk as ptk
import PIL.Image 

fPath='C:/Users/danea/Documents/Python Scripts/Games/' 

root = Tk()
root.title("Rock Paper Scissors App")
root.iconbitmap(fPath + 'images/RPS/icons/poke.ico')

def rps():
    rpsRoot = Tk() 
    rpsRoot.title("Rock Paper Scissors")
    rpsRoot.iconbitmap(fPath + 'images/RPS/icons/Rock-paper-scissors.ico') 
    
    # create a frame 
    frame = LabelFrame(rpsRoot, text="Rock Paper Scissors...", padx=50, pady=50) 
    frame.pack(padx=10, pady=10) 
    
    e = Entry(frame, width=35, borderwidth=3) 
    e.grid(row=0, column=0, columnspan=3, padx=10, pady=5) 
    
    #create a list of play options
    t = ["Rock", "Paper", "Scissors"]
    
    #set player to False
    player = False 
    
    #while player == False:
    #set player to True
    # move this function to the game_gui script for this file to call 
    def shoot(player): 
        #assign a random play to the computer
        computer = t[randint(0,2)]
        current = e.get()
        e.delete(0, END) 
        decision_tree(player, computer, e)    
    
    #create buttons
    rockButton = Button(frame, text="ROCK", width=25, command=lambda: shoot("Rock")) 
    paperButton = Button(frame, text="PAPER", width=25, command=lambda: shoot("Paper")) 
    scissorsButton = Button(frame, text="SCISSORS", width=25, command=lambda: shoot("Scissors")) 
    quitButton = Button(frame, text="EXIT PROGRAM", width=50, command=rpsRoot.destroy) 
    
    #place buttons
    rockButton.grid(row=1,column=0)
    paperButton.grid(row=1,column=1)
    scissorsButton.grid(row=1,column=2)
    quitButton.grid(row=2, column=1, columnspan=2, pady=5)
    
    rpsRoot.mainloop() 

def rps5(): 
    rps5Root = Tk()  
    rps5Root.title("Rock Paper Scissors Lizard Spock")
    rps5Root.iconbitmap(fPath + 'images/RPS/icons/RPSLS.ico') 
    
    # create a frame 
    frame = LabelFrame(rps5Root, text="Rock Paper Scissors Lizard Spock...", padx=50, pady=50) 
    frame.pack(padx=10, pady=10) 
    
    e = Entry(frame, width=35, borderwidth=3) 
    e.grid(row=0, column=1, columnspan=3, padx=10, pady=10) 
    
    #create a list of play options
    t = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    
    #set player to False
    player = False 
    
    #while player == False:
    #set player to True
    # move this function to the game_gui script for this file to call 
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
    quitButton = Button(frame, text="EXIT PROGRAM", width=50, command=rps5Root.destroy) 
    
    #place buttons
    rockButton.grid(row=1,column=0)
    paperButton.grid(row=1,column=1)
    scissorsButton.grid(row=1,column=2)
    lizardButton.grid(row=1,column=3)
    spockButton.grid(row=1,column=4)
    quitButton.grid(row=2, column=1, columnspan=3, pady=10)
    
    rps5Root.mainloop() 
    
    
def rps7():
    rps7Root = Tk() 
    rps7Root.title("Rock Paper Scissors Fire Water Air Sponge")
    rps7Root.iconbitmap(fPath + 'images/RPS/icons/rpsfwas.ico') 
    
    # create a frame 
    frame = LabelFrame(rps7Root, text="RPS7", padx=50, pady=50) 
    frame.pack(padx=10, pady=10) 
    
    e = Entry(frame, width=35, borderwidth=3) 
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
    rockButton = Button(frame, text="ROCK", width=25, command=lambda: shoot("Rock")) 
    paperButton = Button(frame, text="PAPER", width=25, command=lambda: shoot("Paper")) 
    scissorsButton = Button(frame, text="SCISSORS", width=25, command=lambda: shoot("Scissors")) 
    fireButton = Button(frame, text="FIRE", width=25, command=lambda: shoot("Fire"))
    spongeButton = Button(frame, text="SPONGE", width=25, command=lambda: shoot("Sponge")) 
    waterButton = Button(frame, text="WATER", width=25, command=lambda: shoot("Water")) 
    airButton = Button(frame, text="AIR", width=25, command=lambda: shoot("Air")) 
    quitButton = Button(frame, text="EXIT PROGRAM", width=50, command=rps7Root.destroy) 
    
    #place buttons
    rockButton.grid(row=1,column=1, columnspan=2)
    paperButton.grid(row=1,column=3, columnspan=2)
    scissorsButton.grid(row=1,column=5, columnspan=2)
    fireButton.grid(row=2,column=0, columnspan=2)
    waterButton.grid(row=2,column=2, columnspan=2)
    airButton.grid(row=2,column=4, columnspan=2)
    spongeButton.grid(row=2,column=6, columnspan=2)
    quitButton.grid(row=3, column=2, columnspan=4, pady=10)

    rps7Root.mainloop() 
    
def element():
    ele = Tk()  
    ele.title("カスミちゃんはかわいいですね。")
    ele.iconbitmap(fPath + 'images/RPS/icons/poke.ico') /RPS
    
    # create a frame 
    frame = LabelFrame(ele, text="Gotta Catch'em All", padx=50, pady=50) 
    frame.pack(padx=10, pady=10) 
    
    e = Entry(frame, width=35, borderwidth=3) 
    e.grid(row=0, column=1, columnspan=3, padx=10, pady=10) 
    ele.mainloop() 

my_img1 = ptk.PhotoImage(p.Image.open(fPath + "images/RPS/Rock-paper-scissors.png").resize((200,200))) # original
my_img2 = ptk.PhotoImage(p.Image.open(fPath + "images/RPS/RPSLS.png").resize((200,200))) #RPSLS
my_img3 = ptk.PhotoImage(p.Image.open(fPath + "images/RPS/rpsfwas.jpg").resize((200,200))) #fire water air sponge 
my_img4 = ptk.PhotoImage(p.Image.open(fPath + "images/RPS/poke.png").resize((200,200))) #pokemon


# Add game buttons 
button1 = Button(root, image=my_img1, command=rps) # original rps
button2 = Button(root, image=my_img2, command=rps5) # rps with spock and lizard
button3 = Button(root, image=my_img3, command=rps7) # rps with fire, air, and sponge
button4 = Button(root, image=my_img4, command=element) # rps replaced with pokemon elements
button5 = Button(root, text="Terminate Program", command=root.destroy) # closes program 
button1.grid(row=0, column=0, padx=10, pady=10) # original rps 
button2.grid(row=0, column=1, padx=10, pady=10) # rps with spock and lizard 
button3.grid(row=1, column=0, padx=10, pady=10) # rps with fire, air, and sponge
button4.grid(row=1, column=1, padx=10, pady=10) # rps replaced with pokemon elements 
button5.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

'''
# RPS game selection buttons
btn0 = Button(root, text="Open rps window", command=rps) # original rps
btn1 = Button(root, text="Open rps5 window", command=rps5) # rps with spock and lizard
btn2 = Button(root, text="Open rps7 window", command=rps7) # rps with fire, air, and sponge
btn3 = Button(root, text="Open element window", command=element) # rps replaced with pokemon elements 
btn4 = Button(root, text="Terminate Program", command=root.destroy) # closes program 

btn0.grid(row=0, column=0) # original rps
btn1.grid(row=0, column=1) # rps with spock and lizard
btn2.grid(row=1, column=0) # rps with fire, air, and sponge
btn3.grid(row=1, column=1) # rps replaced with pokemon elements 
btn4.grid(row=2, column=0, columnspan=2) # closes program 
'''
mainloop()