import tkinter as tk

def open_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")

    # Set the grab to restrict focus
    new_window.grab_set()

    # Add a button to minimize the window
    minimize_button = tk.Button(new_window, text="Minimize", command=new_window.iconify)
    minimize_button.pack(pady=20)

root = tk.Tk()
root.title("Main Window")

open_button = tk.Button(root, text="Open Window", command=open_window)
open_button.pack(pady=20)

root.mainloop()
