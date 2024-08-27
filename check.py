#Import required libraries
import tkinter as tk
import datetime as dt
import pandas as pd
import re
from tkinter import messagebox as msg
from tkinter import ttk
import csv
from tkinter import filedialog

#assign a file
Acounts_file='data.csv'

AC_close_file='Closed_Acounts.csv'
ac_closed = pd.read_csv(Acounts_file) if pd.io.common.file_exists(AC_close_file) else pd.DataFrame(columns=["Names", "A/C No:", "Sign:","Mobile_No:",'Adhar_No:',"Time:","Reason"])
   
#function to read the file
def Read_csv():
    read = pd.read_csv(Acounts_file) if pd.io.common.file_exists(Acounts_file) else pd.DataFrame(columns=["Names", "A/C No:", "Balance :", "Sign:","Mobile_No:",'Adhar_No:',"Time:"])
    return read

#class for update the new entries 
class Update:
   
   #function for assign values to the file
    def AC_entry(name, account_no, sign, init_balance,mobile_no,adhar_no,time,Ac_type):
        new_entry = {
            "Names": [name],
            "A/C No:": [account_no],
            "Balance :": [init_balance],
            "Sign:": [sign],
            "Mobile_No:": [mobile_no],
            "Adhar_No:": [adhar_no],
            "Time:": [time],
            'AC_TYPE':[Ac_type]}
        df = pd.DataFrame(new_entry)
        #check the condition , if file is existing or not
        if pd.io.common.file_exists(Acounts_file):
            df.to_csv(Acounts_file, mode="a", index=False, header=False)
        else:
            df.to_csv(Acounts_file, mode="w", index=False)

# assign the details of deleted acount to the closed ac file data
def colsed(name, account_no, sign,mobile_no,adhar_no,time,reason):
    entry = {
        "Names": [name],
        "A/C No:": [account_no],
        "Sign:": [sign],
        "Mobile_No:": [mobile_no],
        "Adhar_No:": [adhar_no],
        "Time:": [time],
        "Reason": [reason]}
    df = pd.DataFrame(entry)

        #check the condition , if file is existing or not
    if pd.io.common.file_exists("AC_close_file.csv"):
        df.to_csv("AC_close_file.csv", mode="a", index=False, header=False)
    else:
        df.to_csv("AC_close_file.csv", mode="w", index=False)
    
#class for varifing mobile and adhar number
class Validation:
    #for update the mobile number as per the rule
    def Mobile(mobile):
        M=re.compile("^[6-9]{1}[0-9]{9}$")
        if M.match(mobile):
            return mobile
        
    #for update the adhar number as per the rule
    def Adhar(adhar):
        A = re.compile("^[2-9]{1}[0-9]{11}$")
        if A.match(adhar):
            return adhar
        
        #validates the amount
    def Amount(amount):
        A = re.compile(r"^[1-9]\d{0,9}(\.(?!0\d)\d{1,10})?$") # first digit  before decimal point value should be greater than zero 
        if A.match(amount):
            return amount
 #validates the name      
    def Name(name):
        N = re.compile("^[A-Za-z][A-Za-z ]{1,19}$")
        if N.match(name):
            return name
    #validates the signature
    def Sign(sign):
        S = re.compile("^[A-Za-z]{1,19}$")
        if S.match(sign):
            return sign
     

#OERATIONS OF BANK CASE'S
class BankOperations:

    #FUNCTION TO ASSIGN AC_NUMBER FOR THE USER
    def ac_generator():
        #Which reads CSV file
        read=Read_csv()

        result = 100
        #Verifying the AC_Number is empty or filled
        if read["A/C No:"].empty:
            result = 100
        else:
            ac=0
            for i in read["A/C No:"].values:
                ac=i
            result = ac+1
        return result
            
#function for create acount
    def create(name,  sign, init_balance,mobile_no,adhar_no,aC_tYpe):
        account_no=BankOperations.ac_generator()
        time = dt.datetime.now()
        Update.AC_entry(name, account_no, sign, init_balance,mobile_no,adhar_no, time,aC_tYpe)
        msg.showinfo("Success", f"Account created for :\n\nName:{name} \n A/C No: {account_no}\nMobile No :{mobile_no},\nAdhar No:{adhar_no}")  
    
 #function for deposit amount to the existing acount          
    def deposit(ac_no,amount):
        read=Read_csv()
        
        if ac_no in read["A/C No:"].values:
            index = read.index[read["A/C No:"] == ac_no].tolist()[0]#to find the index of acount number
            read.at[index, "Balance :"] += amount
            read.to_csv(Acounts_file, index=False)
            details=(f"Amount {amount} deposited in A/C No: {ac_no} \n New Balance: {read.at[index, 'Balance :']}")
            return details
        else:
            return "Account_not_found"
            # if msg.askretrycancel("Error", f"Account No: {ac_no} does not exist"):# pop up message for error and ask for retry
            #     ac=1
            # else:
            #     ac=0
            # return ac
  

#function for withdraw amount from the existing acount     
    def withdraw(ac_no,amount,sign,Ac_type):
        read=Read_csv()
        
        if ac_no in read["A/C No:"].values:#to check acount number is exist or not
            index = read.index[read["A/C No:"] == ac_no].tolist()[0]

            if read.at[index,"AC_TYPE"]==Ac_type:
                if read.at[index, "Sign:"] == sign:#to check signature is matched or not
                    if read.at[index, "Balance :"] >= amount:
                        read.at[index, "Balance :"] -= amount
                        read.to_csv(Acounts_file, index=False)
                        details=(f"Amount {amount} withdrawn from A/C No: {ac_no} \n Available balance : {read.at[index, 'Balance :']}")
                        return details
                    else:
                        info="Insufficient_fund"    
                        return info
                else:                  
                    info="Invalid_sign"    
                    return info
            else:               
                info="Ac_Type_Not_Match"
                return info
        else:
            info='Acount_not_exist'    
            return info
   
    #function to check acount details 
    def check(account_no):
        #account_no = int(input("Enter account number: "))
        read=Read_csv()
        if account_no in read["A/C No:"].values:#for check acount number is existing or not 
            index = read.index[read["A/C No:"] == account_no].tolist()[0]
            
            details=(f"\tAcount Details:\n\nName : {read.at[index, 'Names']}\n\nA/C No : {read.at[index, 'A/C No:']}\n\nAvailable Balance : {read.at[index, 'Balance :']}\n\nMobile Number : {read.at[index, 'Mobile_No:']}\n\nAdhar Card Number : {read.at[index,'Adhar_No:']}\n\nAc Type : {read.at[index,'AC_TYPE']} ")
            return details
        else:
            info="Ac_Number_not_exist"
            return info
              
        
    def remove(ac_no,name,sign,adhar_no,mobile_no,ac_type):
        read = Read_csv()

        if ac_no in read["A/C No:"].values:
            index = read.index[read["A/C No:"] == ac_no].tolist()[0]  # Find the index of the account number
            #Condition to check given details are valid or not
            if read.at[index, "Names"] == name:
                if read.at[index, "Sign:"] == sign:
                    if read.at[index, "Mobile_No:"] == mobile_no:
                        if read.at[index, "Adhar_No:"] == adhar_no:
                            if  read.at[index, "AC_TYPE"] == ac_type:
                                return "removed"
                            else:
                                info="Ac_type_not_match"
                                return info
                        else:
                            info="Adhar_number_not_match"
                            return info
                    else:
                        info="Mobile_number_not_match"
                        return info
                        
                else:
                    info="Signature_not_match"
                    return info
                    
            else:
                info= "Name_not_match"
                return info
                
        else:
            info="Ac_not_exist"  # If account number is not found
            return info
           

# Fuction to Destroy/close the Toplevel window
def close_toplevel(Toplevel):
    Toplevel.destroy()  

