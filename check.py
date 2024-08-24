#Import required libraries
import datetime as dt
import pandas as pd
import re
import tkinter as tk
from tkinter import messagebox as msg
from PIL import Image,ImageTk
from tkinter import ttk
import time
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
            if msg.askretrycancel("Error", f"Account No: {ac_no} does not exist"):# pop up message for error and ask for retry
                ac=1
            else:
                ac=0
            return ac
  

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
                        if msg.askretrycancel("Error", f"Insufficient balance in A/C No: {ac_no}"):#if balance is low and enterd amount is high on that time this pop will apeare
                            ac=4
                        else:
                            ac=0    
                        return ac
                else:
                    if msg.askretrycancel("Error", f"Account No: {ac_no} Signature is not Matched!"):#if signature is mismatched on that time this pop will apeare
                        ac=3
                    else:
                        ac=0    
                    return ac
            else:
                if msg.askretrycancel("Error", f"Account No: {ac_no} is not match the Type of bank acount"):
                    ac=2
                else:
                    ac=0
                return ac
        else:
            if msg.askretrycancel("Error", f"Account No: {ac_no} does not Exists!"):#if entered acount number is not existed then pop w.
                ac=2
            else:
                ac=0    
            return ac
   
    #function to check acount details 
    def check(account_no):
        #account_no = int(input("Enter account number: "))
        read=Read_csv()
        if account_no in read["A/C No:"].values:#for check acount number is existing or not 
            index = read.index[read["A/C No:"] == account_no].tolist()[0]
            
            details=(f"\n\nName : {read.at[index, 'Names']}\nA/C No : {read.at[index, 'A/C No:']}\nAvailable Balance : {read.at[index, 'Balance :']}")
            return details
        else:
            if msg.askretrycancel("Error", "Account number does not exist."):#if Acount number is not existed this popup notification will apeare
                ac=1
            else:
                msg.showinfo("Information","Thank you for using our services")
                ac=0
            return ac   
        
    def remove(ac_no,name,sign,adhar_no,mobile_no,reason):
        read = Read_csv()

        if ac_no in read["A/C No:"].values:
            index = read.index[read["A/C No:"] == ac_no].tolist()[0]  # Find the index of the account number
            #Condition to check given details are valid or not
            if read.at[index, "Names"] == name:
                if read.at[index, "Sign:"] == sign:
                    if read.at[index, "Mobile_No:"] == mobile_no:
                        if read.at[index, "Adhar_No:"] == adhar_no:                     
                            return True
                        else:
                            if msg.askretrycancel("Error", "Adhar number does not match"):
                                return 2
                            else:
                                return 3
                    else:
                        if msg.askretrycancel("Error", "Mobile number does not match"):
                            return 2
                        else:
                            return 3
                        
                else:
                    if msg.askretrycancel("Error", "Signature does not match"):
                        return 2
                    else:
                        return 3
                    
            else:
                if msg.askretrycancel("Error", "Name does not match"):
                    return 2
                else:
                    return 3
                
        else:
            if msg.askretrycancel("Error", f"Account No: {ac_no} does not exist"):  # If account number is not found
                return 2
            else:
                return 3

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
def focus_next_entry(event=None,entries=None,Toplevel=None,mobile_var=None,adhar_var=None,
                     amount_var=None,name_var=None,sign_var=None,new_sign_var=None,ac_no_var=None,check=None,Reason_var=None,ac_type=None,Msg=None):
    # Find the index of the current entry
    current_index = entries.index(event.widget)
    # Calculate the index of the next entry
    next_index = (current_index + 1) % len(entries)
    # Focus on the next entry
    entries[next_index].focus_set()#submit.focus_set()
   
    if check=='create_ac':#conditions to check we are in which type of operations 
        amt = amount_var.get()
        mbl = mobile_var.get()
        adr = adhar_var.get()
        nm = name_var.get()
        sign = sign_var.get()
        ac_Type = ac_type.get()

        if amt=="" or mbl=="" or adr=="" or nm=='' or sign=='' or ac_Type=='':
            return False
        else:
            create_valid(entries,Toplevel,mobile_var,adhar_var,amount_var,name_var,sign_var,ac_Type,Msg)

    elif check=='credit':#conditions to check we are in which type of operations 
        amt=amount_var.get()
        ac_no=ac_no_var.get()
        sign=sign_var.get()

        if amt=="" or ac_no=="" or sign=="" :#if once all required input feilds are filles then only it enters next step
            return False
        
        else:
            with_draw_fun_res =withdraw_valid(entries,Toplevel,amount_var,ac_no_var,sign_var,ac_type,Msg)

    elif check=='deposit':#conditions to check we are in which type of operations 
        amt = amount_var.get()
        ac_no = ac_no_var.get()
        if amt=="" or ac_no=="":#if once all required input feilds are filles then only it enters next step
            return False
        else:
            deposit_valid(entries,Toplevel,amount_var,ac_no_var,Message=Msg)  

    elif check=='remove_ac':#conditions to check we are in which type of operations 
        ac_no = ac_no_var.get()
        mbl = mobile_var.get()
        adr = adhar_var.get()
        nm = name_var.get()
        sign = sign_var.get()
        reason=Reason_var.get()
        Ac=ac_type.get()

        if ac_no=="" or mbl=="" or adr=="" or nm=="" or sign=='' or reason =='':#if once all required input feilds are filles then only it enters next step
            return False
        else:
            remove_valid(entries,toplevel=Toplevel,mobile_no=mobile_var,adhar_no=adhar_var,
                     ac_no_var=ac_no_var,name_var=name_var,sign_var=sign_var,Reason=Reason_var,AC_TYPE=ac_type,Message=Msg)
            
    # elif check =='update':
    #     if ac_no_var.get()=='' or sign_var.get()=="":
    #         return False
    #     else:

    #         New_Update(ac_no_var,sign_var,new_sign_var,name_var,mobile_var,entries,Msg,Toplevel)
    return 'break'

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

