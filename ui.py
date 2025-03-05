import tkinter as tk
import random

class NumberGuessingGameUI:
    def __init__(self, master):
        self.master = master
        master.title("Number Guessing Game")

        self.output_text = tk.Text(master, height=15, width=50)
        self.output_text.pack()

        self.guess_label = tk.Label(master, text="Choose a difficulty:")
        self.guess_label.pack()

        self.easy_button = tk.Button(master, text="Easy", command=lambda: self.start_game(1))
        self.easy_button.pack()

        self.medium_button = tk.Button(master, text="Medium", command=lambda: self.start_game(2))
        self.medium_button.pack()

        self.hard_button = tk.Button(master, text="Hard", command=lambda: self.start_game(3))
        self.hard_button.pack()

        self.insane_button = tk.Button(master, text="Insane", command=lambda: self.start_game(4))
        self.insane_button.pack()

        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack()

        self.guess_button = tk.Button(master, text="Submit Guess", command=self.process_guess)
        self.guess_button.pack()

        self.number = 0

    def start_game(self, difficulty):
        if difficulty == 1:
            self.number = random.randint(1, 10)
            self.output_text.insert(tk.END, "I'm thinking of a number between 1 and 10.\n")
        elif difficulty == 2:
            self.number = random.randint(1, 20)
            self.output_text.insert(tk.END, "I'm thinking of a number between 1 and 20.\n")
        elif difficulty == 3:
            self.number = random.randint(1, 30)
            self.output_text.insert(tk.END, "I'm thinking of a number between 1 and 30.\n")
        elif difficulty == 4:
            self.number = random.randint(1, 50)
            self.output_text.insert(tk.END, "I'm thinking of a number between 1 and 50.\n")

    def process_guess(self):
        guess = self.guess_entry.get()
        if guess.isdigit() and 1 <= int(guess) <= 50:
            if int(guess) == self.number:
                self.output_text.insert(tk.END, "Congratulations, you won!\n")
            else:
                self.output_text.insert(tk.END, f"Sorry, that's not the number. It was {self.number}.\n")
        else:
            self.output_text.insert(tk.END, "Invalid input. Please enter a number between 1 and 50.\n")

if __name__ == "__main__":
    root = tk.Tk()
    game_ui = NumberGuessingGameUI(root)
    root.mainloop()
