from tkinter import *
#from PIL import Image, ImageTK
import os
import sys
import tkinter.messagebox
from willow.image import Image

#from tkFileDialog import askopenfilename

def exit():
    tkinter.messagebox.showwarning("QUIT DIALOG","Are you Sure You Want To Quit?")
    root.destroy()
    
def login_action():
    os.system('login1.py')
    root.destroy()

def mouseEntered(event):
    button = event.widget
    button.config(text = "Click Here To Login")

def mouseExited(event):
    button = event.widget
    button.config(text = "LOGIN")

def main():
    global root
    root = Tk()

    #root.iconbitmap('new.ico')
    root.geometry('1200x800')
    root.title('C S M ')
    
    #menu = Menu(root)
    #root.config(menu=menu)
   #menu.add_cascade(label="File", menu =filemenu)
    
    Label(root, text="CHEP SACCO MANAGEMENT SYSTEM", bg="black", fg="white", height = 4, width = 50).pack(fill=X)
    myButton = Button(root, text="LOGIN", width =15, height = 3, bg = "green", command = login_action)
    myButton.bind("<Enter>",mouseEntered)
    myButton.bind("<Leave>",mouseExited)
    myButton.pack(side=TOP)
    b = Button(root, text = "EXIT", bg="red", fg="white", command=exit, width = 10, height = 3)
    b.pack(side=BOTTOM)
    

    root.mainloop()

main()