#valid checkup for Deposit amount
def deposit_valid(entries,toplevel=None, amount_var=None, ac_no_var=None,Sub_btn=None,Message=None):
    global a
    a=1
    amt=amount_var.get()
    ac_no=ac_no_var.get()
    invalid_msg = Message

    if amt=="" or ac_no=="" :
        a=0
        invalid_msg[2].config(text="Please fill all the fields",fg="red")
        return False
    else:
        invalid_msg[2].config(text='')

    if not Validation.Amount(amt):
        a = 0
        invalid_msg[0].config(text="Invalid Amount Entry",fg="red")
        entries[0].focus_set()
        return False
    else:
        invalid_msg[0].config(text="")
    
    if not ac_no.isdigit():
        a = 0
        invalid_msg[1].config(text="Invalid Account Number",fg="red")
        entries[1].focus_set()
        return False
    else:
        invalid_msg[1].config(text="")
    if a == 1:
        details = BankOperations.deposit(int(ac_no), int(amt))
        if details == 0:
            close_toplevel(toplevel)  # Close the Toplevel window if the deposit is successful
        elif details == 1:
            return False  # Return False if the deposit fails
        else:
            close_toplevel(toplevel)    
            msg.showinfo(title="Details", message=details)  # Show account details after a successful deposi
    
def remove_valid(entries, toplevel=None, mobile_no=None, adhar_no=None, ac_no_var=None, name_var=None,
                 sign_var=None, Reason=None, AC_TYPE=None, Message=None):
    global a  # Use global variable 'a' to track validation status
    a = 1  # Initialize 'a' to 1, indicating that validation has passed so far

    # Get input values from Tkinter variables
    ac_no = ac_no_var.get()     
    mobile_no = mobile_no.get()   
    adhar_no = adhar_no.get()    
    name = name_var.get()     
    sign = sign_var.get()   
    reason = Reason.get()   
    Ac = AC_TYPE
    invalid_msg = Message  #  list of message labels for displaying validation errors
    read=Read_csv()

    # Check if any of the required fields are empty
    if ac_no == "" or mobile_no == "" or adhar_no == "" or name == "" or sign == '' or reason == '':
        invalid_msg[6].config(text="Please fill all the fields",fg="red")
        return False  # Exit function early if any field is empty

    # Validate the entered name
    if not Validation.Name(name):
        a = 0  # Set validation flag to 0 indicating failure
        invalid_msg[0].config(text="Invalid name entry", fg='red')  # Show error message for invalid name
        entries[0].focus_set()  # Set focus back to the name entry field for correction
        return False    
    else:
        invalid_msg[0].config(text="")  # Clear error message if the name is valid

    if not ac_no.isdigit():
        invalid_msg[1].config(text="Invalid input: Please enter a number.")
        entries[1].focus_set() 
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
        entries[3].focus_set()  
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

    # Check that the account type is one of the valid types
    List = ['Saving_A/C', 'Current_A/C', 'FD_A/C']  # List of valid account types
    if Ac in List:
       invalid_msg[5].config(text="   ", fg="red")  # Clear any previous error message for account type
    else:

        invalid_msg[5].config(text="A/C type is required !!", fg="red")  # Show error message for invalid or missing account type
        entries[4].focus_set()  # Set focus back to the Aadhar entry field if account type is invalid
        return  # Exit the function since account type is invalid

    # If all validations pass, proceed with enabling the next entry field and submitting the form
    if a == 1:
        fun_response = BankOperations.remove(int(ac_no), str(name), str(sign), int(adhar_no), int(mobile_no), reason)
        if fun_response == True:
                # If account removal is successful, update the CSV file
            ac = int(ac_no)
            index = read.index[read["A/C No:"] == ac].tolist()[0]  # Find the index of the account to remove
            print("index is =", index)
            read.drop(index, inplace=True)  # Remove the row from the DataFrame
            read.to_csv(Acounts_file, index=False)  # Save the changes to the CSV file
            t = dt.datetime.now()  # Get the current datetime
            time = (t.strftime("%d-%m-%Y   %H:%M:%S "))  # Format the datetime for logging
            close_toplevel(toplevel)    
            colsed(name, ac, sign, mobile_no=mobile_no, adhar_no=adhar_no, time=time, reason=reason)  #update the closed account details
            msg.showinfo("Information", "Account removed successfully")     
        else:
            if fun_response == 3:
                close_toplevel(toplevel)    
            elif fun_response == 2:
                return 1  # Disable the next entry field if validation failed

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
        if details == 0:
            close_toplevel(toplevel)    
        else:
                # Disable the next entry field if submission failed
            # Handle specific cases of submission failure by setting focus back to the corresponding entry field
            if details == 2:
                entries[2].focus_set()  # Focus back to account number entry if it was incorrect
            elif details == 3:
                entries[1].focus_set()  # Focus back to sign entry if it was incorrect
            elif details == 4:
                entries[0].focus_set()  # Focus back to amount entry if it was incorrect
            else:
                close_toplevel(toplevel)  # Close the Toplevel window
                msg.showinfo(title="Details", message=details)

