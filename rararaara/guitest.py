from tkinter import *
from tkinter import ttk, ttk
import csv
import sqlite3
from PIL import ImageTk, Image


#GUI Main
root = Tk()
root.title('Jayson\'s Exercise App')
root.geometry('700x400')

#Search For Target
def target_search():
    def search_now():
        target_box.get()
        sql = '''SELECT * FROM ExerciseLists Where body_target = %s
            '''
        body = (target_box)
        result = cursor.execute(sql,body)
        result = cursor.fetchall()
        if not result:
            result = 'Error'
        
    
    target_box = Entry(root)
    target_box.grid(row=1, column = 1, padx = 10, pady = 10)
    target_box_button= Button(root,text =' Search', command = search_now)
    target_box_button.grid(row=2, column=2, padx=10, pady=10)
    drop = ttk.Combobox(target_box, value=["Search by...","Abs","Abductors","Adductors","Biceps","Cardio","Delts","Forearms","Glutes",
                  "Hamstrings","Lats","Neck","Pectorals", "Quads","Traps","Triceps","Upper Back"] )
    drop.current(0)
    drop.grid(row=0,column=2)

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

select_all = '''SELECT * FROM ExerciseLists Where body_target = 'glutes' AND equipment = 'weighted'
            '''
rows = cursor.execute(select_all).fetchall()

#for r in rows:
    #print(r)


connection.commit()



#Creating title
Title_Label = Label(root, text = 'Jayson\'s Exercise App', font = ('Helvetica', 20))
Title_Label.grid(row = 0, column = 0, columnspan = 2,  pady='10')

#Search Buttons
target_search_button = Label(root, text = 'Targetted Body Part')
target_search()
target_search_button.grid(row = 1, column = 0, sticky= W, padx = 10)


root.mainloop()