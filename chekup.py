# Import required libraries
import datetime as dt
import pandas as pd
import re
import tkinter as tk
from tkinter import messagebox as msg
from PIL import Image, ImageTk
from tkinter import ttk
import time

# assign a file
FILE = 'data_varify.csv'


# function to read the file
def Read_csv():
    read = pd.read_csv(FILE) if pd.io.common.file_exists(FILE) else pd.DataFrame(
        columns=["Names", "A/C No:", "Balance :", "Sign:", "Mobile_No:", 'Adhar_No:', "Time:"])
    return read


# class for update the new entries
class Update:

    # function for assign values to the file
    def update(name, account_no, sign, init_balance, mobile_no, adhar_no, time):
        new_entry = {
            "Names": [name],
            "A/C No:": [account_no],
            "Balance :": [init_balance],
            "Sign:": [sign],
            "Mobile_No:": [mobile_no],
            "Adhar_No:": [adhar_no],
            "Time:": [time]}
        df = pd.DataFrame(new_entry)

        # check the condition , if file is existing or not
        if pd.io.common.file_exists(FILE):
            df.to_csv(FILE, mode="a", index=False, header=False)
        else:
            df.to_csv(FILE, mode="w", index=False)


# class for varifing mobile and adhar number
class Validation:
    # for update the mobile number as per the rule
    def Mobile(mobile):
        M = re.compile("^[6-9]{1}[0-9]{9}$")
        if M.match(mobile):
            return mobile

    # for update the adhar number as per the rule
    def Adhar(adhar):
        A = re.compile("^[2-9]{1}[0-9]{11}$")
        # adhar = input("Enter Adhar No:")
        if A.match(adhar):
            return adhar


# OERATIONS OF BANKUSCASE'S
class BankOperations:

    # FUNCTION TO ASSIGN AC_NUMBER FOR THE USER
    def ac_generator():
        # Which reads CSV file
        read = Read_csv()

        result = 100
        # Verifying the AC_Number is empty or filled
        if read["A/C No:"].empty:
            result = 100
        else:
            ac = 0
            for i in read["A/C No:"].values:
                ac = i
            result = ac + 1
        return result

    # function for create acount
    def create(name, sign, init_balance, mobile_no, adhar_no):
        account_no = BankOperations.ac_generator()
        time = dt.datetime.now()
        Update.update(name, account_no, sign, init_balance, mobile_no, adhar_no, time)
        msg.showinfo("Success", f"Account created for :\nName:{name} \n A/C No: {account_no}")

        # function for deposit amount to the existing acount

    def deposit(ac_no, amount):
        read = Read_csv()

        if ac_no in read["A/C No:"].values:
            index = read.index[read["A/C No:"] == ac_no].tolist()[0]  # to find the index of acount number
            read.at[index, "Balance :"] += amount
            read.to_csv(FILE, index=False)
            details = (f"Amount {amount} deposited in A/C No: {ac_no} \n New Balance: {read.at[index, 'Balance :']}")
            return details
        else:
            if msg.askretrycancel("Error",
                                  f"Account No: {ac_no} does not exist"):  # pop up message for error and ask for retry
                ac = 1
            else:
                ac = 0
            return ac

    # function for withdraw amount from existing acount
    def withdraw(ac_no, amount, sign):
        read = Read_csv()

        if ac_no in read["A/C No:"].values:  # to check acount number is exist or not
            index = read.index[read["A/C No:"] == ac_no].tolist()[0]

            if read.at[index, "Sign:"] == sign:  # to check signature is matched or not
                if read.at[index, "Balance :"] >= amount:
                    read.at[index, "Balance :"] -= amount
                    read.to_csv(FILE, index=False)
                    details = (
                        f"Amount {amount} withdrawn from A/C No: {ac_no} \n Available balance : {read.at[index, 'Balance :']}")
                    return details
                else:
                    if msg.askretrycancel("Error",
                                          f"Insufficient balance in A/C No: {ac_no}"):  # if balance is low and enterd amount is high on that time this pop will apeare
                        ac = 1
                    else:
                        ac = 0
                    return ac
            else:
                if msg.askretrycancel("Error",
                                      f"Account No: {ac_no} Signature is not Matched!"):  # if signature is mismatched on that time this pop will apeare
                    ac = 1
                else:
                    ac = 0
                return ac

        else:
            if msg.askretrycancel("Error",
                                  f"Account No: {ac_no} does not Exists!"):  # if entered acount number is not existed then pop w.
                ac = 1
            else:
                ac = 0
            return ac

    # function to check acount details
    def check(account_no):
        # account_no = int(input("Enter account number: "))
        read = Read_csv()
        if account_no in read["A/C No:"].values:  # for check acount number is existing or not
            index = read.index[read["A/C No:"] == account_no].tolist()[0]

            details = (
                f"\n\nName : {read.at[index, 'Names']}\nA/C No : {read.at[index, 'A/C No:']}\nAvailable Balance : {read.at[index, 'Balance :']}")
            return details
        else:
            if msg.askretrycancel("Error",
                                  "Account number does not exist."):  # if Acount number is not existed this popup notification will apeare
                ac = 1
            else:
                print("Thank you for using our services")
                ac = 0
            return ac