def Submit(entries=None, Toplevel=None, codition=None, name_entry=None, amount_entry=None, sign_entry=None,
           mobile_entry=None, adhar_entry=None, ac_no_var=None, Reason=None, AC_type=None,invalids=None):
    read = Read_csv()  # Read the CSV file and store its contents in a DataFrame
    # Get input values from the Tkinter widgets
    name = name_entry   
    init_balance = amount_entry     
    sign = sign_entry   
    mobile_no = mobile_entry    
    adhar_no = adhar_entry  
    ac_No = ac_no_var   
    reason = Reason     
    
    # Check the condition to determine which operation to perform
    if codition == 1:
        if not name or not init_balance or not sign or not mobile_no or not adhar_no :
            msg.showerror("Error", "All fields are required")  # Show an error message if any field is empty
            return False    
        else:
           create_valid(entries,Toplevel,mobile_no,adhar_no,init_balance,name,sign,AC_type.get(),invalids)

    elif codition == 2:
        # Depositing money into an existing account
        # Validate that the required fields are filled
        if not init_balance or not ac_No:
            msg.showerror("Error", "All fields are required")  # Show an error message if any field is empty
        
            # Call the deposit function from BankOperations to deposit money into the account
        else:
            deposit_valid(entries,Toplevel,amount_entry,ac_no_var,Message=invalids)

    elif codition == 3:
        # Withdrawing money from an existing account
        # Validate that the required fields are filled
        if not init_balance or not ac_No or not sign:
            msg.showerror("Error", "All fields are required")  # Show an error message if any field is empty
        else:
            withdraw_valid(entries,Toplevel,init_balance,ac_no_var,sign,AC_type,invalids)

    elif codition == 4:
        # Removing an existing account
        # Validate that all required fields are filled
        if not name or not ac_No or not sign or not mobile_no or not adhar_no or not reason:
            msg.showerror("Error", "All fields are required")  # Show an error message if any field is empty
            return False    
        else:
            remove_valid(entries,Toplevel,mobile_no,adhar_no,
                     ac_no_var,name_entry,sign_entry,Reason,AC_type,invalids)
            # Call the remove function from BankOperations to remove the account
            # fun_response = BankOperations.remove(int(ac_No), str(name), str(sign), int(adhar_no), int(mobile_no), reason)
            # if fun_response == True:
            #     # If account removal is successful, update the CSV file
            #     ac = int(ac_No)
            #     index = read.index[read["A/C No:"] == ac].tolist()[0]  # Find the index of the account to remove
            #     print("index is =", index)
            #     read.drop(index, inplace=True)  # Remove the row from the DataFrame
            #     read.to_csv(Acounts_file, index=False)  # Save the changes to the CSV file
            #     t = dt.datetime.now()  # Get the current datetime
            #     time = (t.strftime("%d-%m-%Y   %H:%M:%S "))  # Format the datetime for logging
            #     close_toplevel(Toplevel)    
            #     colsed(name, ac, sign, mobile_no=mobile_no, adhar_no=adhar_no, time=time, reason=reason)  #update the closed account details
            #     msg.showinfo("Information", "Account removed successfully")     
            # else:
            #     if fun_response == 3:
            #         close_toplevel(Toplevel)    
            #     elif fun_response == 2:
            #         return 1  
                
#function for create acount button 
def create_account():

    def P():
        return (selected_ac.get())
      
    mini=tk.Toplevel(window)#to create child window
    mini.title("Create Account")
    Toplevel=mini

    tk.Label(mini,text='Fill the below Information for create A/C :',font=("Arial",15,'bold')).grid(row=0,column=0,padx=10,pady=10,columnspan=2)
 # create lables and entry box
    name = tk.Label(mini, text="Enter Name:", font=("Arial", 10))
    name.grid(row=1, column=0, padx=10, pady=10)
    name_var = tk.StringVar()
    name_entry = tk.Entry(mini, textvariable=name_var, width=30)
    name_entry.grid(row=1, column=1, padx=10, pady=10)

    name_invalid_msg = tk.Label(mini, text="", fg="red")
    name_invalid_msg.grid(row=2, column=1, padx=10, pady=0)

# Amount
    amount = tk.Label(mini, text="Enter Initial Amount:", font=("Arial", 10))
    amount.grid(row=3, column=0, padx=10, pady=10)
    amount_var = tk.StringVar()
    amount_entry = tk.Entry(mini, width=30, textvariable=amount_var)
    amount_entry.grid(row=3, column=1, padx=10, pady=10)

    amount_invalid_msg = tk.Label(mini, text="", fg="red")
    amount_invalid_msg.grid(row=4, column=1, padx=10, pady=0)

# Signature
    sign = tk.Label(mini, text="Enter Signature:", font=("Arial", 10))
    sign.grid(row=5, column=0, padx=10, pady=10)
    sign_var = tk.StringVar()
    sign_entry = tk.Entry(mini, textvariable=sign_var, width=30)
    sign_entry.grid(row=5, column=1, padx=10, pady=10)

    sign_invalid_msg = tk.Label(mini, text="", fg="red")
    sign_invalid_msg.grid(row=6, column=1, padx=10, pady=0)

# Mobile
    mobile = tk.Label(mini, text="Enter Mobile Number:", font=("Arial", 10))
    mobile.grid(row=7, column=0, padx=10, pady=10)
    mobile_var = tk.StringVar()
    mobile_entry = tk.Entry(mini, width=30, textvariable=mobile_var)
    mobile_entry.grid(row=7, column=1, padx=10, pady=10)

    mobile_invalid_msg = tk.Label(mini, text="", fg="red")
    mobile_invalid_msg.grid(row=8, column=1, padx=10, pady=0)

# Adhar
    adhar = tk.Label(mini, text="Enter Adhar Card Number:", font=("Arial", 10))
    adhar.grid(row=9, column=0, padx=10, pady=10)
    adhar_var = tk.StringVar()
    adhar_entry = tk.Entry(mini, width=30, textvariable=adhar_var)
    adhar_entry.grid(row=9, column=1, padx=10, pady=10)

    adhar_invalid_msg = tk.Label(mini, text="", fg="red")
    adhar_invalid_msg.grid(row=10, column=1, padx=10, pady=0)


    type_of_ac=['Saving_A/C','Current_A/C','FD_A/C']

    # Create a StringVar to hold the value of the selected radiobutton
    selected_ac = tk.StringVar(value=-1)

    for i in range(len(type_of_ac)):
        # Create a Radiobutton for each account type
        tk.Radiobutton(mini, text=type_of_ac[i], variable=selected_ac, value=type_of_ac[i],font=("Arial",12,),command=P).grid(row=11, column=i)
    radio_invalid_msg = tk.Label(mini, text="", fg="red")
    radio_invalid_msg.grid(row=12, column=1, padx=10, pady=0)

    submit_invalid_msg=tk.Label(mini,text='',font=('',13,'bold'))
    submit_invalid_msg.grid(row=14,column=0,padx=10,pady=10,columnspan=3)

    entries = [name_entry, amount_entry, sign_entry, mobile_entry, adhar_entry]
    invalid_msg=[name_invalid_msg, amount_invalid_msg, sign_invalid_msg, mobile_invalid_msg, adhar_invalid_msg,radio_invalid_msg,submit_invalid_msg]

