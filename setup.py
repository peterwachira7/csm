from tkinter import *
#from PIL import Image, ImageTK
import os
import sys
import tkinter.messagebox
from willow.image import Image

#from tkFileDialog import askopenfilename

def exit():
    result = tkinter.messagebox.askyesno("QUIT DIALOG","Are you Sure You Want To Quit?")
    if result == True:
        root.destroy()
    
    
def login_action():
    root.destroy()
    import login1
    

def mouseEntered(event):
    button = event.widget
    button.config(text = "Click Here To Login")

def mouseExited(event):
    button = event.widget
    button.config(text = "LOGIN")

def mouseEntered_1(event):
    button = event.widget
    button.config(text = "Click Here To Quit")

def mouseExited_1(event):
    button = event.widget
    button.config(text = "EXIT")

def main():
    global root
    root = Tk()

    #root.iconbitmap('new.ico')
    root.geometry('1200x800')
    root.title('Welcome To C . S . M')
    
    #menu = Menu(root)
    #root.config(menu=menu)
   #menu.add_cascade(label="File", menu =filemenu)
    
    Label(root, text="CHEP SACCO MANAGEMENT SYSTEM", bg="black", fg="white", height = 4, width = 50).pack(fill=X)
    myButton = Button(root, text="LOGIN", width =15, height = 3, bg = "green", command = login_action)
    myButton.bind("<Enter>",mouseEntered)
    myButton.bind("<Leave>",mouseExited)
    myButton.pack(side=TOP)
    b = Button(root, text = "EXIT", bg="red", fg="white", command=exit, width = 15, height = 3)
    b.bind("<Enter>",mouseEntered_1)
    b.bind("<Leave>",mouseExited_1)
    b.pack(side=BOTTOM)
    

    root.mainloop()

main()
