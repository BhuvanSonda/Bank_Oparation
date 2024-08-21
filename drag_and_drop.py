import tkinter as tk

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
def drag_motion(event):
    widget = event.widget
    X = widget.winfo_x() - widget.startX + event.x
    Y = widget.winfo_y() - widget.startY + event.y
    lable.place(x=X,y=Y)

main=tk.Tk()
main.geometry("500x500")

lable=tk.Label(main,width=3,height=2,bg='red')
lable.place(x=0,y=0)

lable.bind('<Button-1>',drag_start)
lable.bind('<B1-Motion>',drag_motion)
main.mainloop()