#valid checkup for create ac
def create_valid(entries,toplevel=None,mobile_var=None,adhar_var=None,amount_var=None,name_var=None,sign_var=None,AC_TYPE=None,Message=None):
    global a
    a=1
    init_balance = amount_var.get()
    mobile_no = mobile_var.get()
    adhar_no = adhar_var.get()
    name= name_var.get()
    sign = sign_var.get()
    invalids=Message #invalids=[name_invalid_msg, amount_invalid_msg, sign_invalid_msg, mobile_invalid_msg, adhar_invalid_msg]
    if init_balance=="" or mobile_no=="" or adhar_no=="" or name=='' or sign=='' or AC_TYPE=='':
            invalids[6].config(text=" Please fill the all fields",fg="red")#if ente
            return False
    else:
        invalids[6].config(text='')

    if not Validation.Name(name):
        a = 0
        invalids[0].config(text=" Invalid name",fg="red")#if enter name  is not match the formate of name the it arise error msg
        entries[0].focus_set()
        return False
    else:
        invalids[0].config(text=" ",fg="green")#if enter name  is match the formate of name the it remove the  error msg

    # Validate Amount
    if not Validation.Amount(init_balance):
        a = 0
        invalids[1].config(text="entered  amount must be digits",fg="red")#if enter amount  is not match the formate of amount the it arise error msg
        entries[1].focus_set()
        return False
    else:
        invalids[1].config(text=" ",fg='green')#if enter amount  is match the formate of name the it remove the  error msg

    if not Validation.Sign(sign):
        a=0
        invalids[2].config(text="entered  amount must be digits",fg="red")#if enter sign  is  not match the formate of sign the it remove the  error msg
        entries[2].focus_set()
        return False
    else:
        invalids[2].config(text=" ",fg='green')#if enter sign is match the formate of name the it remove the  error msg
    
        # Validate Mobile Number
    if not Validation.Mobile(mobile_no):
        a = 0
        invalids[3].config(text="entered  mobile number is not valid",fg="red")
        entries[3].focus_set()
        return False
    else:
        invalids[3].config(text=" ",fg='green')
    
        # Validate Aadhar Number
    if not Validation.Adhar(adhar_no):
        a = 0
        invalids[4].config(text="entered  Adhar number is not valid",fg="red")
        entries[4].focus_set()
        return False
    else:  
        invalids[4].config(text=" ",fg='green')
    List=['Saving_A/C','Current_A/C','FD_A/C']#list of acount types
    if AC_TYPE in List:
       invalids[5].config(text="   ",fg="red")
    else:
        invalids[5].config(text="A/C type is required !!",fg="red")
        entries[4].focus_set()
        return
    if a == 1: #once all validation is true then it is enter this contdition
         # Call the create function from BankOperations to create a new account
            BankOperations.create(name, sign, int(init_balance), mobile_no, adhar_no, AC_TYPE)
            close_toplevel(toplevel)  # Close the current Toplevel window')

def create_account():
    # Create a new Toplevel window as a child window to the main window (`window`)
    mini = tk.Toplevel(window)
    mini.title("Create Account")
    Toplevel = mini

    # Label for the form heading
    tk.Label(mini, text='Fill the below Information for create A/C :', font=("Arial", 15, 'bold')).grid(row=0, column=0, padx=10, pady=10, columnspan=2)

    # Label and entry for Name
    name = tk.Label(mini, text="Enter Name:", font=("Arial", 10))
    name.grid(row=1, column=0, padx=10, pady=10)
    name_var = tk.StringVar()
    name_entry = tk.Entry(mini, textvariable=name_var, width=30)
    name_entry.grid(row=1, column=1, padx=10, pady=10)

    # Label to display invalid input messages for Name
    name_invalid_msg = tk.Label(mini, text="", fg="red")
    name_invalid_msg.grid(row=2, column=1, padx=10, pady=0)

    # Label and entry for Initial Amount
    amount = tk.Label(mini, text="Enter Initial Amount:", font=("Arial", 10))
    amount.grid(row=3, column=0, padx=10, pady=10)
    amount_var = tk.StringVar()
    amount_entry = tk.Entry(mini, width=30, textvariable=amount_var)
    amount_entry.grid(row=3, column=1, padx=10, pady=10)

    # Label to display invalid input messages for Initial Amount
    amount_invalid_msg = tk.Label(mini, text="", fg="red")
    amount_invalid_msg.grid(row=4, column=1, padx=10, pady=0)

    # Label and entry for Signature
    sign = tk.Label(mini, text="Enter Signature:", font=("Arial", 10))
    sign.grid(row=5, column=0, padx=10, pady=10)
    sign_var = tk.StringVar()
    sign_entry = tk.Entry(mini, textvariable=sign_var, width=30)
    sign_entry.grid(row=5, column=1, padx=10, pady=10)

    # Label to display invalid input messages for Signature
    sign_invalid_msg = tk.Label(mini, text="", fg="red")
    sign_invalid_msg.grid(row=6, column=1, padx=10, pady=0)

    # Label and entry for Mobile Number
    mobile = tk.Label(mini, text="Enter Mobile Number:", font=("Arial", 10))
    mobile.grid(row=7, column=0, padx=10, pady=10)
    mobile_var = tk.StringVar()
    mobile_entry = tk.Entry(mini, width=30, textvariable=mobile_var)
    mobile_entry.grid(row=7, column=1, padx=10, pady=10)

    # Label to display invalid input messages for Mobile Number
    mobile_invalid_msg = tk.Label(mini, text="", fg="red")
    mobile_invalid_msg.grid(row=8, column=1, padx=10, pady=0)

    # Label and entry for Adhar Card Number
    adhar = tk.Label(mini, text="Enter Adhar Card Number:", font=("Arial", 10))
    adhar.grid(row=9, column=0, padx=10, pady=10)
    adhar_var = tk.StringVar()
    adhar_entry = tk.Entry(mini, width=30, textvariable=adhar_var)
    adhar_entry.grid(row=9, column=1, padx=10, pady=10)

    # Label to display invalid input messages for Adhar Card Number
    adhar_invalid_msg = tk.Label(mini, text="", fg="red")
    adhar_invalid_msg.grid(row=10, column=1, padx=10, pady=0)

    # Radio buttons for selecting the type of account
    type_of_ac = ['Saving_A/C', 'Current_A/C', 'FD_A/C']
    selected_ac = tk.StringVar(value=-1)  # Default value for radiobuttons

    for i in range(len(type_of_ac)):
        tk.Radiobutton(mini, text=type_of_ac[i], variable=selected_ac, value=type_of_ac[i], font=("Arial", 12)).grid(row=11, column=i)

    # Label to display invalid input messages for account type selection
    radio_invalid_msg = tk.Label(mini, text="", fg="red")
    radio_invalid_msg.grid(row=12, column=1, padx=10, pady=0)

    # Label to display general submission errors or messages
    submit_invalid_msg = tk.Label(mini, text='', font=('', 13, 'bold'))
    submit_invalid_msg.grid(row=14, column=0, padx=10, pady=10, columnspan=3)

    # List of entry widgets and associated invalid message labels for easier management
    entries = [name_entry, amount_entry, sign_entry, mobile_entry, adhar_entry]
    invalid_msg = [name_invalid_msg, amount_invalid_msg, sign_invalid_msg, mobile_invalid_msg, adhar_invalid_msg, radio_invalid_msg, submit_invalid_msg]

    # Bind Enter key to move focus to the next entry field
    for entry in entries:
        entry.bind("<Return>", lambda event, entries=entries: focus_next_entry(
            event, entries, Toplevel, mobile_var, adhar_var, amount_var, name_var, sign_var,
            check='create_ac', ac_type=selected_ac, Msg=invalid_msg))
        # Bind Down arrow key to navigate to the next entry
        entry.bind("<Down>", lambda event, entries=entries: Arrow_keys(event, entries))
        # Bind Up arrow key to navigate to the previous entry
        entry.bind("<Up>", lambda event, entries=entries: Arrow_keys(event, entries))

    # Button to submit the form, with validation logic passed in the command
    submit_btn = tk.Button(mini, text='SUBMIT', font=("Arial", 10, 'bold'),
                           command=lambda: create_valid(entries, Toplevel, mobile_var, adhar_var, amount_var, name_var, sign_var, selected_ac.get(), invalid_msg))
    submit_btn.grid(row=13, column=0, padx=10, pady=10, columnspan=2)

    # Disable interaction with the main window until this toplevel window is closed
    mini.grab_set()
    # Allow the toplevel window to be resizable
    mini.resizable(True, True)
    # Start the Tkinter event loop
    mini.mainloop()



