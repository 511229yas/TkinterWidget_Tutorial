import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('SIMPLE GRADING SYSTEM')
window.geometry('400x400')

string_var = tk.StringVar()
Text_entry = ttk.Entry(master = window, textvariable = string_var, font = 'Calibri 24 bold')

Text_entry.pack();
