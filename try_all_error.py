# def load_csv(Secret_key_Entry,button,invalid,tree):
#         Secret_key="1542"
#         if Secret_key_Entry.get()=='':
#             invalid.config(text= "Please enter the secret key!",fg='red')
#             Secret_key_Entry.focus_set()
#             return
        
#         if enter_key!=Secret_key:
#             Secret_key_Entry.focus_set()
#             button[1].config(state='disabled',bg='SystemButtonFace')
#             invalid.config(text="Entered Key is Wrong!!")
#             return False

#         else:
#             Secret_key.grid_remove()
#             Secret_key_Entry.grid_remove()
#             invalid.grid_remove()
#             button[0].grid_remove()
#             button[1].config(state='active',bg='light green')
           
#             data=tree
#     # Open the CSV file and read its content
#             with open(Acounts_file) as file:
#                 read = csv.reader(file)
#                 headers = next(read)
           
#         # Define the columns in the treeview
#                 data["columns"] = headers
#                 data["show"] = "headings"  # Hide the default empty first column
#                 max_col_widths = {header: len(header) for header in headers}
#                 for headdings in headers:
#                     data.heading(headdings, text=headdings,anchor='nw',)
                
#         # Create the headers in the treeview
#                 for row in read:
#                     for idx, value in enumerate(row):
#                         col_width = max(max_col_widths[headers[idx]], len(value))
#                         max_col_widths[headers[idx]] = col_width
#                     data.insert("", "end", values=row)

#                 data['height']=20


    

# Secret_key="1542"
#         enter_key=(Secret_key_Entry.get())
        
#         if Secret_key_Entry.get()=='':
#             msg.showerror("Error", "Please enter the secret key!")
#             Secret_key_Entry.focus_set()
#             return
        
#         if enter_key==Secret_key:
#             remove_secret_keys()
#             load_button.config(state='active',bg='light green')
#         else:
#             Secret_key_Entry.focus_set()
#             load_button.config(state='disabled',bg='SystemButtonFace')
#             Secret_key_invalid.config(text="Entered Key is Wrong!!")