def focus_next_entry(event, entries):
    # Find the index of the current entry
    current_index = entries.index(event.widget)
    # Calculate the index of the next entry
    next_index = (current_index + 1) % len(entries)
    # Focus on the next entry
    entries[next_index].focus_set()
    # Prevent the default action of the Enter key
    return 'break'


# function for create acount button
def create_account():
    click_limit = 3
    click_count = [0]

    def validate_inputs():

        # Get values from entry widgets
        amount = amount_entry.get()
        mobile_number = mobile_entry.get()
        adhar_number = adhar_entry.get()
        name_value = name_entry.get()
        sign_value = sign_entry.get()

        # Initialize valid flag
        all_valid = True

        # Validate amount (should be positive numbers)
        if not re.match("^[0-9]+$", amount):
            amount_entry.config(fg='red')
            all_valid = False
        else:
            amount_entry.config(fg='black')
            amount_entry.config(bg='light green')

        # Validate mobile number (should be exactly 10 digits, starting with 6-9)
        # amount_entry.config(fg='black')
        if mobile_number.isdigit():
            mobile_entry.config(fg='black')

            if not re.match("^[6-9]", mobile_number):  #######change condition
                mobile_entry.config(fg='red')
                return

            elif re.match("^[6-9]{1}[0-9]{9}$", mobile_number):

                mobile_entry.config(bg='light green')
            else:
                mobile_entry.config(fg='red')
                all_valid = False
        else:
            mobile_entry.config(fg='red')
            all_valid = False

        # Validate Aadhar number (should be exactly 12 digits)
        if adhar_number.isdigit():
            adhar_entry.config(fg='black')
            if not re.match("^[2-9]", adhar_number):
                adhar_entry.config(fg='red')
                return

            elif re.match("^[2-9][0-9]{11}$", adhar_number):
                adhar_entry.config(fg='black')
                adhar_entry.config(bg='light green')
            else:
                all_valid = False
        else:
            adhar_entry.config(fg='red')
            all_valid = False

        # Check if all fields are filled
        if not (name_value and amount and sign_value and mobile_number and adhar_number):
            submit.config(state='disabled')
            return

        # Enable submit button if all fields are valid
        if all_valid:
            submit.config(state='normal', bg='light green')
            entries.append(submit)
            submit.bind("<Return>", Submit)
            submit.bind("<Button-1>", Submit)
        else:
            submit.config(state='disabled')

    # function for submit button
    def Submit(event):
        if len(click_count) >= click_limit:
            msg.showwarning("Limit Reached", "You have reached the maximum number of submissions.")
            mini.destroy()

        click_count.append(1)

        name = name_entry.get()
        init_balance = amount_entry.get()
        sign = sign_entry.get()
        mobile_no = mobile_entry.get()
        adhar_no = adhar_entry.get()

        # condition to check all blanks are filled or not
        if not name or not amount or not sign or not mobile_no or not adhar_no:
            msg.showerror("Error", "All fields are required")

        # condition to check entered mobile number is valid or not
        elif not Validation.Mobile(mobile_no):
            msg.showerror("Error", "Invalid mobile number.")
            return

        # condition to check entered adhar number is valid or not
        elif not Validation.Adhar(adhar_no):
            msg.showerror("Error", "Invalid Adhar number.")
            return

        # condition to check valid amount
        elif not (re.match("^[0-9]*[0-9]$", init_balance)):
            msg.showerror("Error", "Please enter valid amount")
            return
        else:  # if all conditions are satisfy then it call create acount in Bank Operation
            # minii = tk.Toplevel()
            # minii.geometry('500x200')
            # minii.title('Progress Bar')

            # bar = ttk.Progressbar(minii, orient='horizontal', length=300)
            # bar.pack(pady=10)
            # x=0
            # task = 100
            # while x!=task:
            #     bar['value'] += 1
            #     minii.update_idletasks()
            #     time.sleep(0.05)
            #     x+=1
            # minii.mainloop()
            # minii.destroy()
            mini.destroy()
            BankOperations.create(name, sign, int(init_balance), int(mobile_no), int(adhar_no))

    mini = tk.Toplevel()  # to create child window
    mini.title("Create Account")

    tk.Label(mini, text='Fill the below Information for create A/C :', font=("Arial", 15, 'bold')).grid(row=0, column=0,
                                                                                                        padx=10,
                                                                                                        pady=10,
                                                                                                        columnspan=2)
    # create lables and entry box
    name = tk.Label(mini, text="Enter Name :", font=("Arial", 10))
    name.grid(row=1, column=0, padx=10, pady=10)
    name_entry = tk.Entry(mini, width=30)
    name_entry.grid(row=1, column=1, padx=10, pady=10)
    name_entry.bind("<KeyRelease>", lambda event: validate_inputs())

    amount = tk.Label(mini, text="Enter Initial Amount :", font=("Arial", 10))
    amount.grid(row=2, column=0, padx=10, pady=10)
    amount_entry = tk.Entry(mini, width=30)
    amount_entry.grid(row=2, column=1, padx=10, pady=10)
    amount_entry.bind("<KeyRelease>", lambda event: validate_inputs())

    sign = tk.Label(mini, text='Enter Signature :', font=("Arial", 10))
    sign.grid(row=3, column=0, padx=10, pady=10)
    sign_entry = tk.Entry(mini, width=30)
    sign_entry.grid(row=3, column=1, padx=10, pady=10)
    sign_entry.bind("<KeyRelease>", lambda event: validate_inputs())

    mobile = tk.Label(mini, text='Enter Mobile Number :', font=("Arial", 10))
    mobile.grid(row=4, column=0, padx=10, pady=10)
    mobile_entry = tk.Entry(mini, width=30)
    mobile_entry.grid(row=4, column=1, padx=10, pady=10)
    mobile_entry.bind("<KeyRelease>", lambda event: validate_inputs())

    adhar = tk.Label(mini, text='Enter Adhar_Card Number :', font=("Arial", 10))
    adhar.grid(row=5, column=0, padx=10, pady=10)
    adhar_entry = tk.Entry(mini, width=30)
    adhar_entry.grid(row=5, column=1, padx=10, pady=10)
    # adhar_entry.bind("<KeyRelease>", lambda event: validate_inputs())

    entries = [name_entry, amount_entry, sign_entry, mobile_entry, adhar_entry]

    # Bind the Enter key event to move focus
    for entry in entries:
        entry.bind("<KeyRelease>", lambda event: validate_inputs())
        entry.bind("<Return>", lambda event, entries=entries: focus_next_entry(event, entries))

    submit = tk.Button(mini, text='SUBMIT', font=("Arial", 10), command=Submit, state="disabled")
    submit.grid(row=6, column=0, padx=10, pady=10, columnspan=2)

    # Bind key release events to validation function
    for entry in entries:
        entry.bind("<KeyRelease>", lambda event: validate_inputs())

    mini.grab_set()  # to freeze the buttons in main window untill close toplevel window
    mini.mainloop()


