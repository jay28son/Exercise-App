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

#Create_MainFrame
main_frame = Frame(root)
main_frame.pack(fill=BOTH,expand=1)

#Creating a canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side= LEFT, fill = BOTH, expand = 1)


my_scrollbar = ttk.Scrollbar(main_frame, orient = VERTICAL)
my_scrollbar.config(command = my_canvas.yview)
my_canvas.configure(yscrollcommand = my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox('all')))

second_frame = Frame(my_canvas)
my_canvas.create_window((0,0), window = second_frame,anchor = NW)

#Example to see if sql for body_target and equipment work
select_all ='''SELECT * FROM ExerciseLists WHERE body_target = 'glutes' and equipment = 'weighted'
            '''
rows = cursor.execute(select_all).fetchall()
class Table:
    def __init__(self,second_frame):
        for i in range(total_rows):
            for j in range(total_columns):
                self = Entry(root,width=20, fg='blue', font = ('Arial',8))
                self.grid(row=i, column=j)
                self.insert(END,rows[i][j])

total_rows = len(rows)
total_columns = len(rows[0])

t = Table(second_frame)

root.mainloop()


connection.commit()