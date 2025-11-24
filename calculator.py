import tkinter as tk
import math
from tkinter import messagebox

# Global variable to store the current expression string
expression = ""

def press(num):
    """Updates the expression when a button (number or operator) is pressed."""
    global expression
    expression += str(num)
    equation.set(expression)

def scientific_func(func):
    """Performs scientific calculations."""
    global expression
    try:
        value = eval(expression)
        result = 0.0

        if func == "sqrt":
            result = math.sqrt(value)
        elif func == "sin":
            result = math.sin(math.radians(value)) 
        elif func == "cos":
            result = math.cos(math.radians(value))
        elif func == "log10":
            result = math.log10(value)
        
        expression = str(result)
        equation.set(expression)

    except Exception:
        messagebox.showerror("Error", "Invalid operation or domain error.")
        expression = ""
        equation.set("")

def equalpress():
    """Calculates the final result."""
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total 
    except Exception:
        messagebox.showerror("Error", "Invalid Expression")
        expression = ""
        equation.set("")

def clear():
    """Clears the entire expression."""
    global expression
    expression = ""
    equation.set("")

# --- GUI Setup ---

if __name__ == "__main__":
    gui = tk.Tk()
    gui.configure(background="#2C3E50") # Dark background
    gui.title("Sci-Calc")
    gui.geometry("380x300") 
    gui.resizable(0, 0)

    equation = tk.StringVar()

    # Display Field
    expression_field = tk.Entry(
        gui, 
        textvariable=equation, 
        font=('Arial', 20, 'bold'), 
        justify='right',
        bg='#ECF0F1', 
        fg='#2C3E50', 
        bd=0,
        relief=tk.FLAT
    )
    expression_field.grid(row=0, columnspan=5, ipadx=8, ipady=8, padx=5, pady=5, sticky='nsew')
    
    # 

    # Button Data: (text, row, column, command, color)
    buttons_data = [
        ('7', 1, 0, lambda: press(7), '#34495E'), ('8', 1, 1, lambda: press(8), '#34495E'), ('9', 1, 2, lambda: press(9), '#34495E'), ('/', 1, 3, lambda: press('/'), '#F39C12'), ('sqrt', 1, 4, lambda: scientific_func("sqrt"), '#1ABC9C'),
        
        ('4', 2, 0, lambda: press(4), '#34495E'), ('5', 2, 1, lambda: press(5), '#34495E'), ('6', 2, 2, lambda: press(6), '#34495E'), ('*', 2, 3, lambda: press('*'), '#F39C12'), ('sin', 2, 4, lambda: scientific_func("sin"), '#1ABC9C'),
        
        ('1', 3, 0, lambda: press(1), '#34495E'), ('2', 3, 1, lambda: press(2), '#34495E'), ('3', 3, 2, lambda: press(3), '#34495E'), ('-', 3, 3, lambda: press('-'), '#F39C12'), ('cos', 3, 4, lambda: scientific_func("cos"), '#1ABC9C'),
        
        ('0', 4, 0, lambda: press(0), '#34495E'), ('.', 4, 1, lambda: press('.'), '#34495E'), ('=', 4, 2, equalpress, '#2ECC71'), ('+', 4, 3, lambda: press('+'), '#F39C12'), ('log10', 4, 4, lambda: scientific_func("log10"), '#1ABC9C'),

        ('Clear', 5, 0, clear, '#E74C3C')
    ]

    # Create and place the buttons
    for (text, r, c, cmd, bg_color) in buttons_data:
        tk.Button(
            gui, 
            text=text, 
            command=cmd, 
            font=('Arial', 11, 'bold'),
            bg=bg_color, 
            fg='white',
            height=2, 
            width=7,
            bd=0
        ).grid(row=r, column=c, padx=3, pady=3, sticky='nsew')

    gui.mainloop()
