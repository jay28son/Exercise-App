from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
import sqlite3


#GUI Main
root = Tk()
root.title('Jayson\'s Exercise App')
root.geometry('900x900')

#converting csv into sql and into a table
connection = sqlite3.connect('g4g.db')
cursor = connection.cursor()

create_Table = ''' CREATE TABLE ExerciseLists(
          bodyPart text,
          equipment text,
          gifURL BLOB,
          id text,
          exercise_name text,
          body_target text);
          '''
          
file = open('fitness_exercises.csv')

contents = csv.reader(file)

insert_records = 'INSERT INTO  ExerciseLists (bodyPart, equipment, gifURL,id, exercise_name, body_target) VALUES(?, ?, ?, ?, ?, ?)'

cursor.executemany(insert_records,contents)
"""
#Search For Target
def target_search():
    def search_now():
        selected = drop.get()
        if selected == 'Search by...':
            test = Label(root, text='Hey! You didn\'t pick a body part!')
            test.grid(row=3, column=0)
        if selected == 'Abs':
            sql = '''SELECT * FROM ExerciseLists Where body_target = 'abs'
                  '''  
            test = Label(root, text='You chose Abs')
            test.grid(row=3, column=0)  
        result = cursor.execute(sql)
        result = cursor.fetchall()
        result_label = Label(root, text = result)
        result_label.grid(row=2, column=0, padx=10, sticky=W)
        
    target_box_button= Button(root,text = ' Search', command = search_now)
    target_box_button.grid(row=2, column=2, padx=10, pady=10)
    drop = ttk.Combobox(root, value=["Search by...","Abs","Abductors","Adductors","Biceps","Cardio","Delts","Forearms","Glutes",
                  "Hamstrings","Lats","Neck","Pectorals", "Quads","Traps","Triceps","Upper Back"] )
    drop.current(0)
    drop.grid(row=1,column=1)
"""


#Example to see if sql for body_target and equipment work
select_all ='''SELECT * FROM ExerciseLists WHERE body_target = 'glutes' and equipment = 'weighted'
            '''
rows = cursor.execute(select_all).fetchall()
class Table:
    def __init__(self,root):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root,width=20, fg='Black', font = ('Times New Roman',8))
                self.e.grid(row=i, column=j)
                self.e.insert(END,rows[i][j])

total_rows = len(rows)
total_columns = len(rows[0])

t = Table(root)
root.mainloop()


connection.commit()


"""
#Creating title
Title_Label = Label(root, text = 'Jayson\'s Exercise App', font = ('Helvetica', 20))
Title_Label.grid(row = 0, column = 0, columnspan = 2,  pady='10')
#Search Buttons
target_search_button = Label(root, text = 'Targetted Body Part')
target_search()
target_search_button.grid(row = 1, column = 0, sticky= W, padx = 10)
root.mainloop()
"""