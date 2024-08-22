# import tkinter as tk
# from tkinter import filedialog, messagebox

# def remove_ac():

#     def validate_inputs():
#         # Get values from entry widgets
#         mobile_number = mobile_entry.get()
#         adhar_number = adhar_entry.get()
#         name_value = name_entry.get()
#         sign_value = sign_entry.get()
#         ac_no=ac_no_Entry.get()
#         reason_file = reason_var.get()

#         all_valid = True

#         # Validate Account Number
#         if ac_no.isdigit():
#             ac_no_Entry.config(fg='black')          
#         else:
#             ac_no_Entry.config(fg='red')
#             all_valid = False

#         # Validate mobile number 
#         if mobile_number.isdigit():
#             mobile_entry.config(fg='black')          
#         else:
#             mobile_entry.config(fg='red')
#             all_valid = False

#         # Validate Aadhar number (should be exactly 12 digits)
#         if adhar_number.isdigit():
#             adhar_entry.config(fg='black')         
#         else:
#             adhar_entry.config(fg='red')
#             all_valid = False

#         # Check if all fields are filled
#         if not (name_value and ac_no and sign_value and mobile_number and adhar_number and reason_file):
#             submit_btn.config(state='disabled')
#             return False

#         if all_valid:
#             submit_btn.config(bg='light green') 
#             # submit_btn.bind("<Return>",Submit)
#             # submit_btn.bind("<Button-1>",Submit)
#         else:
#             submit_btn.config(state='disabled') 
#             submit_btn.config(bg='SystemButtonFace') 
#             return False

#     def browse_file():
#         file_path = filedialog.askopenfilename(title="Select File", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
#         if file_path:
#             reason_var.set(file_path)
#             validate_inputs()  # Re-validate inputs after selecting a file

#     mini=tk.Toplevel()
#     mini.title("Remove Account")
#     Toplevel=mini

#     # Name Entry
#     name=tk.Label(mini,text="Enter Name :",font=("Arial",10))
#     name.grid(row=1,column=0,padx=10,pady=10)
#     name_var=tk.StringVar()
#     name_entry=tk.Entry(mini,textvariable=name_var,width=30)
#     name_entry.grid(row=1,column=1,padx=10,pady=10)

#     # Account Number Entry
#     ac_no=tk.Label(mini, text="Enter Account Number",font=("Arial",10))
#     ac_no.grid(row=3,column=0,padx=10,pady=10)
#     ac_no_var=tk.StringVar()
#     ac_no_Entry=tk.Entry(mini,width=30,textvariable=ac_no_var)
#     ac_no_Entry.grid(row=3,column=1,padx=10,pady=10)

#     # Signature Entry
#     sign=tk.Label(mini,text='Enter Signature :',font=("Arial",10))
#     sign.grid(row=5,column=0,padx=10,pady=10)
#     sign_var=tk.StringVar()
#     sign_entry=tk.Entry(mini,textvariable=sign_var,width=30)
#     sign_entry.grid(row=5,column=1,padx=10,pady=10)

#     # Mobile Number Entry
#     mobile=tk.Label(mini,text='Enter Mobile Number :',font=("Arial",10))
#     mobile.grid(row=7,column=0,padx=10,pady=10)
#     mobile_var = tk.StringVar()
#     mobile_entry=tk.Entry(mini,width=30,textvariable=mobile_var)
#     mobile_entry.grid(row=7,column=1,padx=10,pady=10)

#     # Aadhar Number Entry
#     adhar=tk.Label(mini,text='Enter Adhar_Card Number :',font=("Arial",10))
#     adhar.grid(row=9,column=0,padx=10,pady=10)
#     adhar_var=tk.StringVar()
#     adhar_entry=tk.Entry(mini,width=30,textvariable=adhar_var)
#     adhar_entry.grid(row=9,column=1,padx=10,pady=10)

#     # Replace Reason Entry with Browse Button
#     reason_label = tk.Label(mini, text="Upload Reason File:", font=("Arial", 10))
#     reason_label.grid(row=11, column=0, padx=10, pady=10)
#     reason_var = tk.StringVar()
#     reason_entry = tk.Entry(mini, textvariable=reason_var, width=30, state='readonly')
#     reason_entry.grid(row=11, column=1, padx=10, pady=10)
#     browse_btn = tk.Button(mini, text="Browse", command=browse_file)
#     browse_btn.grid(row=11, column=2, padx=10, pady=10)

#     # Radio Buttons for Account Type
#     type_of_ac=['Saving_A/C','Current_A/C','FD_A/C']
#     selected_ac = tk.StringVar(value=-1)
#     for i in range(len(type_of_ac)):
#         tk.Radiobutton(mini, text=type_of_ac[i], variable=selected_ac, value=type_of_ac[i], font=("Arial",12)).grid(row=13, column=i)

#     # Submit Button
#     submit_btn=tk.Button(mini,text='SUBMIT',font=("Arial",10),command=Submit,state="disabled")
#     submit_btn.grid(row=14,column=0,padx=10,pady=10,columnspan=2)

#     entries = [name_entry, ac_no_Entry, sign_entry, mobile_entry, adhar_entry, reason_entry]
    
#     for entry in entries:
#         entry.bind("<Return>", lambda event, entries=entries: focus_next_entry(event,entries, Toplevel=Toplevel,mobile_var=mobile_var,adhar_var=adhar_var,
#                                                                                ac_no_var=ac_no_var,name_var=name_var,sign_var=sign_var,
#                                                                                check='remove_ac',Reason_var=reason_var,ac_type=selected_ac ))
    
#         entry.bind("<Down>", lambda event, entries=entries: Arrow_keys(event,entries))
#         entry.bind("<Up>", lambda event, entries=entries: Arrow_keys(event,entries))

#     mini.grab_set()
#     mini.resizable(True,True)
#     mini.mainloop()
# remove_ac()