# Bind the Enter key event to move focus
    for entry in entries:
        entry.bind("<Return>", lambda event, entries=entries: focus_next_entry(event,entries, Toplevel,mobile_var,adhar_var,
                                                                               amount_var,name_var,sign_var,check='create_ac',ac_type=selected_ac,Msg=invalid_msg))
        entry.bind("<Down>", lambda event, entries=entries: Arrow_keys(event,entries))
        entry.bind("<Up>", lambda event, entries=entries: Arrow_keys(event,entries))

    
    submit_btn=tk.Button(mini,text='SUBMIT',font=("Arial",10,'bold'),command=lambda : create_valid(entries,Toplevel,mobile_var,adhar_var,amount_var,name_var,sign_var,selected_ac.get(),invalid_msg))
    submit_btn.grid(row=13,column=0,padx=10,pady=10,columnspan=2)


    mini.grab_set()# to freeze the buttons in main window untill close toplevel window
    mini.resizable(True,True)
    mini.mainloop()


#function for deposit button
def deposit_amount():
          
    mini=tk.Toplevel()
    mini.title("Deposit Amount")
    Toplevel=mini

    tk.Label(mini,text='Fill the below Information for Deposit :',font=("Arial",15,'bold')).grid(row=0,column=0,padx=10,pady=10,columnspan=2)
    #to create lables and entry box
     #to create lables and entry box
    amount=tk.Label(mini,text="Enter Initial Amount :",font=("Arial",10))
    amount.grid(row=1,column=0,padx=10,pady=10)
    amount_var=tk.StringVar()
    amount_entry=tk.Entry(mini,width=30,textvariable=amount_var)
    amount_entry.grid(row=1,column=1,padx=10,pady=10)

    amount_invalid_msg = tk.Label(mini, text="", fg="red")
    amount_invalid_msg.grid(row=2, column=1, padx=10, pady=0)

    ac_no=tk.Label(mini,text='Enter Acount Number :',font=("Arial",10))
    ac_no.grid(row=3,column=0,padx=10,pady=10)
    ac_no_var=tk.StringVar()
    ac_no_entry=tk.Entry(mini,width=30,textvariable=ac_no_var)
    ac_no_entry.grid(row=3,column=1,padx=10,pady=10)

    ac_no_invalid_msg = tk.Label(mini, text="", fg="red")
    ac_no_invalid_msg.grid(row=4, column=1, padx=10, pady=0)

    submit_invalid_msg=tk.Label(mini,text='',font=('',13,'bold'))
    submit_invalid_msg.grid(row=6,column=0,padx=10,pady=10,columnspan=3)
    
    entries = [amount_entry,ac_no_entry ]
    invalid_msg=[ amount_invalid_msg,ac_no_invalid_msg,submit_invalid_msg ]

    submit_btn=tk.Button(mini,text='SUBMIT',font=("Arial",10),command=lambda :deposit_valid(entries,Toplevel,amount_entry,ac_no_var,Message=invalid_msg),)
    submit_btn.grid(row=5,column=0,padx=10,pady=10,columnspan=2)

    
# Bind the Enter key event to move focus
    for entry in entries:
        entry.bind("<Return>", lambda event, entries=entries: focus_next_entry(event, entries, Toplevel, amount_var=amount_var,
                                                                               ac_no_var=ac_no_var,check='deposit',Msg=invalid_msg))
        entry.bind("<Down>", lambda event, entries=entries: Arrow_keys(event,entries))
        entry.bind("<Up>", lambda event, entries=entries: Arrow_keys(event,entries))

  
    mini.grab_set()# to freeze the buttons in main window untill close toplevel window
    mini.resizable(True,True)
    mini.mainloop()

#function for withdraw button
def withdraw_amount():
    
    mini = tk.Toplevel()
    mini.title("Withdraw Amount")
    Toplevel=mini

    tk.Label(mini, text='Fill the below Information for Withdraw:', font=("Arial", 15, 'bold')).grid(row=0,column=0,padx=10,pady=10,columnspan=2)
    
    tk.Label(mini, text="Enter Amount:", font=("Arial", 10)).grid(row=1, column=0, padx=10, pady=10)
    amount_var=tk.StringVar()
    amount_entry = tk.Entry(mini, width=30,textvariable=amount_var)
    amount_entry.grid(row=1, column=1, padx=10, pady=10)

    amount_invalid_msg = tk.Label(mini, text="", fg="red")
    amount_invalid_msg.grid(row=2, column=1, padx=10, pady=0)

    tk.Label(mini, text='Enter Signature:', font=("Arial", 10)).grid(row=3, column=0, padx=10, pady=10)
    sign_var=tk.StringVar()
    sign_entry = tk.Entry(mini, width=30,textvariable=sign_var)
    sign_entry.grid(row=3, column=1, padx=10, pady=10)

    sign_invalid_msg = tk.Label(mini, text="", fg="red")
    sign_invalid_msg.grid(row=4, column=1, padx=10, pady=0)

    tk.Label(mini, text='Enter Account Number:', font=("Arial", 10)).grid(row=5, column=0, padx=10, pady=10)
    ac_no_var=tk.StringVar()
    ac_no_entry = tk.Entry(mini, width=30,textvariable=ac_no_var)
    ac_no_entry.grid(row=5, column=1, padx=10, pady=10)

    ac_no_invalid_msg = tk.Label(mini, text="", fg="red")
    ac_no_invalid_msg.grid(row=6, column=1, padx=10, pady=0)

    entries = [ amount_entry, sign_entry, ac_no_entry ]
      
    type_of_ac=['Saving_A/C','Current_A/C','FD_A/C']

    # Create a StringVar to hold the value of the selected radiobutton
    selected_ac = tk.StringVar(value=-1)

    for i in range(len(type_of_ac)):
        # Create a Radiobutton for each account type
        tk.Radiobutton(mini, text=type_of_ac[i], variable=selected_ac, value=type_of_ac[i]
                       ,font=("Arial",12,)).grid(row=7, column=i)
    radio_invalid_msg = tk.Label(mini, text="", fg="red")
    radio_invalid_msg.grid(row=8, column=1, padx=10, pady=0)

    submit_invalid_msg=tk.Label(mini,text='',font=('',13,'bold'))
    submit_invalid_msg.grid(row=10,column=0,padx=10,pady=10,columnspan=3)

    invalid_msg=[ amount_invalid_msg, sign_invalid_msg, ac_no_invalid_msg, radio_invalid_msg, submit_invalid_msg]

