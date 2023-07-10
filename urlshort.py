#===============================Jatin's URL Shortner==========================

import pyshorteners
from tkinter import *
win = Tk()
win.geometry("700x400")
win.configure(bg="brown")

#---------------------------------Button Function----------------------------


def short():
    url = Entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)

    Entry2.insert(END,s)

#----------------------------Label for Entering  User Url--------------------


Label(win,text="Jatin's URL Shortner",font="impact 20",bg="black",fg="white").pack(fill="x")

#-----------------------------------Entry Box--------------------------------

Entry1 = Entry(win,font="10",bd=3,width=60)
Entry1.pack(pady=20)

#------------------------------------Button----------------------------------


Button(win,text="Click Here",font="impack 12 bold",bg="green",fg="white",width=14,command=short).pack()

#-----------------------------------Entrty-----------------------------------

Entry2 = Entry(win,font="impack 16 bold",bg="pink",width=24,bd=0)
Entry2.pack(pady=30)

mainloop()

#==============================Hope So You Like It============================