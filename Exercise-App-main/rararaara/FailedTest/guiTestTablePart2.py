from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import csv
import sqlite3


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


#Example to see if sql for body_target and equipment work
select_all ='''SELECT * FROM ExerciseLists WHERE body_target = 'glutes' and equipment = 'weighted'
            '''
rows = cursor.execute(select_all).fetchall()



#GUI Main
"""
root = Tk()
root.title('Jayson\'s Exercise App')
root.geometry('900x900')
"""
class Table(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        self.canvas = tk.Canvas(self,borderwidth = 0, background = '#ffffff')
        self.frame = tk.Frame(self.canvas, background = '#ffffff' )
        self.vsb = tk.Scrollbar(self,orient = VERTICAL, command = self.canvas.yview)
        self.canvas.configure(yscrollcommand= self.vsb.set)
        
        self.vsb.pack(side='right', fill = 'y')
        self.canvas.pack(side ='left', fill = 'both',expand = TRUE)
        self.canvas.create_window((0,0), window = self.frame, anchor='nw', tags='self.frame')
        self.frame.bind('<Configure>', self.onFrameConfigure)
        
        self.table()
        
        
    
    def table(self):
       
            for i in range(total_rows):
                for j in range(total_columns):
                    tk.Label(self.frame, text ='%s' % rows).grid(row=i, column=0)
                    """
        
        for i in range(total_rows):
            for j in range(total_columns):
                tk.Label(self.frame, text = '%s' % i, width = 20, borderwidth ='1',
                         relief = 'solid').grid(row=i,column=j)
                
                
                self = Entry(root,width=20, fg='blue', font = ('Arial',8))
                self.grid(row=i, column=j)
                self.insert(END,rows[i][j])
            """
                
    def onFrameConfigure(self,event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))



total_rows = len(rows)
total_columns = len(rows[0])   


if __name__ == '__main__':
    root = tk.Tk()
    Tables = Table(root)
    Tables.pack(side = 'top', fill = 'both',expand = TRUE)
    root.mainloop()