# Bind the Enter key event to move focus
    for entry in entries:
        entry.bind("<Return>", lambda event, entries=entries: focus_next_entry(event, entries,Toplevel,amount_var=amount_var,
                                                                               ac_no_var=ac_no_var,sign_var=sign_var,check='credit',
                                                                               ac_type=selected_ac,Msg=invalid_msg))
        entry.bind("<Down>", lambda event, entries=entries: Arrow_keys(event,entries))
        entry.bind("<Up>", lambda event, entries=entries: Arrow_keys(event,entries))
                                            # withdraw_valid(entries,Toplevel,init_balance,ac_no_var,sign,AC_type,invalids)
    submit_btn = tk.Button(mini, text='SUBMIT', font=("Arial", 10), command=lambda:withdraw_valid(entries,Toplevel,amount_var,ac_no_var,sign_var,selected_ac.get(),invalid_msg))
    submit_btn.grid(row=9, column=0, padx=10, pady=10, columnspan=2)


    mini.grab_set()  # to freeze the buttons in the main window until the toplevel window is closed
    mini.mainloop()

#function for check button in main window
def check_account():

    click_limit =3
    click_count = [0]
    
    def validate():#to validate the entry box inputs

        ac_no=ac_no_entry.get()
        if not ac_no.isdigit():
            invalid_msg.config(text="Invalid input: Please enter a number.")
            return False
        else:
            invalid_msg.config(text="")  # Clear the message if input is valid
            
        if ac_no.isdigit():
            ac_no_entry.config(fg='black')
            #ac_no_entry.config(bg='light green') 
            submit_btn.config(state='normal',bg='light green')
            entries.append(submit_btn)
            #submit_btn.focus_set()
            submit_btn.bind("<Return>",Submit)
            submit_btn.bind("<Button-1>",Submit)

           
        else:
            ac_no_entry.config(fg='red')  
            submit_btn.config(state='disabled',bg='SystemButtonFace')
    def Submit(event):
        if len(click_count) >= click_limit:
            mini.destroy()
            msg.showwarning("Limit Reached", "You have reached the maximum number of submissions.")
                    
        click_count.append(1)
        account_no = ac_no_entry.get()
        if  not account_no  :
            msg.showerror("Error", "Account number is required.")
            return
        
        else:
            
            details=BankOperations.check(int(account_no))

            if details==0:
                mini.destroy()
              
            elif details==1:
                return
            else:
                close_toplevel(mini)
                msg.showinfo(title="Details",message=details)
                # mini.destroy()


    M=tk.Toplevel()
    mini=M
    tk.Label(mini,text='Fill the below Information for Check A/C details :',font=("Arial",15,'bold')).grid(row=0,column=0,padx=10,pady=10,columnspan=2)
    
    #to create lables and entry box
    ac_no=tk.Label(mini,text='Enter Acount Number :',font=("Arial",10))
    ac_no.grid(row=1,column=0,padx=10,pady=10)
    ac_no_var=tk.StringVar()
    ac_no_entry=tk.Entry(mini,width=30,textvariable=ac_no_var)
    ac_no_entry.grid(row=1,column=1,padx=10,pady=10)
    ac_no_entry.bind("<KeyRelease>",lambda event:validate())
    
    submit_btn=tk.Button(mini,text='SUBMIT',font=("Arial",10),command=Submit,state="disabled")
    submit_btn.grid(row=3,column=0,padx=10,pady=10,columnspan=2)

    invalid_msg = tk.Label(mini, text="", fg="red")
    invalid_msg.grid(row=2,column=0,padx=10,pady=10,columnspan=2)
    entries = [ ac_no_entry]

# Bind the Enter key event to move focus
    for entry in entries:
        entry.bind("<Return>", lambda event, entries=entries: focus_next_entry(event, entries))

    mini.grab_set()# to freeze the buttons in main window untill close toplevel window
    mini.resizable(True,True)
    mini.mainloop()

