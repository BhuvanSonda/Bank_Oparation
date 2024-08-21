import tkinter as tk
from tkinter import ttk

def click():
    #new_window=tk.Toplevel()   depend on parent window
    new_window=tk.Tk()

window_1 =tk.Tk()

tk.Button(window_1,text='click to create another window ',command=click).pack() #create new window


notebook= ttk.Notebook(window_1)

tab_1=tk.Frame(notebook)
tab_2=tk.Frame(notebook)

notebook.add(tab_1,text='Tab_1')
notebook.add(tab_2,text='Tab_2')
notebook.pack(expand=True,fill='both')

tk.Label(tab_1,text='You are in first tab',width=50,height=25).pack()
tk.Label(tab_2,text='you are in second tab',width=50,height=25).pack()

window_1.mainloop()