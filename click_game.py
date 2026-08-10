import tkinter as tk
root=tk.Tk()
root.title("Clicker game")
score=0

label=tk.Label(text=f"Score: {score}")
label.pack()

def function_add():
    global score
    if score < 10:
        score += 1
        label.config(text=f"Score: {score}")

    if score == 10: 
        label.config(text=("YOU WIN!"))
        root.config(bg="green")
    root.title(f"Score: {score}")

button=tk.Button(text="+1", command=function_add).pack()

def function_reset():
    global score
    score = 0
    root.title(f"Score: {score}")
    label.config(text=f"Score: {score}")
    root.config(bg="SystemButtonFace")

button=tk.Button(text="reset", command=function_reset).pack()
root.mainloop()