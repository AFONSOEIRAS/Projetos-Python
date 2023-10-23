from tkinter import ttk
from tkinter import *

parent = Tk()#instanciar o Tk() para uma variavel que vai ser manipulada e criada a interface
frame = ttk.Frame(parent)

s = ttk.Style()
s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')
ttk.Frame(parent, width=200, height=200, style='Danger.TFrame').grid()

parent.mainloop()