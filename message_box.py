import tkinter as tk
from tkinter import messagebox
class click:
    def info():
        messagebox.showinfo(title="Information",message="You are in show info",icon=messagebox.QUESTION)
    
    def warning():
        messagebox.showwarning(title="Warning",message="You are in show warning")

    def error():
        messagebox.showerror(title="Error",message="You are in show error")
    
    def OK_CANCEL():
        if messagebox.askokcancel(title="OKCANCEL",message="You are in OK_CANCEL"):
            print("You clicked OK")
        else:
            print("You clicked Cancel")
    
    def retry():
        if messagebox.askretrycancel(title="RETRY",message="You are in RETRY"):
            print("You clicked Retry")
        else:
            print("You clicked Cancel")
    
    def yes_no():
        if messagebox.askyesno(title="YESNO",message="You are in YES_NO"):
            print("You clicked Yes")
        else:
            print("You clicked No")
    
    def Question():
        if messagebox.askquestion(title="QUESTION",message="You are in QUESTION"):
            print("You clicked Yes")
        else:
            print("You clicked No")

    def yes_no_cancel():
        ans=messagebox.askyesnocancel(title="YES_NO_CANCEL",message="You are in YES_NO_CANCEL")
        if ans==True:
            print("You clicked Yes")
        elif ans==False:
            print("You clicked No")
        else:
            print("You clicked Cancel")

main=tk.Tk()
main.geometry("300x300")
main.title("Message Box")

b1=tk.Button(main,text='Show_info',command=click.info)
b1.pack()

Warning=tk.Button(main,text="warning",command=click.warning)
Warning.pack()

error=tk.Button(main,text="Error",command=click.error)
error.pack()

ok_cancel=tk.Button(main,text="Ok_Cancel",command=click.OK_CANCEL)
ok_cancel.pack()

REtry=tk.Button(main,text="RETRY",command=click.retry)
REtry.pack()

YES_NO=tk.Button(main,text="Yes_No",command=click.yes_no)
YES_NO.pack()

QUestion=tk.Button(main,text="Question",command=click.Question)
QUestion.pack()

YES_NO_CANCEL=tk.Button(main,text="Yes_No_Cancel",command=click.yes_no_cancel)
YES_NO_CANCEL.pack()

main.mainloop()