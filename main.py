import random # used for generating the random number
difficulty = 0
def main():
    print ("Choose an option:")
    print ("1. Start Game")
    print ("2. Quit Game")
    option = input("Enter your option: ")
    if option == "1":
        game()
    elif option == "2":
        print ("Goodbye!")
        exit()


def game():
    print("Choose a difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Insane")
    print ("5. Custom")
    difficulty = input("Enter your choice: ")
    if difficulty == "1":
        number = random.randint(1, 10)
        print ("Easy")
        print ("I'm thinking of a number between 1 and 10.")
    elif difficulty == "2":
        number = random.randint(1, 20)
        print ("Medium")
        print ("I'm thinking of a number between 1 and 20.")
    elif difficulty == "3":
        number = random.randint(1, 30)
        print ("Hard")
        print ("I'm thinking of a number between 1 and 30.")
    elif difficulty == "4":
        number = random.randint(1, 50)
        print ("Insane")
        print ("I'm thinking of a number between 1 and 50.")
    else:
        print("An error occoured. Restarting the game...")
        game()
    guess = input("Guess the number: ")
    if guess.isdigit() and 1 <= int(guess) <= 50: # checks if the variable guess is an integer and if it's between 1 and 50
        if int(guess) == number:
            print ("Congratulations, you won!")
            play_again()
        else:
            print ("Sorry, that's not the number I was thinking of.")
            print ("The number I was thinking of was", number)
            play_again()

def set_custom_difficulty():
    print("Coming soon!")
    game()

def play_again():
    print ("Would you like to play again?")
    print ("1. Yes")
    print ("2. No")
    wyltpa = input("Enter your choice: ")
    if wyltpa == "1":
        game()
    else:
        print ("Goodbye!")
        exit()

main() # starts the program
