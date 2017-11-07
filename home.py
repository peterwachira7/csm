from tkinter import*
import os
import  sys
import tkinter.messagebox
from willow import image
from threading import Thread

class home():

    global root
    root = Tk()
    root.configure(bg = 'orange')
    root.geometry('900x880')
    root.title('HOME',)
    
    label = Label(root, text = "W E L C O M E   T O   C S M " , font = 'HELVETICA 25' , bg = 'grey' )
    label.place(relx = 0.1, x = 100, rely = 0.1) 

    def _init_(self, master = None):
        self.master = master
        self.frame = Frame(master, width = 800, height = 960, relief = RAISED, bd = 4)
        
    def  register_vehicle():
        import register_vehicle
        
    def monitor_vehicle():
        import monitor


    def  logout():
        result0 = tkinter.messagebox.askyesno(' --LOG OUT--', 'Really want to log out?')
        if result0 == True:
            root.destroy()
            import setup          
        

    def quit_ask():
       result = tkinter.messagebox.askyesno(' Q U I T', 'Really Want To Quit?') 
       if result == True:
            root.destroy()
                   
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command = quit_ask)
    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...")
                             
        
    btn1 = Button(root,  text = "REGISTER VEHICLE",font = 'HELVETICA' 'bold' , fg = 'red',bg = 'green', command = register_vehicle,  height = 3, width = 30 )
    btn1.place(relx=0.1, rely=0.48 )

    btn2 = Button(root,  text = "MONITOR VEHICLE",font = 'HELVETICA' 'bold' , fg = 'red',bg = 'green', command = monitor_vehicle,  height = 3, width = 30)
    btn2.place(relx = 0.6, rely = 0.48) 

    btn3 = Button(root,  text = "LOG OUT",font = 'HELVETICA' 'bold' , fg = 'red',bg = 'green', command = logout,  height = 3, width = 10)
    btn3.place(relx = 0.1, rely = 0.8)
    
    btn4 = Button(root,  text = "QUIT",font = 'HELVETICA' 'bold' , fg = 'red',bg = 'green', command = quit_ask,  height = 3, width = 10)
    btn4.place(relx = 0.8, rely = 0.8) 
    root.mainloop()
