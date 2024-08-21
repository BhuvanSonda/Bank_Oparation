import tkinter as tk
root=tk.Tk()
root.title("Python")
photo=tk.PhotoImage(file='pyy.png')
Lbl=tk.Label(root,text='Well-Come to ',
             font=('Arial',25,'bold'),
             fg='#3ff723',
             relief="solid",
             bg='#f7239f',
             image=photo,
             compound='right',
             padx=20,
             pady=20)
Lbl.pack()

def sub():
    ans=entry.get()
    print(ans)
    entry.config(state='disabled')
    submit.configure(state='disabled')


def clear():
    entry.delete(len(entry.get())-1,tk.END)

def delete():
    entry.delete(0,tk.END)

def check():
    if x.get()==1:
        print("You are a Male")
    else:
        print("You are a Female")

def BUTTON(button_press):
    print(button_press)

def scale_rate():
    print(f"Temparature is {scle.get()} degree Celcius")
    scle.config(state='disabled')
    Scl_btn.config(state='disabled')

def buy():
    print(f"You have bought the product of {fruits[x.get()]}")
  
def order():
    ordr=[]
    select=listbox.curselection()
    for i in select:
        item=listbox.get(i)
        ordr.append(item)
    print("You Ordered items :")
    for i in ordr:
        print(i)

def add():
    listbox.insert(tk.END,entryy.get())
    entryy.delete(0,tk.END)
    listbox.config(height=listbox.size())

def Delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height=listbox.size())


icon=tk.PhotoImage(file='pyy.png')
root.iconphoto(True,icon)
root.config(background='#54ebe3')

name=tk.Label(root,text="Enter your name :",font=('Arial',15,'bold'),)
name.place(x=140,y=150)

entry=tk.Entry(root,fg='black',bg='white',width=10,font=('Arial',15))
entry.place(x=320,y=150)


tiger=tk.PhotoImage(file="Tiger.png")

 
root.geometry('500x500')


button1=tk.Button(root,text='Lion',fg='red',cursor='hand2',activebackground='blue',
                  activeforeground='white',width=10,
                  font='Arialbold',command=lambda res="Lion is Clicked":BUTTON(res) )
button1.pack(padx=5,pady=5)
button2=tk.Button(root,text='Tiger',fg='red',cursor='hand2',activebackground='blue',
                  activeforeground='white',width=10,
                  font='Arialbold',
                  command=lambda res="Tiger is Clicked":BUTTON(res))
                  
button2.pack(padx=5,pady=5)

p1=tk.PhotoImage(file='pp.png')

dele=tk.Button(root,text='Clear All', font=("Arial",15,'bold'),command=delete)
dele.place(x=360,y=200)

submit=tk.Button(root,text="Submit",font=("Arial",15,'bold'),command=sub)
submit.place(x=270,y=200)

dele=tk.Button(root,text="Back",font=("Arial",15,'bold'),command=clear)
dele.place(x=200,y=200)

x=tk.IntVar()
check_btn=tk.Checkbutton(root,text='Male',
                         font=('Arial',15,'bold'),bg='#54ebe3',fg='black',
                         activebackground='black',activeforeground='white',
                         variable=x,
                         onvalue=1,
                         offvalue=0,
                         command=check)
                         
check_btn.place(x=0,y=400)


fruits=['Banana','Apple','Mango']

x=tk.IntVar()
for index in range(len(fruits)):
    R_button=tk.Radiobutton(root,text=fruits[index],
                            font=('Cursive',20,'bold'),
                            value=index,
                            variable=x,
                            fg='red',
                            bg='light green',
                            command=buy)
                            
    pp=R_button.pack(anchor='w',side='right')



c=tk.IntVar()
scle=tk.Scale(root,from_=100.00,to=0.00,font=("Arial",10),
              tickinterval=5,
              bg='light green',fg='red',orient=tk.VERTICAL,
              length=500,variable=c,resolution=1)
scle.place(x=0,y=0)

Scl_btn=tk.Button(root,text="Submit",
                  font=("Arial",15,'bold'),command=scale_rate)
Scl_btn.place(x=0,y=550)

ent=tk.Entry(root,font=("Arisl"),width=15,textvariable=c)
ent.place(x=0,y=510)


c1=tk.StringVar()
listbox=tk.Listbox(root,fg='white',
                bg = 'gray',font=('Arial',20),
               selectmode=tk.MULTIPLE)
food=['Kabab','Dose','Pongal','Curd Rice','Dose','Pongal','Curd Rice']
for item in range(len(food)):
    listbox.insert(item,food[item])
listbox.config(height=listbox.size())
listbox.place(x=200,y=250)

entryy=tk.Entry(root,font=('cobalt',20),)
entryy.place(x=510,y=350)

S_buton=tk.Button(root,text='Submit',height=4,command=order)
S_buton.place(x=510,y=400)

add_button=tk.Button(root,text='Add',height=4,command=add)
add_button.place(x=580,y=400)

L_del=tk.Button(root,text='Delete',height=4,command=Delete)
L_del.place(x=650,y=400)



root.tk.mainloop()