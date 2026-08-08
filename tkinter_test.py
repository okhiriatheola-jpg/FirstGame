import tkinter as tk
root = tk.Tk()
root.title("Test")
tk.Label(root, text="Hello, Tkinter!").config(font=("Arial", 16)).pack(pady=10)
def button_clicked():
    print("Button clicked!")

tk.Button(root, text="Click me!", command=button_clicked).pack()
entry_box = tk.Entry(root)
entry_box.pack()
name = entry_box.get()

root.mainloop()
