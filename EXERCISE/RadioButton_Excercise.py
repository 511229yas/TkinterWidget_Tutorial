import tkinter as tk
from tkinter import ttk

# Create the Tkinter Window and set its title and size
window = tk.Tk()
window.title('Tkinter Radiobutton Widget')
window.geometry('400x400')

# Function to update the label based on selected Radiobutton
def update_label():
    selected_value = int_var.get()
    if selected_value == 1:
        output_label.config(text="You selected: This is One")
    elif selected_value == 2:
        output_label.config(text="You selected: This is Two")
    else:
        output_label.config(text="Select an option above")

# Create a Frame to hold the Radiobuttons
radiobutton_frame = tk.Frame(window)

# Create IntVar to hold the selected value
int_var = tk.IntVar(value=0)  # default to 0 (none selected)

# Create Radiobutton widgets and attach the update function
Int_radiobutton_1 = ttk.Radiobutton(
    radiobutton_frame, value=1, variable=int_var, text='This is One', command=update_label
)
Int_radiobutton_2 = ttk.Radiobutton(
    radiobutton_frame, value=2, variable=int_var, text='This is Two', command=update_label
)

# Create a Label to display the output
output_label = ttk.Label(window, text='Select an option above')

# Pack elements into the window
radiobutton_frame.pack(pady=10)
Int_radiobutton_1.pack(anchor="w")
Int_radiobutton_2.pack(anchor="w")
output_label.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()

