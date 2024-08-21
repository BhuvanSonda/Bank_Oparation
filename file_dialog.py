import tkinter as tk
from tkinter import filedialog

def Open_file():
    file=filedialog.askopenfilename()
    print(file)
    f=open(file,'r') 
    print(f.read())
    f.close()

def save_file():
    file=filedialog.asksaveasfile(mode='w',defaultextension='.txt',
                                  filetypes=[('Text Files', '.txt'),('HTML files','.html'), ('All Files', '*.*')])
    filetext=text.get(1.0,tk.END)
    file.write(filetext)
    file.close()
    
main=tk.Tk()
main.geometry("400x400")

open=tk.Button(main,text='Open',command=Open_file)
open.pack()

save=tk.Button(main,text='Save',command=save_file)
save.pack() 
text=tk.Text(main)
text.pack()

#Menu Bar

menubar=tk.Menu(main)
main.config(menu=menubar)

file_menu=tk.Menu(menubar,tearoff=0,)
menubar.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label="Open",command=Open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="Exit",command=main.quit)

main.mainloop()