import tkinter as tk
root = tk.Tk()
root.title("Test")
tk.Label(root, text="Hello, Tkinter!").pack()
def button_clicked():
    print("Button clicked!")

tk.Button(root, text="Click me!", command=button_clicked).pack()
name = entry_box.get()
root.mainloop()
