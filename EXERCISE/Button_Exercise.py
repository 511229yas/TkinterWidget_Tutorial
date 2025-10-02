import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('SIMPLE GRADING SYSTEM')
window.geometry('400x400')  

output_string = tk.StringVar()
output_label = ttk.Label(master=window, textvariable=output_string)

# Define the button command functions
def get_button1_text():
    output_string.set("You submitted a response.")

# Buttons
button_1 = ttk.Button(master=window, text='SUBMIT', command=get_button1_text)
