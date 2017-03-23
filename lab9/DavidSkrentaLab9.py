'''
CIS 117 Python Programing: Lab 9
David Skrenta
'''

import tkinter

class MyGUI:
  def __init__(self):
     self.main_window = tkinter.Tk()

     self.main_window.geometry('400x400')

     self.label = tkinter.Label(self.main_window, text='David Skrenta')

     self.label.pack()

     tkinter.mainloop()

my_gui=MyGUI()
