import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x500")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Function to add text to entry
def click_button(value):
    entry.insert(tk.END, value)

# Function to clear entry
def clear():
    entry.delete(0, tk.END)

# Function to evaluate expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Create buttons dynamically
for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(expand=True, fill="both")
    
    for button in row:
        btn = tk.Button(
            row_frame,
            text=button,
            font=("Arial", 18),
            relief=tk.RAISED,
            bd=5,
            command=lambda b=button: 
                clear() if b == 'C' else
                calculate() if b == '=' else
                click_button(b)
        )
        btn.pack(side="left", expand=True, fill="both")

# Run application
root.mainloop()