def remove_ac():

    def browse_file():
        file_path = filedialog.askopenfilename(title="Select File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if file_path:
            reason_var.set(file_path)
        

   
    mini=tk.Toplevel()
    mini.title("Remove Account")
    Toplevel=mini

    name=tk.Label(mini,text="Enter Name :",font=("Arial",10))
    name.grid(row=1,column=0,padx=10,pady=10)
    name_var=tk.StringVar()
    name_entry=tk.Entry(mini,textvariable=name_var,width=30)
    name_entry.grid(row=1,column=1,padx=10,pady=10)
    name_invalid_msg=tk.Label(mini)
    name_invalid_msg.grid(row=2,column=1)
    #name_entry.bind("<KeyRelease>", lambda event: validate_inputs())

    ac_no=tk.Label(mini, text="Enter Account Number",font=("Arial",10))
    ac_no.grid(row=3,column=0,padx=10,pady=10)
    ac_no_var=tk.StringVar()
    ac_no_Entry=tk.Entry(mini,width=30,textvariable=ac_no_var)
    ac_no_Entry.grid(row=3,column=1,padx=10,pady=10)
    
    ac_no_invalid_msg=tk.Label(mini)
    ac_no_invalid_msg.grid(row=4,column=1)
    
    sign=tk.Label(mini,text='Enter Signature :',font=("Arial",10))
    sign.grid(row=5,column=0,padx=10,pady=10)
    sign_var=tk.StringVar()
    sign_entry=tk.Entry(mini,textvariable=sign_var,width=30)
    sign_entry.grid(row=5,column=1,padx=10,pady=10)
   
    sign_invalid_msg=tk.Label(mini)
    sign_invalid_msg.grid(row=6,column=1)

    mobile=tk.Label(mini,text='Enter Mobile Number :',font=("Arial",10))
    mobile.grid(row=7,column=0,padx=10,pady=10)
    mobile_var = tk.StringVar()
    mobile_entry=tk.Entry(mini,width=30,textvariable=mobile_var)
    mobile_entry.grid(row=7,column=1,padx=10,pady=10)
 
    mobile_invalid_msg=tk.Label(mini)
    mobile_invalid_msg.grid(row=8,column=1)

    adhar=tk.Label(mini,text='Enter Adhar_Card Number :',font=("Arial",10))
    adhar.grid(row=9,column=0,padx=10,pady=10)
    adhar_var=tk.StringVar()
    adhar_entry=tk.Entry(mini,width=30,textvariable=adhar_var)
    adhar_entry.grid(row=9,column=1,padx=10,pady=10)
   
    adhar_invalid_msg=tk.Label(mini)
    adhar_invalid_msg.grid(row=10,column=1)


    # Replace Reason Entry with Browse Button
    reason_label = tk.Label(mini, text="Upload Reason File:", font=("Arial", 10))
    reason_label.grid(row=11, column=0, padx=10, pady=10)
    reason_var = tk.StringVar()
    reason_entry = tk.Entry(mini, textvariable=reason_var, width=30, state='readonly')
    reason_entry.grid(row=11, column=1, padx=10, pady=10)
    upload_btn = tk.Button(mini, text="Upload file", command=browse_file)
    upload_btn.grid(row=11, column=2, padx=10, pady=10)

    reason_invalid_msg = tk.Label(mini)
    reason_invalid_msg.grid(row=12, column=1)


    type_of_ac=['Saving_A/C','Current_A/C','FD_A/C']

    # Create a StringVar to hold the value of the selected radiobutton
    selected_ac = tk.StringVar(value=-1)

    
    for i in range(len(type_of_ac)):
        # Create a Radiobutton for each account type
        tk.Radiobutton(mini, text=type_of_ac[i], variable=selected_ac, value=type_of_ac[i]
                       ,font=("Arial",12,)).grid(row=13, column=i)
    radio_invalid_msg = tk.Label(mini)
    radio_invalid_msg.grid(row=14, column=1)

    submit_invalid_msg=tk.Label(mini,text='',font=('',13,'bold'))
    submit_invalid_msg.grid(row=17,column=0,padx=10,pady=10,columnspan=3)

    entries = [name_entry, ac_no_Entry, sign_entry, mobile_entry, adhar_entry,reason_entry]
    invalid_msg=[name_invalid_msg,ac_no_invalid_msg,sign_invalid_msg,mobile_invalid_msg,adhar_invalid_msg,
             radio_invalid_msg,submit_invalid_msg]

    submit_btn=tk.Button(mini,text='SUBMIT',font=("Arial",10),command=lambda : remove_valid(entries,Toplevel,mobile_entry,adhar_entry,
                     ac_no_var,name_entry,sign_entry,reason_entry,selected_ac.get(),invalid_msg))
    submit_btn.grid(row=15,column=0,padx=10,pady=10,columnspan=2)

    
# Bind the Enter key event to move focus
    for entry in entries:
        entry.bind("<Return>", lambda event, entries=entries: focus_next_entry(event,entries, Toplevel=Toplevel,mobile_var=mobile_var,adhar_var=adhar_var,
                                                                               ac_no_var=ac_no_var,name_var=name_var,sign_var=sign_var,
                                                                               check='remove_ac',Reason_var=reason_var,ac_type=selected_ac,Msg=invalid_msg ))
    
        entry.bind("<Down>", lambda event, entries=entries: Arrow_keys(event,entries))
        entry.bind("<Up>", lambda event, entries=entries: Arrow_keys(event,entries))

    mini.grab_set()# to freeze the buttons in main window untill close toplevel window
    mini.resizable(True,True)
    mini.mainloop()

def New_Update(ac_no_var=None, old_sign=None, new_sign=None, name=None, mobile_no=None, Entries=None, invalids=None,topleve=None):
    read = Read_csv()  # Read the CSV file to get the latest account information
        
    read = Read_csv()  # Read the CSV file to get account information
    ac = ac_no_var.get()  # Get the account number from the input field
    sign = old_sign.get()  # Get the old signature from the input field
    name = name.get()  # Get the name from the input field
    new_sign = new_sign.get()  # Get the new signature from the input field
    mobile_no = mobile_no.get()  # Get the mobile number from the input field
    Entries = Entries  # Get the list of entry fields
    invalids = invalids  # Get the list of invalid message labels
        
        # Check if the account number field is empty
    if ac == "" or sign=='':
        invalids[5].config(text="Please fill all the REQUIRED fileds",fg='red')
        return False      
    else:
        invalids[5].config(text="")

    if not ac.isdigit():
        Entries[0].focus_set()
        invalids[0].config(text="Account Number should be numeric",fg='red')
        return False
    else:
        invalids[0].config(text="  ")

        # Check if the account number exists in the CSV file
    
    if int(ac) not in read["A/C No:"].values:                           #entries = [ac_no_entry, sign_entry, name_entry, new_sign_entry, mobile_entry]
        Entries[0].focus_set() 
        msg.showerror("Error", "Account Number does not exist")
        return False
    index = read.index[read["A/C No:"] == int(ac)].tolist()[0]  # Find the index of the account number

        # Validate the old signature
    if read.at[index, "Sign:"] == sign:
        updated = False  # Track if any update is made
            
            # Update the name if provided and valid
        if name:
            if Validation.Name(name):
                invalids[2].config(text="")             
                read.at[index, "Names"] = name
                msg.showinfo("Information", f"Name Updated to {name}")
                updated = True
            else:
                invalids[2].config(text="Invalid Name", fg="red")
                Entries[2].focus_set()
                return False
                
            # Update the signature if provided and valid
        if new_sign:
            if Validation.Sign(new_sign):
                invalids[3].config(text="")
                read.at[index, "Sign:"] = new_sign
                msg.showinfo("Information", f"Signature Updated to {new_sign}")
                updated = True
            else:
                invalids[3].config(text="Invalid Signature", fg="red")
                Entries[3].focus_set()
                return False
                
            # Update the mobile number if provided and valid
        if mobile_no:
            if Validation.Mobile(mobile_no):
                invalids[4].config(text="")
                read.at[index, "Mobile_No:"] = mobile_no
                msg.showinfo("Information", f"Mobile Number Updated to {mobile_no}")
                updated = True
            else:
                invalids[4].config(text="Invalid Mobile Number", fg="red")
                Entries[4].focus_set()
                return False
                
            # Save changes to the CSV file if any updates were made
        if updated:
            read.to_csv(Acounts_file, index=False)
            close_toplevel(topleve)
        else:

            invalids[5].config(text="No changes were made!",fg="red")
            # invalids[2].config(text="Invalid Name", fg="red")
            # Entries[2].focus_set()
            # invalids[3].config(text="Invalid Signature", fg="red")
            # invalids[4].config(text="Invalid Mobile Number", fg="red")
            return
                
    else:
        invalids[1].config(text="Signature is not Valid!",fg='red')
        Entries[1].focus_set()


def edit_ac():
    # Create a secondary window using Toplevel
    mini = tk.Toplevel()
    mini.title("Edit Account")
    Toplevel=mini

    # Label and entry field for account number
    ac_no = tk.Label(mini, text="Enter Account Number (*REQUIRED)", font=("Arial", 10))
    ac_no.grid(row=0, column=0, padx=10, pady=5)
    ac_no_var = tk.StringVar()
    ac_no_entry = tk.Entry(mini, width=30, textvariable=ac_no_var)
    ac_no_entry.grid(row=0, column=1, padx=10, pady=5)

    ac_no_invalid_msg = tk.Label(mini)
    ac_no_invalid_msg.grid(row=1, column=1)

    # Old Signature
    sign = tk.Label(mini, text="Enter Old Signature (*REQUIRED)", font=("Arial", 10))
    sign.grid(row=2, column=0, padx=10, pady=5)
    sign_entry = tk.Entry(mini, width=30)
    sign_entry.grid(row=2, column=1, padx=10, pady=5)

    sign_invalid_msg = tk.Label(mini)
    sign_invalid_msg.grid(row=3, column=1)

    # New Name
    name = tk.Label(mini, text="Enter New Name (optional)", font=("Arial", 10))
    name.grid(row=4, column=0, padx=10, pady=5)
    name_entry = tk.Entry(mini, width=30)
    name_entry.grid(row=4, column=1, padx=10, pady=5)

    name_invalid = tk.Label(mini)
    name_invalid.grid(row=5, column=1)

    # New Signature
    new_sign = tk.Label(mini, text="Enter New Signature (optional)", font=("Arial", 10))
    new_sign.grid(row=6, column=0, padx=10, pady=5)
    new_sign_entry = tk.Entry(mini, width=30)
    new_sign_entry.grid(row=6, column=1, padx=10, pady=5)

    new_sign_invalid = tk.Label(mini)
    new_sign_invalid.grid(row=7, column=1)

    # New Mobile Number
    mobile = tk.Label(mini, text="Enter New Mobile Number (optional)", font=("Arial", 10))
    mobile.grid(row=8, column=0, padx=10, pady=5)
    mobile_entry = tk.Entry(mini, width=30)
    mobile_entry.grid(row=8, column=1, padx=10, pady=5)

    mobile_invalid = tk.Label(mini)
    mobile_invalid.grid(row=9, column=1)

    submit_invalid_msg=tk.Label(mini,text='',font=('',13,'bold'))
    submit_invalid_msg.grid(row=11,column=0,padx=10,pady=10,columnspan=3)

    # List of invalid message labels and entry fields for validation
    invalids_msg = [ac_no_invalid_msg, sign_invalid_msg, name_invalid, new_sign_invalid, mobile_invalid,submit_invalid_msg]
    entries = [ac_no_entry, sign_entry, name_entry, new_sign_entry, mobile_entry]

    # Bind keyboard events for navigating between entries
    for entry in (entries):
        entry.bind("<Return>", lambda event: focus_next_entry(event, entries,ac_no_var=ac_no_var,sign_var=sign_entry,
                                                              new_sign_var=new_sign_entry,name_var=name_entry,check='update',Msg=invalids_msg,Toplevel=Toplevel))
        entry.bind("<Up>", lambda event : Arrow_keys(event, entries,))
        entry.bind("<Down>", lambda event : Arrow_keys(event, entries,))

    # Submit button for updating account information
    submit_btn = tk.Button(mini, text="Submit", font=("Arial", 10),command=lambda : New_Update(ac_no_var,sign_entry,new_sign_entry,name_entry,mobile_entry,entries,invalids_msg,Toplevel))
    submit_btn.grid(row=10, column=0, pady=10, columnspan=2)

    mini.grab_set() 
    
    mini.mainloop()



def Acounts():
    Secret_key="1542"
    def load_csv():
        
        load_button.destroy()
        
    # Open the CSV file and read its content
        with open(Acounts_file) as file:
            read = csv.reader(file)
            headers = next(read)
           
        # Define the columns in the treeview
            tree["columns"] = headers
            tree["show"] = "headings"  # Hide the default empty first column
            max_col_widths = {header: len(header) for header in headers}
            for headdings in headers:
                tree.heading(headdings, text=headdings,anchor='nw',)
                
        # Create the headers in the treeview
            for row in read:
                for idx, value in enumerate(row):
                    col_width = max(max_col_widths[headers[idx]], len(value))
                    max_col_widths[headers[idx]] = col_width
                tree.insert("", "end", values=row)

            tree['height']=20
    def remove_secret_keys():
        """Function to remove the Secret_key label, entry field, invalid label, and button."""
        Secret_key.grid_remove()
        Secret_key_Entry.grid_remove()
        Secret_key_invalid.grid_remove()
        chk.grid_remove()

    def valid():
        Secret_key="1542"
        enter_key=(Secret_key_Entry.get())
        
        if Secret_key_Entry.get()=='':
            msg.showerror("Error", "Please enter the secret key!")
            Secret_key_Entry.focus_set()
            return
        
        if enter_key==Secret_key:
            remove_secret_keys()
            load_button.config(state='active',bg='light green')
        else:
            Secret_key_Entry.focus_set()
            load_button.config(state='disabled',bg='SystemButtonFace')
            Secret_key_invalid.config(text="Entered Key is Wrong!!")
        # Create the main Tkinter window
    mini = tk.Toplevel()
    mini.title("Acounts detaills")

    # Create a frame for the Treeview
    frame = tk.Frame(mini,height=300,width=300)
    frame.grid(row=0,column=0,sticky="nsew")

    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Arial', 15, 'bold'))  # Set font size and style
    # Create and configure the Treeview
    tree = ttk.Treeview(frame)
    tree.pack(padx=20, pady=20, fill="both", expand=True)

    Secret_key=tk.Label(mini,text='enter secret key:',font=('Arial',12,'bold'))
    Secret_key.grid(row=1,column=0)
    Secret_key_var = tk.StringVar()
    Secret_key_Entry = tk.Entry(mini, width=30, textvariable=Secret_key_var)
    Secret_key_Entry.grid(row=1,column=1)
    Secret_key_Entry.focus_set()
    Secret_key_Entry.bind("<Return>",lambda event : valid())
    Secret_key_invalid=tk.Label(mini,font=('Arial'),fg='red')
    Secret_key_invalid.grid(row=2,column=1)
    chk=tk.Button(mini,text='check',font=('Arial',13,'bold'),command=valid)
    chk.grid(row=1,column=2,padx=20,pady=20)

    # Create a button to load the specific CSV file
    load_button = tk.Button(mini, text="Click To Open File", command=load_csv,state='disabled',font=('Arial',13,'bold'))
    load_button.grid(row=3,column=0,padx=10,pady=10,columnspan=2)

    
    mini.resizable(True,True)
    mini.mainloop()

# for creat Bank Operation  main window
window = tk.Tk()

w=window.winfo_screenwidth()
h=window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))# to set the

