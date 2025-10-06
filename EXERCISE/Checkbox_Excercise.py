import tkinter as tk
from tkinter import ttk

# Create the Tkinter Window and set its title and size
window = tk.Tk()
window.title('Tkinter Checkbutton Widget')
window.geometry('400x400')

# Function to update label based on Checkbutton state
def update_label():
    if bool_var.get():
        output_label.config(text="I AM VERY HAPPY FOR YOU!")
    else:
        output_label.config(text="I AM SORRY, BETTER DAYS ARE AHEAD!")

# Create the Checkbutton widget
bool_var = tk.BooleanVar()
Boolean_checkbutton = ttk.Checkbutton(
    window,
    variable=bool_var,
    text='Are you happy?',
    onvalue=True,
    offvalue=False,
    command=update_label
)

# Create the Label widget
output_label = ttk.Label(window, text="")

# Pack the widgets
Boolean_checkbutton.pack(pady=10)
output_label.pack(pady=10)

# Run the main Tkinter event loop
window.mainloop()


