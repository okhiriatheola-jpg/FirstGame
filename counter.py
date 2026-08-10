import tkinter as tk
root = tk.Tk()
root.title("Let's Count!")
count = 0
label = tk.Label(root, text=f"Count: {count}")
label.pack()
def function():
    global count
    if count < 10:
        count += 1
    if count == 10:
        label.config(text="MAX SCORE!")
        root.config(bg="green")
    else:
        label.config(text=f"Count: {count}") 
    root.title(f"Score: {count}")    
         
tk.Button(root, text="+1", command=function).pack()  
def function_sub():
    global count
    if count > 0:
        count -= 1
    if count == 0:
        label.config(text="START")
    else:        
        label.config(text=f"Count: {count}")
    root.title(f"Count: {count}")
tk.Button(root, text="-1", command=function_sub).pack()
def function_reset():
    global count
    count = 0
    label.config(text="START")
    root.title("Let's Count")
    root.config(bg="SystemButtonFace") 

tk.Button(root, text="reset", command=function_reset).pack()

root.mainloop()
