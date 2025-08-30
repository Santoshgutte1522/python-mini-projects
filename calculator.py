import tkinter as tk

import tkinter as tk

# Function to update the entry field
def click(event):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(event.widget["text"]))

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the entry
def clear():
    entry.delete(0, tk.END)

# Window setup
window = tk.Tk()
window.title("Attractive Calculator")
window.geometry("300x400")
window.configure(bg="#222831")

# Entry field
entry = tk.Entry(window, font=("Arial", 20), bd=8, insertwidth=2, width=14, borderwidth=4,
relief="ridge", justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Button text layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

# Create buttons dynamically
for i in range(4):
    for j in range(4):
        btn_text = buttons[i][j]
        btn = tk.Button(window, text=btn_text, padx=20, pady=20, font=("Arial", 14),
        bg="#00ADB5", fg="white", bd=0)
        btn.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
        if btn_text == "=":
            btn.config(command=calculate)
        else:
            btn.bind("<Button-1>", click)

# Clear Button
clear_btn = tk.Button(window, text="C", padx=20, pady=20, font=("Arial", 14), bg="#FF5722",
fg="white", bd=0, command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Make columns and rows resize with window
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

for i in range(6):
    window.grid_rowconfigure(i, weight=1)

window.mainloop()