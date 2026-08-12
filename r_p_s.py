import tkinter as tk
import random
root = tk.Tk()
root.title("Rock, Paper and Scissors")

choices = ("rock","paper","scissors")


result_label = tk.Label()
result_label.pack()

def play_game(player_move):
	global computer_choice
	computer_choice = random.choice(choices)

	if computer_choice == player_move:
		result_label.config(text=f"You Played {player_move}! \n Computer played {computer_choice}! \n Tie!")
	elif player_move == "rock" and computer_choice == "scissors":
		result_label.config(text=f"You Played {player_move}! \n Computer played {computer_choice}!\n You won!")
	elif player_move == "paper" and computer_choice == "rock":
		result_label.config(text=f"You Played {player_move}! \n Computer played {computer_choice}! \n  You won!")
	elif player_move == "scissors" and computer_choice == "paper":
		result_label.config(text=f"You Played {player_move}! \n Computer played {computer_choice}! \n You won!")
	else:
		result_label.config(text=f"You Played {player_move}! \n Computer played {computer_choice}! \n Computer won!")
	

button=tk.Button(text=("Rock"), command=lambda: play_game("rock"), width=20, height=4, bg="blue").pack(pady=20)
button=tk.Button(text=("Paper"), command=lambda: play_game("paper"), width=20, height=4, bg="green").pack(pady=20)
button=tk.Button(text=("Scissors"), command=lambda: play_game("scissors"), width=20, height=4, bg="red").pack(pady=20)


root.mainloop()