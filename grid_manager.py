import tkinter as tk

def SUBMIT():
    print(f"first name is : {first_name_entry.get()}")
    
    print(f"last name is : {last_name_entry.get()}")
    
    print(f"email is : {email_entry.get()}")

main=tk.Tk()
main.geometry("500x500")
 
first_name=tk.Label(main,text='first name :').grid(row=1,column=0)
first_name_entry=tk.Entry(main)
first_name_entry.grid(row=1,column=1)

last_name=tk.Label(main,text='last name :').grid(row=2,column=0)
last_name_entry=tk.Entry(main)
last_name_entry.grid(row=2,column=1)

email=tk.Label(main,text='E-mail :').grid(row=3,column=0)
email_entry=tk.Entry(main)
email_entry.grid(row=3,column=1)

submit=tk.Button(main,text='Submit',command=SUBMIT).grid(row=4,column=1,columnspan=1)

main.mainloop()