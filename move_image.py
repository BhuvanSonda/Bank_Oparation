import tkinter as tk

def move_up(event):
    x, y = label.winfo_x(), label.winfo_y()
    label.place(x=x, y=y-10)

def move_down(event):
    x, y = label.winfo_x(), label.winfo_y()
    label.place(x=x, y=y+10)

def move_left(event):
    x, y = label.winfo_x(), label.winfo_y()
    label.place(x=x-10, y=y)

def move_right(event):
    x, y = label.winfo_x(), label.winfo_y()
    label.place(x=x+10, y=y)

main = tk.Tk()
main.geometry("500x500")

main.bind("<w>", move_up)
main.bind("<s>", move_down)
main.bind("<a>", move_left)
main.bind("<d>", move_right)

main.bind("<Up>", move_up)
main.bind("<Down>", move_down)
main.bind("<Left>", move_left)
main.bind("<Right>", move_right)

photo = tk.PhotoImage(file="star.png")  
label = tk.Label(main, image=photo)     

# label = tk.Label(main, bg='red', width=4, height=2)
# label.place(x=0, y=0)

main.mainloop()
