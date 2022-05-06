from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Treeview
import csv
import sqlite3

#Creating Main Frame
app = Tk()
frame_search = Frame(app)
frame_search.grid(row = 0, column = 0)
app.title('Jayson\'s Exercise App')
app.geometry('900x900')
connection = sqlite3.connect('db')
cursor = connection.cursor()

create_Table = ''' CREATE TABLE IF NOT EXISTS ExerciseLists(
          bodyPart text,
          equipment text,
          gifURL BLOB,
          id text,
          exercise_name text,
          body_target text);
          '''
          
file = open('fitness_exercises.csv')

contents = csv.reader(file)

insert_records = 'INSERT INTO  ExerciseLists (bodyPart, equipment, gifURL,id, exercise_name, bodyTarget) VALUES(?, ?, ?, ?, ?, ?)'

cursor.executemany(insert_records,contents)

#GUI
bt_search = Label(frame_search, text = 'Search By Body Target', font = 14, pady = 20)
bt_search.grid(row = 0, column = 0, pady = 20)
bodyTarget_search = StringVar()
bodyTarget_search_entry = Entry(frame_search,textvariable= bodyTarget_search)
bodyTarget_search_entry.grid(row=0,column = 1)

#Search Button
frame_btns = Frame(app)
frame_btns.grid(row=3, column = 0)
search_btn = Button(frame_search,text = 'Search',width = 12, command = bodyTarget_search)
search_btn.grid(row =0, column = 2)


# Treeview 
frame_router = Frame(app)
frame_router.grid (row = 4, column = 0, rowspan = 7, padx = 50, pady = 50)
columns = ['bodyPart', 'equipment', 'gifURL', 'id','exercise_name','body_target']
router_tree_view = Treeview(frame_router, column=columns, show='headings')
router_tree_view.column('id', width=30)
for col in columns[1:]:
    router_tree_view.column(col, width= 20)
    router_tree_view.heading(col,text = col)
"""router_tree_view.bind('<<TreeviewSelect>>', select_router)"""
router_tree_view.pack(side='left',fill='y')
scrollbar= Scrollbar(frame_router,orient = VERTICAL)
scrollbar.configure(command=router_tree_view.yview)
scrollbar.pack(side='right',fill='y')
router_tree_view.config(yscrollcommand=scrollbar.set)



#Functions
#DataBase
'''
class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS ExerciseLists(
            bodyPart text,
            equipment text,
            gifURL BLOB,
            id text,
            exercise_name text,
            bodyTarget text)""" )
        
        
        self.conn.commit()
    
    
    def fetch(self, bodyTarget = ''):
        self.cursor.execute(
            'SELECT * FROM ExerciseLists WHERE bodyTarget LIKE ?', ('%'+bodyTarget+'%',))
        rows = self.cursor.fetchall()
        return rows
    
    def insert(self,bodyPart,equipment,gifURL,id,exercise_name,body_target):
        file = open('fitness_exercises.csv')

        contents = csv.reader(file)
        self.cursor.executemany('INSERT INTO  ExerciseLists (bodyPart, equipment, gifURL,id, exercise_name, body_target) VALUES(?, ?, ?, ?, ?, ?)',contents)
        self.conn.commit()
'''
#Action Functions
#Populate List with Database Values
def populate_list(bodyTarget=''):
    for i in router_tree_view.get_children():
        router_tree_view.delete(i)
    for row in db.fetch(bodyTarget):
        router_tree_view.insert('','end',values=row)
def search_bodyTarget():
    bodyTarget = bodyTarget_search.get()
    populate_list(bodyTarget)
    
    


    
#Running App

populate_list()

app.mainloop()