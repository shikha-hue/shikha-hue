import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        
        self.user_score = 0
        self.computer_score = 0
        
        self.create_widgets()
    
    def create_widgets(self):
        # Create buttons for user choices
        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play_game("rock"))
        self.rock_button.pack(pady=10)
        
        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play_game("paper"))
        self.paper_button.pack(pady=10)
        
        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play_game("scissors"))
        self.scissors_button.pack(pady=10)
        
        # Label to display the result
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)
        
        # Label to display the scores
        self.score_label = tk.Label(self.root, text="User: 0, Computer: 0", font=("Helvetica", 14))
        self.score_label.pack(pady=10)
        
    def play_game(self, user_choice):
        computer_choice = random.choice(["rock", "paper", "scissors"])
        result = self.determine_winner(user_choice, computer_choice)
        
        self.result_label.config(text=f"You chose {user_choice.capitalize()}, Computer chose {computer_choice.capitalize()}. {result}")
        self.score_label.config(text=f"User: {self.user_score}, Computer: {self.computer_score}")
    
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "Computer wins!"
    
if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
