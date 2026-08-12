import tkinter as tk
root = tk.Tk()
root.title("Dodge The Enemy")

canvas = tk.Canvas(width=500, height=400)
canvas.pack()

player = canvas.create_rectangle(235, 185, 265, 215, fill="light blue")

enemy = canvas.create_rectangle(430, 50, 460, 80, fill="pink")

def move_player(event):
	if event.keysym == "Left":
		canvas.move(player, -10, 0)
	elif event.keysym == "Right":
		canvas.move(player, +10, 0)
	elif event.keysym == "Up":
		canvas.move(player, 0, -10)
	elif event.keysym == "Down":
		canvas.move(player, 0, +10)	
	player_coords = canvas.coords(player)

	if player_coords[0] < 0:
		 canvas.move(player, +10, 0)
	if player_coords[2] > 500:
		canvas.move(player, -10, 0)
	if player_coords[1] < 0:
		canvas.move(player, 0, +10)
	if player_coords[3] > 400:
		canvas.move(player, 0, -10)	 
def move_enemy():
	canvas.move(enemy, -10, 0)

canvas.bind("<KeyPress>", move_player)
canvas.focus_set()

root.mainloop()