#valid checkup for Deposit amount
def deposit_valid(entries, toplevel=None, amount_var=None, ac_no_var=None, Sub_btn=None, Message=None):
    global a
    a = 1  # Initialize a flag to track if validation passes (1) or fails (0)

    # Retrieve the input values from the entry fields
    amt = amount_var.get()
    ac_no = ac_no_var.get()
    invalid_msg = Message  # List of labels to display validation messages

    # Check if any of the fields are empty
    if amt == "" or ac_no == "":
        a = 0  # Set flag to 0, indicating validation failure
        invalid_msg[2].config(text="Please fill all the fields", fg="red")  # Show message to fill all fields
        return False
    else:
        invalid_msg[2].config(text='')  # Clear the validation message if fields are filled

    # Validate the amount using a custom validation function (e.g., `Validation.Amount()`)
    if not Validation.Amount(amt):
        a = 0  # Set flag to 0, indicating validation failure
        invalid_msg[0].config(text="Invalid Amount Entry", fg="red")  # Show message for invalid amount
        entries[0].focus_set()  # Set focus back to the amount entry field
        return False
    else:
        invalid_msg[0].config(text="")  # Clear the validation message if the amount is valid

    # Check if the account number is a valid digit
    if not ac_no.isdigit():
        a = 0  # Set flag to 0, indicating validation failure
        invalid_msg[1].config(text="Invalid Account Number", fg="red")  # Show message for invalid account number
        entries[1].focus_set()  # Set focus back to the account number entry field
        return False
    else:
        invalid_msg[1].config(text="")  # Clear the validation message if the account number is valid

    # If all validations pass (`a` is still 1)
    if a == 1:
        # Call the deposit function from `BankOperations` class and store the returned details
        details = BankOperations.deposit(int(ac_no), int(amt))
        
        # Check if the deposit operation returned "Account_not_found"
        if details == "Account_not_found":
            invalid_msg[2].config(text="Account number is not found!!", fg="red")  # Show message if account not found
            entries[1].focus_set()  # Set focus back to the account number entry field
        else:
            close_toplevel(toplevel)  # Close the toplevel window after successful deposit
            msg.showinfo(title="Details", message=details)  # Show account details in a message box after deposit

def deposit_amount():
    # Create a new Toplevel window for the deposit form
    mini = tk.Toplevel()
    mini.title("Deposit Amount")
    Toplevel = mini

    # Create a label for the form heading
    tk.Label(mini, text='Fill the below Information for Deposit :', font=("Arial", 15, 'bold')).grid(row=0, column=0, padx=10, pady=10, columnspan=2)

    # Create a label and entry for the initial amount
    amount = tk.Label(mini, text="Enter Initial Amount :", font=("Arial", 10))
    amount.grid(row=1, column=0, padx=10, pady=10)
    amount_var = tk.StringVar()
    amount_entry = tk.Entry(mini, width=30, textvariable=amount_var)
    amount_entry.grid(row=1, column=1, padx=10, pady=10)

    # Label to display invalid input messages for the amount
    amount_invalid_msg = tk.Label(mini, text="", fg="red")
    amount_invalid_msg.grid(row=2, column=1, padx=10, pady=0)

    # Create a label and entry for the account number
    ac_no = tk.Label(mini, text='Enter Account Number :', font=("Arial", 10))
    ac_no.grid(row=3, column=0, padx=10, pady=10)
    ac_no_var = tk.StringVar()
    ac_no_entry = tk.Entry(mini, width=30, textvariable=ac_no_var)
    ac_no_entry.grid(row=3, column=1, padx=10, pady=10)

    # Label to display invalid input messages for the account number
    ac_no_invalid_msg = tk.Label(mini, text="", fg="red")
    ac_no_invalid_msg.grid(row=4, column=1, padx=10, pady=0)

    # Label to display general submission errors or messages
    submit_invalid_msg = tk.Label(mini, text='', font=('', 13, 'bold'))
    submit_invalid_msg.grid(row=6, column=0, padx=10, pady=10, columnspan=3)

    # List of all entry widgets and associated invalid message labels for easier management
    entries = [amount_entry, ac_no_entry]
    invalid_msg = [amount_invalid_msg, ac_no_invalid_msg, submit_invalid_msg]

    # Button to submit the form, with validation logic passed in the command
    submit_btn = tk.Button(mini, text='SUBMIT', font=("Arial", 10), command=lambda: deposit_valid(entries, Toplevel, amount_entry, ac_no_var, Message=invalid_msg))
    submit_btn.grid(row=5, column=0, padx=10, pady=10, columnspan=2)

    # Bind Enter key to move focus to the next entry field
    for entry in entries:
        entry.bind("<Return>", lambda event, entries=entries: focus_next_entry(event, entries, Toplevel, amount_var=amount_var,
                                                                               ac_no_var=ac_no_var, check='deposit', Msg=invalid_msg))
        # Bind Down arrow key to navigate to the next entry
        entry.bind("<Down>", lambda event, entries=entries: Arrow_keys(event, entries))
        # Bind Up arrow key to navigate to the previous entry
        entry.bind("<Up>", lambda event, entries=entries: Arrow_keys(event, entries))

    # Disable interaction with the main window until this toplevel window is closed
    mini.grab_set()
    # Allow the toplevel window to be resizable
    mini.resizable(True, True)
    # Start the Tkinter event loop
    mini.mainloop()

