import tkinter as tk

def login():
    username = user_entry.get()
    password = pass_entry.get()
    if username == "admin" and password == ("1522"):
        result_label.config(text="Login Successful")
    else:
        result_label.config(text="Login Failed")

window = tk.Tk()
window.title("Login Form")

# user name

tk.Label(window,text="Username").grid(row=0, column=0)
user_entry = tk.Entry(window)
user_entry.grid(row=0, column=1)

# password
tk.Label(window,text="Password").grid(row=1, column=0)
pass_entry = tk.Entry(window,show="*")
pass_entry.grid(row=1, column=1)

# Button

tk.Button(window,text="Login",command=login).grid(row=2, columnspan=2)

# result
result_label = tk.Label(window)
result_label.grid(row=3, columnspan=2)

window.mainloop()