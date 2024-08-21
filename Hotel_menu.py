import tkinter as tk

def order():
    ordr=[]
    select=list_box.curselection()
    for i in select:
        item=list_box.get(i)
        ordr.append(item)
    print("You Ordered items :")
    for i in ordr:
        print(i)

menu=tk.Tk()
menu.geometry("500x500")
menu.title("Menu List")
menu.configure(background="sky blue")


lable=tk.Label(menu,text='Menu Card',font=("Arial",20,"bold"),fg='blue',bg='white',)
lable.pack()
list=['Dosa','Idly','Palav','Avalakki','Full meals']

list_box=tk.Listbox(menu,fg='black',bg='#C4A484',
                    font=('arial',15,'bold'),width=20,
                    selectmode='multiple')
for index in range(len(list)):
    list_box.insert(index,list[index])
list_box.config(height=list_box.size())
list_box.place(x=50,y=50)

submit=tk.Button(menu,text="Submit",activebackground='white',activeforeground='blue',
                 font=('arial',15,'bold'),width=10,bg='light blue',fg='yellow',
                 cursor='hand2',command=order)
submit.pack(side='bottom')
menu.mainloop()