def remove_valid(entries, toplevel=None, mobile_no=None, adhar_no=None, ac_no_var=None, name_var=None,
                 sign_var=None, Reason=None, AC_TYPE=None, Message=None):
    global a  # Use global variable 'a' to track validation status
    a = 1  # Initialize 'a' to 1, indicating that validation has passed so far

    # Get input values from Tkinter variables
    ac_no = ac_no_var.get()     # Account number
    mobile_no = mobile_no.get()   # Mobile number
    adhar_no = adhar_no.get()    # Aadhar number
    name = name_var.get()     # Account holder's name
    sign = sign_var.get()   # Signature
    reason = Reason.get()   # Reason for removal
    Ac = AC_TYPE  # Account type [Saving, Current, FD]
    invalid_msg = Message  # List of message labels for displaying validation errors
    read = Read_csv()  # Function call to read CSV file

    # Check if any of the required fields are empty
    if ac_no == "" or mobile_no == "" or adhar_no == "" or name == "" or sign == '' or reason == '':
        invalid_msg[7].config(text="Please fill all the fields", fg="red")
        return False  # Exit function early if any field is empty
    invalid_msg[7].config(text="")  # Clear any error message for empty fields

    # Validate the entered name
    if not Validation.Name(name):
        a = 0  # Set validation flag to 0 indicating failure
        invalid_msg[0].config(text="Invalid name entry", fg='red')  # Show error message for invalid name
        entries[0].focus_set()  # Set focus back to the name entry field for correction
        return False    
    else:
        invalid_msg[0].config(text="")  # Clear error message if the name is valid

    # Validate the account number
    if not ac_no.isdigit():
        invalid_msg[1].config(text="Invalid input: Please enter a number.")
        entries[1].focus_set()  # Set focus back to the account number entry field for correction
        return False
    else:
        invalid_msg[1].config(text="")  # Clear the message if input is valid

    # Validate the signature
    if not Validation.Sign(sign):
        a = 0   
        invalid_msg[2].config(text="Invalid signature", fg='red')  # Show error message for invalid signature
        entries[2].focus_set()  # Set focus back to the signature entry field for correction
        return False    
    else:
        invalid_msg[2].config(text="")  # Clear error message if the signature is valid

    # Validate Mobile Number
    if not Validation.Mobile(mobile_no):
        a = 0  # Set validation flag to 0 indicating failure
        invalid_msg[3].config(text="Invalid mobile number", fg='red')  # Show error message for invalid mobile number
        entries[3].focus_set()  # Set focus back to the mobile number entry field for correction
        return False    
    else:
        invalid_msg[3].config(text="")  # Clear error message if the mobile number is valid

    # Validate Aadhar Number
    if not Validation.Adhar(adhar_no):
        a = 0   
        invalid_msg[4].config(text="Invalid adhar number", fg='red')  # Show error message for invalid Aadhar number
        entries[4].focus_set()  # Set focus back to the Aadhar number entry field for correction
        return False    
    else:
        invalid_msg[4].config(text="")  # Clear error message if the Aadhar number is valid
    
    # Check if reason file is uploaded
    if not reason:
        invalid_msg[5].config(text="Please upload your file ", fg="red")
        return False
    else:
        invalid_msg[5].config(text="")  # Clear error message if file is uploaded

    # Check that the account type is one of the valid types
    List = ['Saving_A/C', 'Current_A/C', 'FD_A/C']  # List of valid account types
    if Ac in List:
        invalid_msg[6].config(text="   ", fg="red")  # Clear any previous error message for account type
    else:
        invalid_msg[6].config(text="A/C type is required !!", fg="red")  # Show error message for invalid or missing account type
        entries[4].focus_set()  # Set focus back to the Aadhar entry field if account type is invalid
        return  # Exit the function since account type is invalid

    # If all validations pass, proceed with enabling the next entry field and submitting the form
    if a == 1:
        # Call the remove function from `BankOperations` class and store the returned details
        details = BankOperations.remove(int(ac_no), str(name), str(sign), int(adhar_no), int(mobile_no), Ac)

        if details == "removed":
            # If account removal is successful, update the CSV file
            ac = int(ac_no)
            index = read.index[read["A/C No:"] == ac].tolist()[0]  # Find the index of the account to remove
            print("index is =", index)
            read.drop(index, inplace=True)  # Remove the row from the DataFrame
            read.to_csv(Acounts_file, index=False)  # Save the changes to the CSV file
            t = dt.datetime.now()  # Get the current datetime
            time = (t.strftime("%d-%m-%Y   %H:%M:%S "))  # Format the datetime for logging
            close_toplevel(toplevel)    
            colsed(name, ac, sign, mobile_no=mobile_no, adhar_no=adhar_no, time=time, reason=reason)  # Update the closed account details
            msg.showinfo("Information", "Account removed successfully")  # Show success message     
        else:
            # Handle different error cases based on the result from `BankOperations.remove()`
            if details == "Ac_not_exist":
                invalid_msg[1].config(text="Account number does not exist!!", fg='red')
                entries[1].focus_set()
                  
            elif details == "Name_not_match":
                invalid_msg[0].config(text="Name Doesn't match!!", fg='red')  # Show error if name doesn't match
                entries[0].focus_set()

            elif details == "Signature_not_match":
                invalid_msg[2].config(text="Signature does not match!!", fg='red')  # Show error if signature doesn't match
                entries[2].focus_set()

            elif details == "Mobile_number_not_match":
                invalid_msg[3].config(text="Mobile number does not match!!", fg='red')  # Show error if mobile number doesn't match
                entries[3].focus_set()
            
            elif details == "Adhar_number_not_match":
                invalid_msg[4].config(text="Aadhar number does not match!!", fg='red')  # Show error if Aadhar number doesn't match
                entries[4].focus_set()

            elif details == "Ac_type_not_match":
                invalid_msg[5].config(text="Account type does not match!!", fg='red')  # Show error if account type doesn't match
                entries[4].focus_set()

def remove_ac():

    # Create a Toplevel window (popup window) for the "Remove Account" functionality
    mini=tk.Toplevel()
    mini.title("Remove Account")
    Toplevel=mini

    # Create a label and entry for entering the user's name
    name=tk.Label(mini,text="Enter Name :",font=("Arial",10))
    name.grid(row=1,column=0,padx=10,pady=10)
    name_var=tk.StringVar()  # Variable to store the entered name
    name_entry=tk.Entry(mini,textvariable=name_var,width=30)
    name_entry.grid(row=1,column=1,padx=10,pady=10)
    name_invalid_msg=tk.Label(mini)  # Label to display any validation errors for the name
    name_invalid_msg.grid(row=2,column=1)

    # Create a label and entry for entering the account number
    ac_no=tk.Label(mini, text="Enter Account Number",font=("Arial",10))
    ac_no.grid(row=3,column=0,padx=10,pady=10)
    ac_no_var=tk.StringVar()  # Variable to store the entered account number
    ac_no_Entry=tk.Entry(mini,width=30,textvariable=ac_no_var)
    ac_no_Entry.grid(row=3,column=1,padx=10,pady=10)
    ac_no_invalid_msg=tk.Label(mini,fg='red')  # Label to display any validation errors for the account number
    ac_no_invalid_msg.grid(row=4,column=1)
    
    # Create a label and entry for entering the user's signature
    sign=tk.Label(mini,text='Enter Signature :',font=("Arial",10))
    sign.grid(row=5,column=0,padx=10,pady=10)
    sign_var=tk.StringVar()  # Variable to store the entered signature
    sign_entry=tk.Entry(mini,textvariable=sign_var,width=30)
    sign_entry.grid(row=5,column=1,padx=10,pady=10)
    sign_invalid_msg=tk.Label(mini,fg='red')  # Label to display any validation errors for the signature
    sign_invalid_msg.grid(row=6,column=1)

    # Create a label and entry for entering the mobile number
    mobile=tk.Label(mini,text='Enter Mobile Number :',font=("Arial",10))
    mobile.grid(row=7,column=0,padx=10,pady=10)
    mobile_var = tk.StringVar()  # Variable to store the entered mobile number
    mobile_entry=tk.Entry(mini,width=30,textvariable=mobile_var)
    mobile_entry.grid(row=7,column=1,padx=10,pady=10)
    mobile_invalid_msg=tk.Label(mini)  # Label to display any validation errors for the mobile number
    mobile_invalid_msg.grid(row=8,column=1)

    # Create a label and entry for entering the Adhar Card number
    adhar=tk.Label(mini,text='Enter Adhar_Card Number :',font=("Arial",10))
    adhar.grid(row=9,column=0,padx=10,pady=10)
    adhar_var=tk.StringVar()  # Variable to store the entered Adhar Card number
    adhar_entry=tk.Entry(mini,width=30,textvariable=adhar_var)
    adhar_entry.grid(row=9,column=1,padx=10,pady=10)
    adhar_invalid_msg=tk.Label(mini)  # Label to display any validation errors for the Adhar Card number
    adhar_invalid_msg.grid(row=10,column=1)

    # Create a section to upload a file as a reason for removing the account
    reason_label = tk.Label(mini, text="Upload Reason File:", font=("Arial", 10))
    reason_label.grid(row=11, column=0, padx=10, pady=10)
    reason_var = tk.StringVar()  # Variable to store the uploaded file path
    reason_entry = tk.Entry(mini, textvariable=reason_var, width=30, state='readonly')  # Entry to display the selected file
    reason_entry.grid(row=11, column=1, padx=10, pady=10)
    upload_btn = tk.Button(mini, text="Upload file", command=lambda : browse_file(reason_var))  # Button to browse and upload file
    upload_btn.grid(row=11, column=2, padx=10, pady=10)
    reason_invalid_msg = tk.Label(mini)  # Label to display any validation errors for the uploaded file
    reason_invalid_msg.grid(row=12, column=1)

    # Create radio buttons for selecting the type of account to be removed
    type_of_ac=['Saving_A/C','Current_A/C','FD_A/C']
    selected_ac = tk.StringVar(value=-1)  # Variable to store the selected account type
    
    for i in range(len(type_of_ac)):
        # Create a Radiobutton for each account type
        tk.Radiobutton(mini, text=type_of_ac[i], variable=selected_ac, value=type_of_ac[i]
                       ,font=("Arial",12,)).grid(row=13, column=i)
    radio_invalid_msg = tk.Label(mini)  # Label to display any validation errors for account type selection
    radio_invalid_msg.grid(row=14, column=1)

    # Label to display any final validation error messages
    submit_invalid_msg=tk.Label(mini,text='',font=('',13,'bold'))
    submit_invalid_msg.grid(row=17,column=0,padx=10,pady=10,columnspan=3)

    # List of entry widgets and corresponding invalid message labels for validation purposes
    entries = [name_entry, ac_no_Entry, sign_entry, mobile_entry, adhar_entry,reason_entry]
    invalid_msg=[name_invalid_msg,ac_no_invalid_msg,sign_invalid_msg,mobile_invalid_msg,adhar_invalid_msg,
             reason_invalid_msg,radio_invalid_msg,submit_invalid_msg]

    # Create a submit button that triggers validation and submission logic when clicked
    submit_btn=tk.Button(mini,text='SUBMIT',font=("Arial",10),command=lambda : remove_valid(entries,Toplevel,mobile_entry,adhar_entry,
                     ac_no_var,name_entry,sign_entry,reason_entry,selected_ac.get(),invalid_msg))
    submit_btn.grid(row=15,column=0,padx=10,pady=10,columnspan=2)