window.title("Banking System")
icon=tk.PhotoImage(file='bakn1.png')
window.iconphoto(False,icon)

canvas=tk.Canvas(window,width=w,height=h)

img=Image.open('money1.jpg')
img=img.resize((w,h))
photo=ImageTk.PhotoImage(img)

wl=tk.PhotoImage(file="bank_26.png")

canvas.create_image(0,0,image=photo,anchor='nw')
wallpaper = tk.Label(window, i=wl)
wallpaper.place(x=0, y=0, relwidth=1, relheight=1)


ac_image=tk.PhotoImage(file='create_ac.png')
dbt_image=tk.PhotoImage(file='deposit.png')
chk_image=tk.PhotoImage(file='check1.png')

ac=Image.open('bank_26.png')
ac=img.resize((80,80))
photo1=ImageTk.PhotoImage(ac)

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

tk.Button(button_frame, text="Acounts check", command=Acounts,
           compound="left", font=("Arial", 12, 'bold'),
          activebackground='blue', bg='navy blue', fg='white',
          borderwidth=4, cursor="hand2",height=3,width=5).grid(row=1,column=0,sticky='ew')

# Add buttons to the frame
tk.Button(button_frame, text="Create Account", command=create_account,
           compound="left", font=("Arial", 12, 'bold'),
          activebackground='blue', bg='green', fg='white',
          borderwidth=4, cursor="hand2",height=3).grid(row=0, column=0, padx=5, pady=5, sticky='ew')

