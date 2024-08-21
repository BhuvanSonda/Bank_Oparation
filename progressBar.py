import tkinter as tk
from tkinter import messagebox as msg
from tkinter import ttk
import re
import threading
import time
import Validation  # Ensure this module is imported correctly
import BankOperations  # Ensure this module is imported correctly

def validate_inputs():
    # Your existing validate_inputs function code here
    pass

def create_account():
    # Function to create account and simulate long operation
    try:
        name = name_entry.get()
        init_balance = amount_entry.get()
        sign = sign_entry.get()
        mobile_no = mobile_entry.get()
        adhar_no = adhar_entry.get()

        # Call the validation functions (ensure they are defined)
        if not (name and init_balance and sign and mobile_no and adhar_no):
            msg.showerror("Error", "All fields are required.")
            return

        if not Validation.Mobile(mobile_no):
            msg.showerror("Error", "Invalid mobile number.")
            return

        if not Validation.Adhar(adhar_no):
            msg.showerror("Error", "Invalid Aadhar number.")
            return

        if not re.match("^[0-9]+$", init_balance):
            msg.showerror("Error", "Please enter a valid amount.")
            return

        # Simulate long-running task
        BankOperations.create(name, sign, int(init_balance), int(mobile_no), int(adhar_no))
        return True

    except Exception as e:
        msg.showerror("Error", f"An error occurred: {e}")
        return False

def run_long_task():
    # Function to run in a separate thread
    global progress_window

    # Update progress bar
    for i in range(101):
        progress_bar['value'] = i
        progress_window.update_idletasks()
        time.sleep(0.02)  # Simulate some work being done
    
    # Perform the actual account creation
    success = create_account()
    
    # Close the progress window
    progress_window.destroy()
    
    if success:
        msg.showinfo("Success", "Account created successfully.")
        mini.destroy()  # Close the child window if account creation was successful

def submit():
    # Open the progress window
    global progress_window, progress_bar

    progress_window = tk.Toplevel(root)
    progress_window.title("Creating Account")
    progress_window.geometry("300x100")

    tk.Label(progress_window, text="Creating account, please wait...", padx=10, pady=10).pack()

    progress_bar = ttk.Progressbar(progress_window, orient='horizontal', length=250, mode='determinate')
    progress_bar.pack(padx=10, pady=10)

    # Start the long-running task in a separate thread
    threading.Thread(target=run_long_task, daemon=True).start()

# Create the main window
root = tk.Tk()

# Create the child window
mini = tk.Toplevel(root)
mini.title("Create Account")

# Create labels and entry boxes
name = tk.Label(mini, text="Enter Name :", font=("Arial", 10))
name.grid(row=1, column=0, padx=10, pady=10)
name_entry = tk.Entry(mini, width=30)
name_entry.grid(row=1, column=1, padx=10, pady=10)

amount = tk.Label(mini, text="Enter Initial Amount :", font=("Arial", 10))
amount.grid(row=2, column=0, padx=10, pady=10)
amount_entry = tk.Entry(mini, width=30)
amount_entry.grid(row=2, column=1, padx=10, pady=10)

sign = tk.Label(mini, text='Enter Signature :', font=("Arial", 10))
sign.grid(row=3, column=0, padx=10, pady=10)
sign_entry = tk.Entry(mini, width=30)
sign_entry.grid(row=3, column=1, padx=10, pady=10)

mobile = tk.Label(mini, text='Enter Mobile Number :', font=("Arial", 10))
mobile.grid(row=4, column=0, padx=10, pady=10)
mobile_entry = tk.Entry(mini, width=30)
mobile_entry.grid(row=4, column=1, padx=10, pady=10)

adhar = tk.Label(mini, text='Enter Aadhar Number :', font=("Arial", 10))
adhar.grid(row=5, column=0, padx=10, pady=10)
adhar_entry = tk.Entry(mini, width=30)
adhar_entry.grid(row=5, column=1, padx=10, pady=10)

submit = tk.Button(mini, text='SUBMIT', font=("Arial", 10), command=submit, state="disabled")
submit.grid(row=6, column=0, padx=10, pady=10, columnspan=2)

# Bind key release events to validation function
for entry in [name_entry, amount_entry, sign_entry, mobile_entry, adhar_entry]:
    entry.bind("<KeyRelease>", lambda event: validate_inputs())

root.mainloop()