# Bind the Enter key event to move focus
    for entry in entries:
        entry.bind("<Return>", lambda event : focus_next_entry(event,entries, Toplevel=Toplevel,mobile_var=mobile_var,adhar_var=adhar_var,
                                                                               ac_no_var=ac_no_var,name_var=name_var,sign_var=sign_var,
                                                                               check='remove_ac',Reason_var=reason_var,ac_type=selected_ac,Msg=invalid_msg ))
        # Bind arrow keys to allow navigation between entry fields
        entry.bind("<Down>", lambda event : Arrow_keys(event,entries))
        entry.bind("<Up>", lambda event : Arrow_keys(event,entries))

    # Freeze the buttons in the main window until the Toplevel window is closed
    mini.grab_set()
    mini.resizable(True,True)  # Allow resizing of the Toplevel window
    mini.mainloop()  # Start the Tkinter main loop to display the Toplevel window

#valid checkup for withdraw amount
def withdraw_valid(entries, toplevel=None, amount_var=None, ac_no_var=None, sign_var=None, AC_TYPE=None, Message=None):
    global a  # Use global variable 'a' to track validation status
    a = 1  # Initialize 'a' to 1, indicating that validation has passed so far

    # Get the input values from Tkinter variables
    amt = amount_var.get()  
    ac_no = ac_no_var.get()     
    sign = sign_var.get()   
    invalid_msg = Message  # Reference to the list of message labels for displaying validation errors

    # Check if any of the required fields are empty
    if amt == "" or ac_no == "" or sign == "":
        invalid_msg[4].config(text="Please fill in all fields", fg="red")
        return False  # Exit function early if any field is empty
    else:
        invalid_msg[4].config(text='')

    # Validate the entered amount
    if not Validation.Amount(amt):
        a = 0  # Set validation flag to 0 indicating failure
        invalid_msg[0].config(text="Invalid amount entry")  # Show error message for invalid amount
        entries[0].focus_set()  # Set focus back to the amount entry field for correction
        return False    
    else:
        invalid_msg[0].config(text="")  # Clear error message if the amount is valid

    # Validate the sign entry
    if not Validation.Sign(sign):
        a = 0  # Set validation flag to 0 indicating failure
        invalid_msg[1].config(text="Invalid sign entry")  # Show error message for invalid sign
        entries[1].focus_set()  # Set focus back to the sign entry field for correction
        return False    
    else:
        invalid_msg[1].config(text="")  # Clear error message if the sign is valid

    # Validate that the account number is numeric
    if not ac_no.isdigit():
        a = 0   
        invalid_msg[2].config(text="Account Number should be a digit", fg="red")  # Show error message for invalid account number
        entries[2].focus_set()  # Set focus back to the account number entry field for correction
        return False    
    else:
        invalid_msg[2].config(text="")  # Clear error message if the account number is valid

    # Check that the account type is one of the valid types
    List = ['Saving_A/C', 'Current_A/C', 'FD_A/C']  # List of valid account types
    if AC_TYPE.get() in List:
        invalid_msg[3].config(text="   ", fg="red")     
    else:
        print(AC_TYPE.get())  # Debug print to check the selected account type
        invalid_msg[3].config(text="A/C type is required !!", fg="red")  # Show error message for invalid or missing account type
        entries[2].focus_set()      
        return      

    # If all validations pass, proceed with enabling the next entry field and submitting the form
    if a == 1:
        details = BankOperations.withdraw(int(ac_no), float(amt), sign, AC_TYPE.get())
        if details == 'Acount_not_exist':
            invalid_msg[2].config(text="Account Number does not exist", fg="red")
            entries[2].focus_set()

        elif details =="Ac_Type_Not_Match" :
            invalid_msg[3].config(text="Account Type does not match", fg="red")
            entries[2].focus_set() 

        elif details == "Invalid_sign":
            invalid_msg[1].config(text="Signature is not Valid!!", fg="red")
            entries[1].focus_set() 

        elif details == "Insufficient_fund":
            invalid_msg[0].config(text="Insufficient fund", fg="red")
            entries[0].focus_set()

        else:
            close_toplevel(toplevel)  # Close the Toplevel window
            msg.showinfo(title="Details", message=details)

def withdraw_amount():
    
    # Create a Toplevel window (popup window) for the "Withdraw Amount" functionality
    mini = tk.Toplevel()
    mini.title("Withdraw Amount")
    Toplevel = mini

    # Header label for instructions
    tk.Label(mini, text='Fill the below Information for Withdraw:', font=("Arial", 15, 'bold')).grid(row=0,column=0,padx=10,pady=10,columnspan=2)
    
    # Label and entry for entering the amount to withdraw
    tk.Label(mini, text="Enter Amount:", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=10)
    amount_var = tk.StringVar()  # Variable to store the entered amount
    amount_entry = tk.Entry(mini, width=30, textvariable=amount_var)
    amount_entry.grid(row=1, column=1, padx=10, pady=10)

    # Label to display validation errors for the amount
    amount_invalid_msg = tk.Label(mini, text="", fg="red")
    amount_invalid_msg.grid(row=2, column=1, padx=10, pady=0)

    # Label and entry for entering the user's signature
    tk.Label(mini, text='Enter Signature:', font=("Arial", 10)).grid(row=3, column=0, padx=10, pady=10)
    sign_var = tk.StringVar()  # Variable to store the entered signature
    sign_entry = tk.Entry(mini, width=30, textvariable=sign_var)
    sign_entry.grid(row=3, column=1, padx=10, pady=10)

    # Label to display validation errors for the signature
    sign_invalid_msg = tk.Label(mini, text="", fg="red")
    sign_invalid_msg.grid(row=4, column=1, padx=10, pady=0)

    # Label and entry for entering the account number
    tk.Label(mini, text='Enter Account Number:', font=("Arial", 10)).grid(row=5, column=0, padx=10, pady=10)
    ac_no_var = tk.StringVar()  # Variable to store the entered account number
    ac_no_entry = tk.Entry(mini, width=30, textvariable=ac_no_var)
    ac_no_entry.grid(row=5, column=1, padx=10, pady=10)

    # Label to display validation errors for the account number
    ac_no_invalid_msg = tk.Label(mini, text="", fg="red")
    ac_no_invalid_msg.grid(row=6, column=1, padx=10, pady=0)

    # List of entry widgets for validation and focus management
    entries = [amount_entry, sign_entry, ac_no_entry]
      
    # Define account types for radio button selection
    type_of_ac = ['Saving_A/C', 'Current_A/C', 'FD_A/C']

    # Create a StringVar to hold the value of the selected radiobutton
    selected_ac = tk.StringVar(value=-1)

    for i in range(len(type_of_ac)):
        # Create a Radiobutton for each account type
        tk.Radiobutton(mini, text=type_of_ac[i], variable=selected_ac, value=type_of_ac[i], font=("Arial", 12)).grid(row=7, column=i)
    
    # Label to display validation errors for account type selection
    radio_invalid_msg = tk.Label(mini, text="", fg="red")
    radio_invalid_msg.grid(row=8, column=1, padx=10, pady=0)

    # Label to display any final validation error messages
    submit_invalid_msg = tk.Label(mini, text='', font=('', 13, 'bold'))
    submit_invalid_msg.grid(row=10, column=0, padx=10, pady=10, columnspan=3)

    # List of invalid message labels for validation purposes
    invalid_msg = [amount_invalid_msg, sign_invalid_msg, ac_no_invalid_msg, radio_invalid_msg, submit_invalid_msg]

