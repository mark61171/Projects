# import tkinter

import tkinter as tk

# Function to handle button clicks
def button_click(char):
    # Get the current expression in the entry box and append the clicked character
    current = entry.get()
    entry.delete(0, tk.END)  # Clear the entry box
    entry.insert(0, current + char)  # Insert the new expression

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())  # Evaluate the expression
        entry.delete(0, tk.END)  # Clear the entry box
        entry.insert(0, str(result))  # Display the result
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")  # In case of invalid input

# Function to clear the entry box
def clear():
    entry.delete(0, tk.END)  # Clear the entry box

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Set window size
window.geometry("400x600")

# Entry widget to display the current input and result
entry = tk.Entry(window, width=16, font=('Arial', 24), borderwidth=5, relief='solid', justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Buttons for digits and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and place the buttons on the window
row, col = 1, 0
for button in buttons:
    if button == "=":
        tk.Button(window, text=button, width=5, height=2, font=('Arial', 18),
                  command=calculate).grid(row=row, column=col)
    else:
        tk.Button(window, text=button, width=5, height=2, font=('Arial', 18),
                  command=lambda b=button: button_click(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
clear_button = tk.Button(window, text="C", width=5, height=2, font=('Arial', 18), command=clear)
clear_button.grid(row=row, column=0)

# Start the GUI loop
window.mainloop()
