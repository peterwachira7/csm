from tkinter import *
from tkinter import messagebox,Label,Button, FALSE,Tk,Entry
import os
import sys

root = Tk()
root.geometry('380x400')
label_1=Label(root, text = "Username").grid(row = 0, sticky = E)
label_2 = Label(root, text = "Password").grid(row = 1, sticky = E)

username = "root" #that's the given username
password = "toor" #that's the given password
#username entry
username_entry = Entry(root)
username_entry.grid(row = 0, column =6)
#password entry
password_entry = Entry(root, show='*')
password_entry.grid(row = 1, column =6)
def trylogin():
    if username == username_entry.get() and password == password_entry.get():
        messagebox.showinfo("VERIFIED","You are now logged in")
        os.system('home.py')
        root.destroy()
    else:
        messagebox.showerror("FAILED ","Wrong Username or Password")
button = Button(root, text="LOGIN", command = trylogin, height = 3, width = 10, bg = "green")
button.grid(row = 6, column = 6) #App starter
root.mainloop()