# Bind the Enter key event to move focus between fields
    for entry in entries:
        entry.bind("<Return>", lambda event: focus_next_entry(event, entries, Toplevel, amount_var=amount_var, ac_no_var=ac_no_var, sign_var=sign_var, check='credit', ac_type=selected_ac, Msg=invalid_msg))
        
        # Bind arrow keys to allow navigation between entry fields
        entry.bind("<Down>", lambda event: Arrow_keys(event, entries))
        entry.bind("<Up>", lambda event: Arrow_keys(event, entries))

    # Create a submit button that triggers validation and submission logic when clicked
    submit_btn = tk.Button(mini, text='SUBMIT', font=("Arial", 10), command=lambda: withdraw_valid(entries, Toplevel, amount_var, ac_no_var, sign_var, selected_ac, invalid_msg))
    submit_btn.grid(row=9, column=0, padx=10, pady=10, columnspan=2)

    # Freeze the buttons in the main window until the Toplevel window is closed
    mini.grab_set()
    mini.mainloop()  # Start the Tkinter main loop to display the Toplevel window


def check_valid(ac_no_entry, invalid_msg, entry, Toplevel):
    # Retrieve the entered account number from the Entry widget
    ac_no = ac_no_entry.get()

    # Check if the account number field is empty
    if ac_no == '':
        invalid_msg.config(text=" Please enter Account number.")

    # Check if the entered account number is not a number
    if not ac_no.isdigit():
        invalid_msg.config(text="Invalid input: Please enter a number.")
        return False  # Return False to indicate invalid input
    else:
        # Clear any previous error messages if the input is valid
        invalid_msg.config(text="")

        # Call a method to check if the account number exists in the database
        details = BankOperations.check(int(ac_no))

        # Check the result of the account number check
        if details == "Ac_Number_not_exist":
            invalid_msg.config(text="Account number does not exist.")  # Display error message if account number does not exist
            entry.focus_set()  # Set focus back to the entry field for user to re-enter the account number
        else:
            # Close the Toplevel window if account number exists
            close_toplevel(Toplevel)
            # Show a message box with the account details
            msg.showinfo(title="Details", message=details)


def check_account():
    # Create a new Toplevel window for the "Check Account Details" form
    M = tk.Toplevel()
    mini = M  # Alias the Toplevel window to 'mini' for easier reference

    # Add a label at the top of the window with instructions
    tk.Label(mini, text='Fill the below Information for Check A/C details:', font=("Arial", 15, 'bold')).grid(row=0, column=0, padx=10, pady=10, columnspan=2)
    
    # Create a label for the account number entry field
    ac_no = tk.Label(mini, text='Enter Account Number:', font=("Arial", 10))
    ac_no.grid(row=1, column=0, padx=10, pady=10)
    
    # Create an entry widget for the user to input the account number
    ac_no_var = tk.StringVar()  # Variable to store the account number
    ac_no_entry = tk.Entry(mini, width=30, textvariable=ac_no_var)
    ac_no_entry.grid(row=1, column=1, padx=10, pady=10)
    
    # Create a label to display invalid input messages
    invalid_msg = tk.Label(mini, text="", fg="red")
    invalid_msg.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

    # Create a submit button that triggers the check_valid function to validate the account number
    submit_btn = tk.Button(mini, text='SUBMIT', font=("Arial", 10), command=lambda: check_valid(ac_no_entry, invalid_msg, ac_no_entry, Toplevel=mini))
    submit_btn.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

    # List of entry widgets to manage focus traversal
    entries = [ac_no_entry]
    
    # Bind the Enter key to move focus to the next entry widget or trigger actions
    ac_no_entry.bind("<Return>", lambda event: focus_next_entry(event, entries, mini, check="Ac_check", ac_no_var=ac_no_entry, Msg=invalid_msg))

    # Freeze the main window until this Toplevel window is closed
    mini.grab_set()
    
    # Allow resizing of the Toplevel window
    mini.resizable(True, True)
    
    # Start the event loop for the Toplevel window
    mini.mainloop()

def Arrow_keys(event, entries):
    # Find the index of the current entry
    current_index = entries.index(event.widget)
    # Determine the next or previous index based on the arrow key pressed
    if event.keysym == "Down" or event.keysym == "Right":
        next_index = (current_index + 1) % len(entries)  # Move forward
    elif event.keysym == "Up" or event.keysym == "Left":
        next_index = (current_index - 1) % len(entries)  # Move backward
    else:
        return  # Ignore other keys

    # Focus on the next or previous entry
    entries[next_index].focus_set()

#function to Handle Enter key
def focus_next_entry(event=None, entries=None, Toplevel=None, mobile_var=None, adhar_var=None,
                     amount_var=None, name_var=None, sign_var=None, new_sign_var=None, ac_no_var=None, check=None, Reason_var=None, ac_type=None, Msg=None):
    # Find the index of the current entry widget
    current_index = entries.index(event.widget)
    # Calculate the index of the next entry widget in the list
    next_index = (current_index + 1) % len(entries)
    # Set focus to the next entry widget
    entries[next_index].focus_set()
   
    # Check the type of operation based on the 'check' parameter
    if check == 'create_ac':
        # Retrieve the values from the entry fields
        amt = amount_var.get()
        mbl = mobile_var.get()
        adr = adhar_var.get()
        nm = name_var.get()
        sign = sign_var.get()
        ac_Type = ac_type.get()

        # Check if any required field is empty; if so, do nothing
        if amt == "" or mbl == "" or adr == "" or nm == '' or sign == '' or ac_Type == '':
            return False
        else:
            # Call the function to validate and create a new account if all fields are filled
            create_valid(entries, Toplevel, mobile_var, adhar_var, amount_var, name_var, sign_var, ac_Type, Msg)

    elif check == 'credit':
        # Retrieve the values for withdrawal operation
        amt = amount_var.get()
        ac_no = ac_no_var.get()
        sign = sign_var.get()

        # Check if any required field is empty; if so, do nothing
        if amt == "" or ac_no == "" or sign == "":
            return False
        else:
            # Call the function to validate and process withdrawal if all fields are filled
            with_draw_fun_res = withdraw_valid(entries, Toplevel, amount_var, ac_no_var, sign_var, ac_type, Msg)

    elif check == 'deposit':
        # Retrieve the values for deposit operation
        amt = amount_var.get()
        ac_no = ac_no_var.get()
        
        # Check if any required field is empty; if so, do nothing
        if amt == "" or ac_no == "":
            return False
        else:
            # Call the function to validate and process deposit if all fields are filled
            deposit_valid(entries, Toplevel, amount_var, ac_no_var, Message=Msg)

    elif check == 'remove_ac':
        # Retrieve the values for account removal operation
        ac_no = ac_no_var.get()
        mbl = mobile_var.get()
        adr = adhar_var.get()
        nm = name_var.get()
        sign = sign_var.get()
        reason = Reason_var.get()
        Ac = ac_type.get()

        # Check if any required field is empty; if so, do nothing
        if ac_no == "" or mbl == "" or adr == "" or nm == "" or sign == '' or reason == '':
            return False
        else:
            # Call the function to validate and remove an account if all fields are filled
            remove_valid(entries, toplevel=Toplevel, mobile_no=mobile_var, adhar_no=adhar_var,
                         ac_no_var=ac_no_var, name_var=name_var, sign_var=sign_var, Reason=Reason_var, AC_TYPE=Ac, Message=Msg)

    elif check == "Ac_check":
        # For account check operation, call the validation function directly
        check_valid(ac_no_var, Msg, entries, Toplevel)

    return 'break'  # Prevent the default behavior of the Return key when this function is bound to an entry widget