# function for deposit button
def deposit_amount():
    click_limit = 3
    click_count = [0]

    def validate_inputs():
        # Check if both fields are filled
        # if not ( amount_entry.get() and ac_no_entry.get()):
        #     submit.config(state='disabled')
        #     return

        # # Validate initial amount
        # if not re.match("^[0-9]+$", amount_entry.get()):
        #     submit.config(state='disabled')
        #     return

        # # Validate account number
        # if not re.match("^[0-9]+$", ac_no_entry.get()):
        #     submit.config(state='disabled')

        # # All validations passed, enable the submit button
        # submit.config(state='normal')

        read = Read_csv()
        ac_no = ac_no_entry.get()
        amount = amount_entry.get()
        if ac_no.isdigit():
            ac_no_entry.config(fg='black')
            ac_no_entry.config(bg='light green')
            all_valid = True
        else:
            ac_no_entry.config(fg='red')
            all_valid = False

        # Validate amount (should be positive numbers)
        if not re.match("^[0-9]+$", amount):
            amount_entry.config(fg='red')
            all_valid = False
        else:
            amount_entry.config(fg='black')
            amount_entry.config(bg='light green')
            all_valid = True

        if not (amount_entry.get() and ac_no_entry.get()):
            submit.config(state='disabled')
            return

        # Enable submit button if all fields are valid
        if all_valid:
            submit.config(state='normal', bg='light green')
            entries.append(submit)
            submit.bind("<Return>", Submit)
            submit.bind("<Button-1>", Submit)
        else:
            submit.config(state='disabled')

    # function for submit button
    def Submit(event):
        submit.focus_set()
        if len(click_count) >= click_limit:
            mini.destroy()
            msg.showwarning("Limit Reached", "You have reached the maximum number of submissions.")

        click_count.append(1)
        # Get the values from the entry fields
        ac_no = ac_no_entry.get()
        amount = amount_entry.get()
        if not amount or not ac_no:
            msg.showerror("Error", "Please fill all the fields.")  # for pop up msg if any feild is blank
            return
        else:
            details = BankOperations.deposit(int(ac_no), int(amount))
            if details == 0:
                mini.destroy()
            elif details == 1:
                return
            else:
                mini.destroy()
                msg.showinfo(title="Details", message=details)

    mini = tk.Toplevel()
    mini.title("Deposit Amount")

    # def test(row_val,column_val,padx_val,pady_val,var):
    #     var.grid(row=row_val,column=column_val,padx=padx_val,pady=pady_val)

    tk.Label(mini, text='Fill the below Information for Deposit :', font=("Arial", 15, 'bold')).grid(row=0, column=0,
                                                                                                     padx=10, pady=10,
                                                                                                     columnspan=2)
    # to create lables and entry box
    ac_no = tk.Label(mini, text='Enter Acount Number :', font=("Arial", 10))
    ac_no.grid(row=1, column=0, padx=10, pady=10)
    # test(1,0,10,10,ac_no)

    ac_no_entry = tk.Entry(mini, width=30)
    ac_no_entry.grid(row=1, column=1, padx=10, pady=10)
    ac_no_entry.bind("<KeyRelease>", lambda event: validate_inputs())

    amount = tk.Label(mini, text="Enter Initial Amount :", font=("Arial", 10))
    amount.grid(row=2, column=0, padx=10, pady=10)
    amount_entry = tk.Entry(mini, width=30)
    amount_entry.grid(row=2, column=1, padx=10, pady=10)
    amount_entry.bind("<KeyRelease>", lambda event: validate_inputs())

    submit = tk.Button(mini, text='SUBMIT', font=("Arial", 10), command=Submit, state="disabled")
    submit.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

    entries = [ac_no_entry, amount_entry]

    # Bind the Enter key event to move focus
    for entry in entries:
        entry.bind("<Return>", lambda event, entries=entries: focus_next_entry(event, entries))

    # Bind key release events to validation function
    for entry in entries:
        entry.bind("<KeyRelease>", lambda event: validate_inputs())

    mini.grab_set()  # to freeze the buttons in main window untill close toplevel window
    mini.mainloop()


