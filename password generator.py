import tkinter as tk
import random
import string

# to return 
def create_password(length):
    char = string.ascii_letters + string.digits + string.punctuation
    
    password = ""
    for i in range(length):
        password = password + random.choice(char)
    
    return password   

# to generate 
def generate_password():
    try:
        length = int(entry.get())
    except:
        result_label.config(text="Enter valid number")
        return

    password = create_password(length)   
    result_label.config(text=password)

# to copy 
def copy_password():
    password = result_label.cget("text")
    
    if password == "":
        result_label.config(text="Nothing to copy")
        return
    
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()   

    result_label.config(text="Password copied!")

# window
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x300")

# title
title = tk.Label(root, text="Password Generator", font=("Times New Roman", 16))
title.pack(pady=10)

# label
prompt_label = tk.Label(root, text="Enter password length:")
prompt_label.pack(pady=5)

# input box
entry = tk.Entry(root, width=20)
entry.pack(pady=10)

# for button
btn_generate = tk.Button(root, text="Generate", command=generate_password)
btn_generate.pack(pady=5)

# result
result_label = tk.Label(root, text="", wraplength=300)
result_label.pack(pady=10)

# copy button
btn_copy = tk.Button(root, text="Copy Password", command=copy_password)
btn_copy.pack(pady=5)

# to run 
root.mainloop()
