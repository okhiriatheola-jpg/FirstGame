import tkinter as tk
root = tk.Tk()
root.title("Test")

label = tk.Label(root, text="Hello, Tkinter!")
label.config(font=("Arial", 16))
label.pack(pady=10)

def button_clicked():
    name = entry_box.get()
    label.config(text=f"Hello, {name}!")

    if entry_box.get() == "":
        label.config(text="Please enter your name.")
    else:
        label.config(text=f"Hello, {name}!")    

tk.Button(root, text="Click me!", command=button_clicked).pack()
entry_box = tk.Entry(root)
entry_box.pack()



root.mainloop()
