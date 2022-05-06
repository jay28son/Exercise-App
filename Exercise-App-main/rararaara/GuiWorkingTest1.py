from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Treeview
import csv
import sqlite3
import tkinter as tk
#connecting to sqlite3
def connect():
    con = sqlite3.connect('g4g.db')
    cursor = con.cursor()
    create_Table = ''' CREATE TABLE IF NOT EXISTS ExerciseLists(
          bodyPart text,
          equipment text,
          gifURL BLOB,
          id text,
          exercise_name text,
          body_target text);
          '''
    delete_firstrow = '''DELETE FROM ExerciseLists where rowid = 1 '''      
    cursor.execute(create_Table)
    cursor.execute(delete_firstrow)
    con.commit()
    con.close()
    
#viewing the tree

def view():
    con = sqlite3.connect('g4g.db')
    cursor = con.cursor()
    for record in tree.get_children():
        tree.delete(record)
    select_all = ''' SELECT DISTINCT * FROM ExerciseLists
          '''
    cursor.execute(select_all)
    rows = cursor.fetchall()
    for row in rows:
        tree.insert('', tk.END,values=row)
    con.close()

#Drop Down Menu Selected Functions
def search_records():
    lookup_records = clicked.get()
    print(lookup_records)
    #Resetting Data
    for record in tree.get_children():
        tree.delete(record)
    con = sqlite3.connect('g4g.db')
    cursor = con.cursor()
    cursor.execute("SELECT DISTINCT * FROM ExerciseLists WHERE body_target LIKE ?", (lookup_records,))
    rows = cursor.fetchall()
    for row in rows:
        tree.insert('', tk.END,values=row)
    con.close()
    
    
#GUI Display Data
connect()
root = tk.Tk()
tree_scroll= Scrollbar(root)
tree_scroll.pack(side=RIGHT, fill = Y)

tree = ttk.Treeview(root,  column= ('c1','c2','c3','c4','c5','c6'), show='headings', yscrollcommand= tree_scroll.set)
tree.heading('#1', text = 'bodyPart')
tree.column('#2',anchor = tk.CENTER)
tree.heading('#2', text = 'equipment')
tree.column('#3',anchor = tk.CENTER)
tree.heading('#3', text = 'gifurl')
tree.column('#4',anchor = tk.CENTER)
tree.heading('#4', text = 'id')
tree.column('#5',anchor = tk.CENTER)
tree.heading('#5', text = 'exerciseName')
tree.column('#6',anchor = tk.CENTER)
tree.heading('#6', text = 'bodyTarget') 
tree.pack()
tree_scroll.config(command=tree.yview)

#DropDown Search Menu
Options = ['abs','adductors','biceps','calves','cardio','delts','forearms','glutes','hamstrings','lats','pectorals','quads','spine','triceps','upper back']
clicked= StringVar()
clicked.set(Options[0])
Search_menu = OptionMenu(root, clicked ,*Options,)
Search_menu.pack(padx = 20, pady = 20)
Search_button = Button(root, text='Search', command = search_records)
Search_button.pack(pady = 10)

#Display Data Button
button = tk.Button(text = 'Display Data', command = view)
button.pack(pady=20)

root.mainloop()