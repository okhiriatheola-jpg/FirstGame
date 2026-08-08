import tkinter as tk
root = tk.Tk()
root.title("StringVar Test")
text = tk.StringVar(value="Hello!")
text.set("Hello, Tkinter!")
label = tk.Label(root, textvariable=text)
label.pack(pady=10)
button = tk.Button(root, text="Click me!", command=lambda: text.set("You clicked the button!"))
button.pack(pady=10)

root.mainloop()