# function for withdraw button
def withdraw_amount():
    click_limit = 3
    click_count = [0]

    def validate_inputs():

        #     # Check if all fields are filled
        #     if not (amount_entry.get() and sign_entry.get() and ac_no_entry.get()):
        #         submit.config(state='disabled')
        #         return

        #     # Validate the amount
        #     if not re.match("^[0-9]+$", amount_entry.get()):
        #         submit.config(state='disabled')
        #         return

        #     # Validate the account number
        #     if not re.match("^[0-9]+$", ac_no_entry.get()):
        #         submit.config(state='disabled')
        #         return

        #     # All validations passed, enable the submit button
        #     submit.config(state='normal')
        # #function for submit button
        read = Read_csv()
        ac_no = ac_no_entry.get()
        amount = amount_entry.get()
        if ac_no.isdigit():
            ac_no_entry.config(fg='black')
            ac_no_entry.config(bg='light green')
            all_valid = True
        else:
            ac_no_entry.config(fg='red')
            all_valid = False

        # Validate amount (should be positive numbers)
        if not re.match("^[0-9]+$", amount):
            amount_entry.config(fg='red')
            all_valid = False
        else:
            amount_entry.config(fg='black')
            amount_entry.config(bg='light green')
            all_valid = True

        if not (amount_entry.get() and ac_no_entry.get()):
            submit.config(state='disabled')
            return

        # Enable submit button if all fields are valid
        if all_valid:
            submit.config(state='normal', bg='light green')
            entries.append(submit)
            submit.tk_focusNext()
            submit.bind("<Return>", Submit)
            submit.bind("<Button-1>", Submit)
        else:
            submit.config(state='disabled')

    def Submit(event):
        if len(click_count) >= click_limit:
            mini.destroy()
            msg.showwarning("Limit Reached", "You have reached the maximum number of submissions.")

        click_count.append(1)
        ac_no = ac_no_entry.get()
        amount = amount_entry.get()
        sign = sign_entry.get()

        if not amount or not ac_no or not sign:
            msg.showerror("Error", "Please fill all the fields.")
            return
        else:
            # Assuming BankOperations.withdraw() is a function that handles the withdrawal process
            details = BankOperations.withdraw(int(ac_no), int(amount), sign)
            if details == 0:
                mini.destroy()
            elif details == 1:
                return
            else:
                mini.destroy()
                msg.showinfo(title="Details", message=details)

    mini = tk.Toplevel()
    mini.title("Withdraw Amount")

    tk.Label(mini, text='Fill the below Information for Withdraw:', font=("Arial", 15, 'bold')).grid(row=0, column=0,
                                                                                                     padx=10, pady=10,
                                                                                                     columnspan=2)
    # to create lables and entry box
    tk.Label(mini, text='Enter Account Number:', font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=10)
    ac_no_entry = tk.Entry(mini, width=30)
    ac_no_entry.grid(row=1, column=1, padx=10, pady=10)
    ac_no_entry.bind("<KeyRelease>", lambda event: validate_inputs())

    tk.Label(mini, text='Enter Signature:', font=("Arial", 10)).grid(row=2, column=0, padx=10, pady=10)
    sign_entry = tk.Entry(mini, width=30)
    sign_entry.grid(row=2, column=1, padx=10, pady=10)
    sign_entry.bind("<KeyRelease>", lambda event: validate_inputs())

    tk.Label(mini, text="Enter Amount:", font=("Arial", 10)).grid(row=3, column=0, padx=10, pady=10)
    amount_entry = tk.Entry(mini, width=30)
    amount_entry.grid(row=3, column=1, padx=10, pady=10)
    amount_entry.bind("<KeyRelease>", lambda event: validate_inputs())

    entries = [ac_no_entry, sign_entry, amount_entry]

    # Bind the Enter key event to move focus
    for entry in entries:
        entry.bind("<Return>", lambda event, entries=entries: focus_next_entry(event, entries))

    submit = tk.Button(mini, text='SUBMIT', font=("Arial", 10), command=Submit, state='disabled')
    submit.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

    # Bind key release events to validation function
    for entry in entries:
        entry.bind("<KeyRelease>", lambda event: validate_inputs())

    mini.grab_set()  # to freeze the buttons in the main window until the toplevel window is closed
    mini.mainloop()


