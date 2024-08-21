import tkinter as tk

#function for key event
def do(event):
    print(event.keysym)

#function for mouse event
def do_it(event):
    print(f"x={event.x},y={event.y}") 

main=tk.Tk()

main.bind('<Key>',do) #binds with keys

#main.bind('<Motion>',do_it)  #where mouse move
main.bind('<Button-1>',do_it)
main.mainloop()