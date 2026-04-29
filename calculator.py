import tkinter as tk

# main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x300")

# Entry 
entry = tk.Entry(root, width=22, font=("Times New Roman", 18), bd=5, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

# to add value to entry
def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

# to clear entry
def clear():
    entry.delete(0, tk.END)

# to calculate result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3)
]

# Create buttons
for (text, row, col) in buttons:
    if text == 'C':
        tk.Button(root, text=text, width=5, height=2, command=clear).grid(row=row, column=col)
    elif text == '=':
        tk.Button(root, text=text, width=5, height=2, command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=5, height=2,
                  command=lambda t=text: click(t)).grid(row=row, column=col)

# Run app
root.mainloop()
