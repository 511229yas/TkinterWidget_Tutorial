import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Tkinter Spinbox Widget')
window.geometry('400x400')


def update_number_label(*args):
    number_label.config(text=f"Current number: {int_var.get()}")


int_var = tk.DoubleVar()
int_var.trace_add("write", update_number_label)  # Detects when the value changes
Number_spinbox = ttk.Spinbox(
    window, from_=0, to=100, increment=0.01,
    textvariable=int_var, font=('Calibri 21 bold')
)
Number_spinbox.pack(pady=10)

# Label to show numeric Spinbox value
number_label = ttk.Label(window, text="Current number: 0")
number_label.pack(pady=5)




def update_subject_label(*args):
    subject_label.config(text=f"Selected subject: {subject_var.get()}")

# Subject Spinbox with list of options
subjects = ['Maths', 'English', 'Science', 'Computing', 'Latin', 'Arabic', 'Social Studies', 'Sports Science']
subject_var = tk.StringVar()
subject_var.trace_add("write", update_subject_label)
Subject_spinbox = ttk.Spinbox(window, values=subjects, textvariable=subject_var, font=('Calibri 16'))
Subject_spinbox.pack(pady=10)


subject_label = ttk.Label(window, text="Selected subject: None")
subject_label.pack(pady=5)



window.mainloop()


