import tkinter as tk
root = tk.Tk()
root.title("entry_stringvar Test")
name = tk.StringVar()
entry = tk.Entry(root, textvariable=name).pack()
def show_name():
    if name.get() == "":
        label.config(text="Please enter your name.")
    else:
        label.config(text=f"Hello, {name.get()}!")    
label = tk.Label(root, text="Hello!")
label.pack()    
button = tk.Button(root, text="your name", command=show_name)
button.pack()
root.mainloop()