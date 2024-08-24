import tkinter as tk

def edit():
    # Create a secondary window using Toplevel
    mini = tk.Tk()
    mini.title("Edit Account")

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

    # List of invalid message labels and entry fields for validation
    invalids_msg = [ac_no_invalid_msg, sign_invalid_msg, name_invalid, new_sign_invalid, mobile_invalid]
    entries = [ac_no_entry, sign_entry, name_entry, new_sign_entry, mobile_entry]

    # Bind keyboard events for navigating between entries
    for i, entry in enumerate(entries):
        entry.bind("<Return>", lambda event, idx=i: focus_next_entry(event, entries, idx))
        entry.bind("<Up>", lambda event, idx=i: arrow_keys(event, entries, idx, "Up"))
        entry.bind("<Down>", lambda event, idx=i: arrow_keys(event, entries, idx, "Down"))

    # Submit button for updating account information
    submit_btn = tk.Button(mini, text="Submit", font=("Arial", 10))
    submit_btn.grid(row=10, column=0, pady=10, columnspan=2)

    mini.grab_set()  # Make the Toplevel modal
    mini.resizable(True, True)
    mini.mainloop()

def focus_next_entry(event, entries, idx):
    next_idx = (idx + 1) % len(entries)
    entries[next_idx].focus_set()

def arrow_keys(event, entries, idx, direction):
    if direction == "Up":
        prev_idx = (idx - 1) % len(entries)
        entries[prev_idx].focus_set()
    elif direction == "Down":
        next_idx = (idx + 1) % len(entries)
        entries[next_idx].focus_set()

edit()
