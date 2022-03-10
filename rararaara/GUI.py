
import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
import os
import sqlite3
from PIL import ImageTk, Image
from pygame import Cursor
root = tk.Tk()
root.title('Jayson\'s Exercise App')
root.geometry('700x400')


def submit():
    target.delete(0,END)
#databases

conn = sqlite3.connect

#Create Cursor

#Create Table

target = Entry(root, width = 30)
target.grid(row = 0, column =1, padx = 20)

target_label = Label(root, text = 'Target')
target_label.grid(row=0, column=0)

submit_btn = Button(root, text='Find Workouts', command = submit)

submit_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10,ipadx=100)
#Commit Changes


#Close Connection



root.mainloop()