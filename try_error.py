def withdraw_valid(entries,amount_var=None):
    global a
    a=1
    # amt=amount_var.get()

    # if not Validation.Amount(amt):
    #     a = 0
    #     msg.showerror("Error", "Invalid amount.")
    #     entries[0].focus_set()
    #     return
    if a == 1:
        entries[3].config(state='normal')
        entries[3].config(bg="light green")
            
    else:
        entries[4].config(state='disabled')
entries=[12]
amount_var=12    
withdraw_valid(entries,amount_var)