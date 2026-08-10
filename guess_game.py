import tkinter as tk
import random 
root = tk.Tk()
root.title("guessing game")

number = random.randint(1,10)
guess = tk.StringVar()

tk.Entry(textvariable = guess).pack()

label=tk.Label()
label.pack()
guess_label=tk.Label()
guess_label.pack()
guess_count = 0

def check_guess():
	player_guess=int(guess.get())
	if player_guess == number:
		label.config(text=("You guessed the right number!"))
	elif player_guess > number:
		label.config(text=("Too high!"))
	elif player_guess <	number:
		label.config(text="Too low!")
	global guess_count
	guess_count += 1
	guess_label.config(text=f"Guesses: {guess_count}")
def new_game():
	global number
	global guess_count
	number = random.randint(1,10)
	guess.set("")
	label.config(text=("Guess the number!"))
	guess_count = 0
	guess_label.config(text="Guesses: 0")

button=tk.Button(text=("New Game"), command=new_game).pack()

button = tk.Button(text=("Guess!"), command=check_guess).pack()
root.mainloop()