# function for check button in main window
def check_account():
    click_limit = 3
    click_count = [0]

    def validate():  # to validate the entry box inputs
        # if not (re.match("^[0-9]*$",ac_no_entry.get())):#if its then submit button is enable else disable
        #     submit.config(state='disabled')
        # else:
        #     submit.config(state='normal')
        # function for submit button
        read = Read_csv()
        ac_no = ac_no_entry.get()
        if ac_no.isdigit():
            ac_no_entry.config(fg='black')
            ac_no_entry.config(bg='light green')
            submit.config(state='normal', bg='light green')
            submit.bind("<Return>", Submit)
            all_valid = True
        else:
            ac_no_entry.config(fg='red')

    def Submit():
        if len(click_count) >= click_limit:
            mini.destroy()
            msg.showwarning("Limit Reached", "You have reached the maximum number of submissions.")

        click_count.append(1)
        account_no = ac_no_entry.get()
        if not account_no:
            msg.showerror("Error", "Account number is required.")
            return
        else:
            details = BankOperations.check(int(account_no))

            if details == 0:
                mini.destroy()
            elif details == 1:
                return
            else:
                mini.destroy()
                msg.showinfo(title="Details", message=details)
                # mini.destroy()

    mini = tk.Toplevel()

    tk.Label(mini, text='Fill the below Information for Check A/C details :', font=("Arial", 15, 'bold')).grid(row=0,
                                                                                                               column=0,
                                                                                                               padx=10,
                                                                                                               pady=10,
                                                                                                               columnspan=2)
    # to create lables and entry box
    ac_no = tk.Label(mini, text='Enter Acount Number :', font=("Arial", 10))
    ac_no.grid(row=1, column=0, padx=10, pady=10)
    ac_no_entry = tk.Entry(mini, width=30)
    ac_no_entry.grid(row=1, column=1, padx=10, pady=10)
    ac_no_entry.bind("<KeyRelease>", lambda event: validate())

    submit = tk.Button(mini, text='SUBMIT', font=("Arial", 10), command=Submit, state="disabled")
    submit.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
    submit.bind("<Return>", Submit)

    mini.grab_set()  # to freeze the buttons in main window untill close toplevel window
    mini.mainloop()


