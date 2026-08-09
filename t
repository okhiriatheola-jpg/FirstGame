
import tkinter as tk
root = tk.Tk()
root.title("Let's Count!")
count = 0
label = tk.Label(root, text=f"Count: {count}")
label.pack()
def function():
    global count
    count += 1
    label.config(text=f"Count: {count}")
tk.Button(root, text="+1", command=function).pack()  
def function_sub():
    global count
    count -= 1
    label.config(text=f"Count: {count}")
tk.Button(root, text="-1", command=function_sub).pack()
def function_reset():
    global count
    count = 0
    label.config(text=f"Count: {count}")
if count < 10
    count += 1
else:



root.mainloop()
