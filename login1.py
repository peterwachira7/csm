from tkinter import *
from tkinter import messagebox,Label,Button, FALSE,Tk,Entry
import os
import sys

global root
root = Tk()
root.title('Login')
root.geometry('380x400')
root.configure(bg = 'navy blue')
label_1=Label(root, text = "Username", fg = 'blue', width = 10, height = 1).place(relx = 0.1, rely = 0.03)
label_2 = Label(root, text = "Password", fg = 'red', width = 10, height = 1).place(relx = 0.1, rely = 0.10)

username = "root" #that's the given username
password = "toor" #that's the given password
#username entry
username_entry = Entry(root)
username_entry.place(relx = 0.4, rely = 0.03)
#password entry
password_entry = Entry(root, show='*',)
password_entry.place(relx = 0.4, rely = 0.10)
def trylogin():
    if username == username_entry.get() and password == password_entry.get():
        messagebox.showinfo("VERIFIED","You are now logged in")
        root.destroy()
        import home
        
    else:
        messagebox.showerror("FAILED ","Wrong Username or Password")
        messagebox.showinfo("TRY AGAIN", "Try Again Later")
        root.destroy()
        import setup
        
button = Button(root, text="LOGIN", command = trylogin, height = 3, width = 10, bg = "green")
button.place(relx = 0.3, rely = 0.4, anchor =W) #App starter
root.mainloop()
