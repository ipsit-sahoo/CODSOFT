import tkinter as tk
from tkinter import messagebox
import json
import os

file_name = "tasks.json"

# TO Load tasks
def load_tasks():
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return []

# To Save tasks
def save_tasks():
    with open(file_name, "w") as file:
        json.dump(tasks, file)

# To Update Listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔" if task["done"] else "✘"
        listbox.insert(tk.END, f"{task['title']} [{status}]")

# To Add Task
def add_task():
    task = entry.get()
    if task == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return
    tasks.append({"title": task, "done": False})
    entry.delete(0, tk.END)
    save_tasks()
    update_listbox()

# Delete Task
def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        save_tasks()
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Select a task!")

# To Mark as Done
def mark_done():
    try:
        selected = listbox.curselection()[0]
        tasks[selected]["done"] = True
        save_tasks()
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Select a task!")

# For Main Window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x450")

tasks = load_tasks()

# Title
title = tk.Label(root, text="To-Do List", font=("Times New Roman", 18))
title.pack(pady=10)

# Entry box
entry = tk.Entry(root, width=30, font=("Times New Roman", 12))
entry.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

add_btn = tk.Button(btn_frame, text="Add Task", width=12, command=add_task)
add_btn.grid(row=0, column=0, padx=5)

done_btn = tk.Button(btn_frame, text="Mark Done", width=12, command=mark_done)
done_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete Task", width=12, command=delete_task)
delete_btn.grid(row=0, column=2, padx=5)

# Listbox
listbox = tk.Listbox(root, width=45, height=15, font=("Times New Roman", 11))
listbox.pack(pady=10)

update_listbox()

root.mainloop()
