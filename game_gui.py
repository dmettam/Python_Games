# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 03:53:11 2022

@author: Dane Mettam (デイン　メッタム)
"""

import tkinter as tkr 
import PIL as p 
import PIL.ImageTk as ptk
import PIL.Image 
import rock_paper_scissor_lizard_spock as rps5
#import rps7 

fPath='C:/Users/danea/Documents/Python Scripts/Games/' 


root = tkr.Tk()
root.title("Rock Paper Scissor Type Games")
root.iconbitmap(fPath + '/images/Pokemon/tumblr_pbrevojubz_X7Y_icon.ico')
root.geometry("450x450") 

      
def rps_selector(selection): 
    if selection == 1:
        rps5.openrps 
        command=openrps
        return() 
    elif selection == 2: 
        import rps7
    elif selection == 3: 
        import rps7.py
    else:
        import rps7.py 


my_img1 = ptk.PhotoImage(p.Image.open(fPath + "images/RPS/RPSLS.png").resize((200,200))) #RPSLS
my_img2 = ptk.PhotoImage(p.Image.open(fPath + "images/RPS/rpsfwas.jpg").resize((200,200))) #fire water air sponge 
my_img3 = ptk.PhotoImage(p.Image.open(fPath + "images/RPS/RPS_mod.jpg").resize((200,200))) #RPSLS w/ spiderman, batman wizard & glock 
my_img4 = ptk.PhotoImage(p.Image.open(fPath + "images/RPS/Rock-paper-scissors.png").resize((200,200))) # original

"""
#photo1 = ptk.PhotoImage(my_img1) #there is an issue with this line
#label1 = tkr.Label(root, image=photo1)
label1 = tkr.Label(root, image=my_img1)
label2 = tkr.Label(root, image=my_img2)
label3 = tkr.Label(root, image=my_img3)
label4 = tkr.Label(root, image=my_img4)

label1.grid(row=0, column=1, padx=10, pady=10)  
label2.grid(row=0, column=0, padx=10, pady=10)  
label3.grid(row=1, column=0, padx=10, pady=10)  
label4.grid(row=1, column=1, padx=10, pady=10)  
"""

#rps_btn1 = tkr.Button(root, image=my_img1, command=test)
button1 = tkr.Button(root, image=my_img1, command=lambda: rps_selector(1))
button2 = tkr.Button(root, image=my_img2, command=lambda: rps_selector(2))
button3 = tkr.Button(root, image=my_img3, command=lambda: rps_selector(3))
button4 = tkr.Button(root, image=my_img4, command=lambda: rps_selector(4))

button1.grid(row=1, column=1, padx=10, pady=10)  
button2.grid(row=1, column=0, padx=10, pady=10)  
button3.grid(row=2, column=0, padx=10, pady=10)  
button4.grid(row=2, column=1, padx=10, pady=10) 


#rps_btn1.grid(row=2, column=0)
#test_label = tkr.Label(root, text='') 
#test_label.grid(row=3, column=0) 


'''
def open():
    global my_img 
    top = Toplevel() 
    top.title("カスミ")
    top.iconbitmap('C:/Users/danea/Documents/Python Scripts/Tkinter Tutorial/images/tumblr_pbrevojubz_X7Y_icon.ico')
    lbl = Label(top, text="whaaaat！　カスミちゃん可愛いね。").pack() 
    my_img = ImageTk.PhotoImage(Image.open("images/pokemon-cosplay-misty.jpg"))
    my_label = Label(top, image=my_img).pack() 
    btn2 = Button(top, text="Close Window", command=top.destroy).pack()  
'''    
        
#btn = Button(root, text="Open 2nd window", command=open).pack()  

#my_img1_label = Label(root, image-my_img1) 
#my_img1_label.image = img 
#label.pack()

#my_btn = Button(root, text="open file", command=open).pack()  


root.mainloop() 