def browse_file(reason_var):
        file_path = filedialog.askopenfilename(title="Select File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if file_path:
            reason_var.set(file_path)
        

def New_Update(ac_no_var=None, old_sign=None, new_sign=None, name=None, mobile_no=None, Entries=None, invalids=None, topleve=None):
    # Read the CSV file to get the latest account information
    read = Read_csv()
    
    # Get the account number, old signature, new signature, name, and mobile number from the input fields
    ac = ac_no_var.get()  # Account number
    sign = old_sign.get()  # Old signature
    name = name.get()  # Name
    new_sign = new_sign.get()  # New signature
    mobile_no = mobile_no.get()  # Mobile number
    Entries = Entries  # List of entry fields
    invalids = invalids  # List of invalid message labels
    
    # Check if the account number or old signature field is empty
    if ac == "" or sign == '':
        invalids[5].config(text="Please fill all the REQUIRED fields", fg='red')
        return False
    else:
        invalids[5].config(text="")

    # Check if the account number is numeric
    if not ac.isdigit():
        Entries[0].focus_set()
        invalids[0].config(text="Account Number should be numeric", fg='red')
        return False
    else:
        invalids[0].config(text="  ")

    # Check if the account number exists in the CSV file
    if int(ac) not in read["A/C No:"].values:
        Entries[0].focus_set()
        invalids[0].config(text="Account Number does not exist")
        return False
    
    # Find the index of the account number in the CSV file
    index = read.index[read["A/C No:"] == int(ac)].tolist()[0]

    # Validate the old signature
    if read.at[index, "Sign:"] == sign:
        updated = False  # Track if any update is made

        # Update the name if provided and valid
        if name:
            if Validation.Name(name):  # Validate the name
                invalids[2].config(text="")
                read.at[index, "Names"] = name  # Update the name in the CSV data
                msg.showinfo("Information", f"Name Updated to {name}")
                updated = True
            else:
                invalids[2].config(text="Invalid Name", fg="red")
                Entries[2].focus_set()
                return False

        # Update the signature if provided and valid
        if new_sign:
            if Validation.Sign(new_sign):  # Validate the new signature
                invalids[3].config(text="")
                read.at[index, "Sign:"] = new_sign  # Update the signature in the CSV data
                updated = True
            else:
                invalids[3].config(text="Invalid Signature", fg="red")
                Entries[3].focus_set()
                return False

        # Update the mobile number if provided and valid
        if mobile_no:
            if Validation.Mobile(mobile_no):  # Validate the mobile number
                invalids[4].config(text="")
                read.at[index, "Mobile_No:"] = mobile_no  # Update the mobile number in the CSV data
                updated = True
            else:
                invalids[4].config(text="Invalid Mobile Number", fg="red")
                Entries[4].focus_set()
                return False

        # Save changes to the CSV file if any updates were made
        if updated:
            read.to_csv(Acounts_file, index=False)  # Write the updated data back to the CSV file
            close_toplevel(topleve)  # Close the toplevel window
            msg.showinfo("Information", "Account details Successfully Updated")
        else:
            # If no changes were made, show a message and set focus to the name entry
            invalids[5].config(text="No changes were made!", fg="red")
            Entries[2].focus_set()
            return

    else:
        # If the old signature is not valid, show an error message and set focus to the signature entry
        invalids[1].config(text="Signature is not Valid!", fg='red')
        Entries[1].focus_set()

def edit_ac():
    # Create a secondary window using Toplevel
    mini = tk.Toplevel()
    mini.title("Edit Account")  # Set the title of the window
    Toplevel = mini  # Assign the secondary window to a variable for later use

    # Label and entry field for account number
    ac_no = tk.Label(mini, text="Enter Account Number (*REQUIRED)", font=("Arial", 10))
    ac_no.grid(row=0, column=0, padx=10, pady=5)  # Position the label in the grid
    ac_no_var = tk.StringVar()  # Create a StringVar to store the account number
    ac_no_entry = tk.Entry(mini, width=30, textvariable=ac_no_var)  # Create an entry widget for account number input
    ac_no_entry.grid(row=0, column=1, padx=10, pady=5)  # Position the entry widget in the grid

    # Label to display invalid message for account number input
    ac_no_invalid_msg = tk.Label(mini)
    ac_no_invalid_msg.grid(row=1, column=1)

    # Label and entry field for old signature
    sign = tk.Label(mini, text="Enter Old Signature (*REQUIRED)", font=("Arial", 10))
    sign.grid(row=2, column=0, padx=10, pady=5)
    sign_entry = tk.Entry(mini, width=30)  # Entry widget for old signature input
    sign_entry.grid(row=2, column=1, padx=10, pady=5)

    # Label to display invalid message for old signature input
    sign_invalid_msg = tk.Label(mini)
    sign_invalid_msg.grid(row=3, column=1)

    # Label and entry field for new name
    name = tk.Label(mini, text="Enter New Name (optional)", font=("Arial", 10))
    name.grid(row=4, column=0, padx=10, pady=5)
    name_entry = tk.Entry(mini, width=30)  # Entry widget for new name input
    name_entry.grid(row=4, column=1, padx=10, pady=5)

    # Label to display invalid message for new name input
    name_invalid = tk.Label(mini)
    name_invalid.grid(row=5, column=1)

    # Label and entry field for new signature
    new_sign = tk.Label(mini, text="Enter New Signature (optional)", font=("Arial", 10))
    new_sign.grid(row=6, column=0, padx=10, pady=5)
    new_sign_entry = tk.Entry(mini, width=30)  # Entry widget for new signature input
    new_sign_entry.grid(row=6, column=1, padx=10, pady=5)

    # Label to display invalid message for new signature input
    new_sign_invalid = tk.Label(mini)
    new_sign_invalid.grid(row=7, column=1)

    # Label and entry field for new mobile number
    mobile = tk.Label(mini, text="Enter New Mobile Number (optional)", font=("Arial", 10))
    mobile.grid(row=8, column=0, padx=10, pady=5)
    mobile_entry = tk.Entry(mini, width=30)  # Entry widget for new mobile number input
    mobile_entry.grid(row=8, column=1, padx=10, pady=5)

    # Label to display invalid message for new mobile number input
    mobile_invalid = tk.Label(mini)
    mobile_invalid.grid(row=9, column=1)

    # Label to display a general invalid message for form submission
    submit_invalid_msg = tk.Label(mini, text='', font=('', 13, 'bold'))
    submit_invalid_msg.grid(row=11, column=0, padx=10, pady=10, columnspan=3)

    # List of invalid message labels and entry fields for validation
    invalids_msg = [ac_no_invalid_msg, sign_invalid_msg, name_invalid, new_sign_invalid, mobile_invalid, submit_invalid_msg]
    entries = [ac_no_entry, sign_entry, name_entry, new_sign_entry, mobile_entry]

    # Bind keyboard events for navigating between entries
    for entry in entries:
        # Bind the Return (Enter) key to move to the next entry or perform checks
        entry.bind("<Return>", lambda event: focus_next_entry(event, entries, ac_no_var=ac_no_var, sign_var=sign_entry,
                                                             new_sign_var=new_sign_entry, name_var=name_entry,
                                                             check='update', Msg=invalids_msg, Toplevel=Toplevel))
        # Bind the Up arrow key to move focus to the previous entry
        entry.bind("<Up>", lambda event: Arrow_keys(event, entries))
        # Bind the Down arrow key to move focus to the next entry
        entry.bind("<Down>", lambda event: Arrow_keys(event, entries))

    # Submit button for updating account information
    submit_btn = tk.Button(mini, text="Submit", font=("Arial", 10), command=lambda: New_Update(ac_no_var, sign_entry,
                                                                                               new_sign_entry,
                                                                                               name_entry, mobile_entry,
                                                                                               entries, invalids_msg, Toplevel))
    submit_btn.grid(row=10, column=0, pady=10, columnspan=2)

    # Grab the focus to prevent user interaction with other windows until this one is closed
    mini.grab_set()
    mini.mainloop()  # Start the event loop for the secondary window

def load_csv(Secret_key_Entry, label, button, invalid, tree, event=None):
    Secret_key = "1542"  # Predefined secret key for authentication
    enter_key = Secret_key_Entry.get()  # Get the entered secret key from the entry field

    # Check if the secret key entry field is empty
    if Secret_key_Entry.get() == '':
        invalid.config(text="Please enter the secret key!", fg='red')  # Display error message
        Secret_key_Entry.focus_set()  # Set focus back to the entry field
        return  # Exit the function

    # Check if the entered key does not match the predefined secret key
    if enter_key != Secret_key:
        Secret_key_Entry.focus_set()  # Set focus back to the entry field
        button.config(bg='SystemButtonFace')  # Reset button background color to default
        invalid.config(text="Entered Key is Wrong!!")  # Display error message
        return False  # Exit the function with a False return value

    else:
        # If the entered key is correct, remove the input elements and error message
        label.destroy()  # Remove the label from the GUI
        Secret_key_Entry.grid_remove()  # Remove the entry field from the grid
        invalid.grid_remove()  # Remove the error message label from the grid
        button.grid_remove()  # Remove the button from the grid

        data = tree  # Assign the treeview object to the variable 'data'

        # Open the CSV file and read its content
        with open(Acounts_file) as file:
            read = csv.reader(file)  # Create a CSV reader object
            headers = next(read)  # Read the first row as headers

            # Define the columns in the treeview
            data["columns"] = headers  # Set the columns of the treeview to the CSV headers
            data["show"] = "headings"  # Hide the default empty first column

            # Initialize dictionary to store the maximum column widths for each header
            max_col_widths = {header: len(header) for header in headers}

            # Create the headers in the treeview
            for heading in headers:
                data.heading(heading, text=heading, anchor='nw')  # Set the heading text and alignment

            # Insert rows from the CSV file into the treeview
            for row in read:
                # Update the maximum column widths based on the data in each row
                for idx, value in enumerate(row):
                    col_width = max(max_col_widths[headers[idx]], len(value))
                    max_col_widths[headers[idx]] = col_width

                # Insert the current row into the treeview
                data.insert("", "end", values=row)

            data['height'] = 20  # Set the height of the treeview to display 20 rows


def Acounts():
    # Create a new top-level window for displaying account details
    mini = tk.Toplevel()
    mini.title("Acounts details")

    # Create a frame to hold the Treeview widget
    frame = tk.Frame(mini, height=300, width=300)
    frame.grid(row=0, column=0, sticky="nsew")  # Position frame in the window using grid

    # Configure the style for the Treeview headings
    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Arial', 15, 'bold'))  # Set the font style and size for the Treeview headings

    # Create the Treeview widget to display account details
    tree = ttk.Treeview(frame)
    tree.pack(padx=20, pady=20, fill="both", expand=True)  # Fill the frame and expand to available space

    # Create a label for the secret key entry field
    Secret_key = tk.Label(mini, text='Enter secret key:', font=('Arial', 12, 'bold'))
    Secret_key.grid(row=1, column=0)  # Position the label using grid

    # Create an entry field for the user to input the secret key
    Secret_key_var = tk.StringVar()  # Variable to hold the value of the entry field
    Secret_key_Entry = tk.Entry(mini, width=30, textvariable=Secret_key_var)
    Secret_key_Entry.grid(row=1, column=1)  # Position the entry field using grid
    Secret_key_Entry.focus_set()  # Set focus on the entry field for user convenience

    # Label to display invalid secret key messages
    Secret_key_invalid = tk.Label(mini, font=('Arial'), fg='red')
    Secret_key_invalid.grid(row=2, column=1)  # Position the label using grid

    # Create a submit button that loads the CSV when clicked
    submit_btn = tk.Button(mini, text='Submit & Open_file', font=('Arial', 13, 'bold'),
                           command=lambda: load_csv(Secret_key_Entry, Secret_key, submit_btn, Secret_key_invalid, tree))
    submit_btn.grid(row=1, column=2, padx=20, pady=20)  # Position the button using grid

    # Bind the Enter key to trigger the CSV loading function
    Secret_key_Entry.bind("<Return>", lambda event: load_csv(Secret_key_Entry, Secret_key, submit_btn, Secret_key_invalid, tree, event=event))

    mini.resizable(True, True)  # Allow the window to be resizable in both directions
    mini.mainloop()  # Start the event loop for this top-level window


# for creat Bank Operation  main window
# Initialize the main window
window = tk.Tk()

# Get screen width and height to set the window size to full screen
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
window.geometry("%dx%d" % (w, h))  # Set the window size to the screen size

# Set the title and icon for the main window
window.title("Banking System")
icon = tk.PhotoImage(file='bakn1.png')
window.iconphoto(False, icon)

# Create a canvas with the full window width and height
canvas = tk.Canvas(window, width=w, height=h)

# Set a background image (wallpaper) for the window
wl = tk.PhotoImage(file="bank_26.png")
wallpaper = tk.Label(window, image=wl)
wallpaper.place(x=0, y=0, relwidth=1, relheight=1)  # Stretch the image to cover the entire window

# Create a frame to hold the buttons at the bottom of the window
button_frame = tk.Frame(window, bg='white')  # Set background color for visibility
button_frame.grid(row=1, column=0, sticky='ew', padx=10, pady=10)  # Position frame at the bottom

# Configure the grid system to ensure proper resizing and layout
window.grid_rowconfigure(0, weight=1)  # Allow row 0 to expand
window.grid_rowconfigure(1, weight=0)  # Keep row 1 fixed in size
window.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand

# Configure columns in the button frame to expand evenly
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(2, weight=1)
button_frame.grid_columnconfigure(3, weight=1)
button_frame.grid_columnconfigure(4, weight=1)
button_frame.grid_columnconfigure(5, weight=1)


# Create buttons and add them to the frame, setting properties like text, command, and appearance

# Button to create a new account
tk.Button(button_frame, text="Create Account", command=create_account,
          compound="left", font=("Arial", 12, 'bold'),
          activebackground='blue', bg='green', fg='white',
          borderwidth=4, cursor="hand2", height=3).grid(row=0, column=0, padx=5, pady=5, sticky='ew')

# Button to update an account
tk.Button(button_frame, text="Update Account", command=edit_ac,
          compound="left", font=("Arial", 12, 'bold'),
          activebackground='blue', bg='aqua', fg='white',
          borderwidth=4, cursor="hand2", height=3).grid(row=0, column=1, padx=5, pady=5, sticky='ew')

# Button to deposit money
tk.Button(button_frame, text="Deposit", command=deposit_amount,
          compound="left", font=("Arial", 12, 'bold'),
          activebackground='blue', bg='#fc9342',
          borderwidth=4, cursor="hand2", height=3).grid(row=0, column=2, padx=5, pady=5, sticky='ew')

# Button to withdraw money
tk.Button(button_frame, text="Withdraw", command=withdraw_amount,
          compound="left", font=("Arial", 12, 'bold'),
          activebackground='blue', bg='#c842fc',
          borderwidth=4, cursor="hand2", height=3).grid(row=0, column=3, padx=5, pady=5, sticky='ew')

# Button to check an account's details
tk.Button(button_frame, text="Check A/C", command=check_account,
          compound="left", font=("Arial", 12, 'bold'),
          activebackground='blue', bg='#FFDAB9',
          borderwidth=4, cursor="hand2", height=3).grid(row=0, column=4, padx=5, pady=5, sticky='ew')

# Button to remove an account
tk.Button(button_frame, text="Remove A/C", command=remove_ac, compound="left",
          font=("Arial", 12, 'bold'), height=3, activebackground='red', bg='gray',
          borderwidth=4, cursor="hand2").grid(row=0, column=5, padx=5, pady=5, sticky='ew')

# Exit button to close the application
tk.Button(button_frame, text="Exit", bg='red', font=("Arial", 12, 'bold'), height=3, width=7,
          command=quit, cursor="hand2").grid(row=0, column=6, padx=5, pady=5, sticky='ew')

# Button to check accounts
tk.Button(button_frame, text="Acounts check", command=Acounts,
          compound="left", font=("Arial", 12, 'bold'),
          activebackground='blue', bg='navy blue', fg='white',
          borderwidth=4, cursor="hand2", height=3, width=5).grid(row=1, column=0, sticky='ew',padx=5, pady=40)

# Allow the main window to be resizable
window.resizable(True, True)

# Start the Tkinter event loop to run the application
window.mainloop()
