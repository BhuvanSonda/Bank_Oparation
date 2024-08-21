import tkinter as tk
from tkinter import colorchooser

def color():
    color = colorchooser.askcolor(title="Choose a color")   
    main.config(bg=color[1])
    text.config(fg=color[1])

def Submit():
    input=text.get(1.0,tk.END)
    print(input)

main= tk.Tk()
main.geometry("500x500")
button=tk.Button(main,text='choose',command=color)
button.pack()
submit=tk.Button(main,text='Submit',command=Submit)
submit.pack()
text=tk.Text(main,font=('free style',20),)
text.pack()



main.mainloop()