tk.Button(button_frame, text="Update Account", command=edit_ac,
          compound="left", font=("Arial", 12, 'bold'),
          activebackground='blue', bg='green', fg='white',
          borderwidth=4, cursor="hand2",height=3).grid(row=0, column=1, padx=5, pady=5, sticky='ew')

tk.Button(button_frame, text="Deposit", command=deposit_amount,
          compound="left", font=("Arial", 12, 'bold'),
          activebackground='blue', bg='#fc9342',
          borderwidth=4, cursor="hand2",height=3).grid(row=0, column=2, padx=5, pady=5, sticky='ew')

tk.Button(button_frame, text="Withdraw", command=withdraw_amount,
           compound="left", font=("Arial", 12, 'bold'),
          activebackground='blue', bg='#c842fc',
          borderwidth=4, cursor="hand2",height=3).grid(row=0, column=3, padx=5, pady=5, sticky='ew')

tk.Button(button_frame, text="Check A/C", command=check_account,
           compound="left", font=("Arial", 12, 'bold'),
          activebackground='blue', bg='light blue', 
          borderwidth=4, cursor="hand2",height=3).grid(row=0, column=4, padx=5, pady=5, sticky='ew')

tk.Button(button_frame, text="Remove A/C", command=remove_ac,compound="left",
           font=("Arial", 12, 'bold'),height=3,activebackground='red',bg='gray',
           borderwidth=4, cursor="hand2").grid(row=0, column=5, padx=5, pady=5, sticky='ew')

tk.Button(button_frame, text="Exit", bg='red', font=("Arial", 12, 'bold'),height=3,width=7, command=quit, cursor="hand2").grid(row=0, column=6, padx=5, pady=5, sticky='ew')
tk.Button(window,).grid(row=5,column=5, padx=5, pady=20)
tk.Button(window,).grid(row=5,column=6, padx=5, pady=20)

# Make the window resizable
window.resizable(True, True)

# Start the Tkinter event loop
window.mainloop()