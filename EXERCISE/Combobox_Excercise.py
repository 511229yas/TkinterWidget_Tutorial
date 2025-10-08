import tkinter as tk
from tkinter import ttk

# Initialize window
window = tk.Tk()
window.title('Tkinter Combobox Widget')
window.geometry('400x400')

# StringVar for Combobox
string_var = tk.StringVar()

# Label that will be updated
label = tk.Label(window, text="Select an option from the Combobox.")
label.pack()

# Function to update label
def update_label(event):
    selected = myCombobox.get()
    label.config(text=f"You selected: {selected}")

# Function triggered before dropdown opens
def on_postcommand():
    print("Dropdown opened!")

# Create Combobox
myCombobox = ttk.Combobox(
    master=window,
    textvariable=string_var,
    values=['This Option', 'That Option', 'Another Option'],
    postcommand=on_postcommand
)

# Bind selection event
myCombobox.bind("<<ComboboxSelected>>", update_label)

# Display the Combobox
myCombobox.pack()

# Run the main event loop
window.mainloop()