# for creat Bank Operation  main window
window = tk.Tk()

w = window.winfo_screenwidth()
h = window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))  # to set the

window.title("Banking System")
icon = tk.PhotoImage(file='bakn1.png')
window.iconphoto(False, icon)

# window = tk.Frame(window)#for frame
# window.grid(row=0)

canvas = tk.Canvas(window, width=w, height=h)

img = Image.open('money1.jpg')
img = img.resize((w, h))
photo = ImageTk.PhotoImage(img)

wl = tk.PhotoImage(file="bank_26.png")

canvas.create_image(0, 0, image=photo, anchor='nw')
wallpaper = tk.Label(window, i=wl)
wallpaper.place(x=0, y=0, relwidth=1, relheight=1)

ac_image = tk.PhotoImage(file='create_ac.png')
dbt_image = tk.PhotoImage(file='deposit.png')
# wd_imag=tk.PhotoImage(file='withdraw.png')
chk_image = tk.PhotoImage(file='check1.png')

ac = Image.open('bank_26.png')
ac = img.resize((80, 80))
photo1 = ImageTk.PhotoImage(ac)

button_frame = tk.Frame(window, bg='white')  # Background color for visibility
button_frame.grid(row=1, column=0, sticky='ew', padx=10, pady=10)  # Place frame at the bottom

# Configure grid to expand with the window
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=0)
window.grid_columnconfigure(0, weight=1)

button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(2, weight=1)
button_frame.grid_columnconfigure(3, weight=1)
button_frame.grid_columnconfigure(4, weight=1)

# Add buttons to the frame
tk.Button(button_frame, text="Create Account", command=create_account,
          image=ac_image, compound="left", font=("Arial", 12, 'bold'), height=60,
          activebackground='blue', bg='green', fg='white',
          borderwidth=4, cursor="hand2").grid(row=0, column=0, padx=5, pady=5, sticky='ew')

tk.Button(button_frame, text="Deposit", command=deposit_amount,
          image=dbt_image, compound="left", font=("Arial", 12, 'bold'), height=60,
          activebackground='blue', bg='#fc9342',
          borderwidth=4, cursor="hand2").grid(row=0, column=1, padx=5, pady=5, sticky='ew')

tk.Button(button_frame, text="Withdraw", command=withdraw_amount,
          image=dbt_image, compound="left", font=("Arial", 12, 'bold'), height=60,
          activebackground='blue', bg='#c842fc',
          borderwidth=4, cursor="hand2").grid(row=0, column=2, padx=5, pady=5, sticky='ew')

tk.Button(button_frame, text="Check A/C", command=check_account,
          image=chk_image, compound="left", font=("Arial", 12, 'bold'), height=60,
          activebackground='blue', bg='light blue',
          borderwidth=4, cursor="hand2").grid(row=0, column=3, padx=5, pady=5, sticky='ew')

tk.Button(button_frame, text="Exit", bg='red', font=("Arial", 12, 'bold'), command=quit, cursor="hand2").grid(row=0,
                                                                                                              column=4,
                                                                                                              padx=5,
                                                                                                              pady=5,
                                                                                                              sticky='ew')
tk.Button(window, ).grid(row=5, column=5, padx=5, pady=20)
tk.Button(window, ).grid(row=5, column=6, padx=5, pady=20)
# Make the window resizable
window.resizable(True, True)

# Start the Tkinter event loop
window.mainloop()