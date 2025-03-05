import random

def main():
    print ("Choose an option:")
    print ("1. Start Game")
    print ("2. Quit Game")
    option = input("Enter your option: ")
    if option == "1":
        start_game()
    elif option == "2":
        print ("Goodbye!")
        exit()

def start_game():
    number = random.randint(1, 10)
    print ("Welcome to the game!")
    print ("I'm thinking of a number between 1 and 10.")
    guess = input("Guess the number: ")
    if guess.isdigit() and 1 <= int(guess) <= 10:
        if int(guess) == number:
            print ("Congratulations, you won!")
            play_again()
        else:
            print ("Sorry, that's not the number I was thinking of.")
            print ("The number I was thinking of was", number)
            play_again()
            
def play_again():
    print ("Would you like to play again?")
    print ("1. Yes")
    print ("2. No")
    wyltpa = input("Enter your choice: ")
    if wyltpa == "1":
        start_game()
    else:
        print ("Goodbye!")
        exit()
main()
