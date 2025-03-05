import random # used for generating the random number

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
    print ("IMPORTANT: Only the first difficulty is implemented for now!!!!")
    print("Choose a difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Insane")
    difficulty = input("Enter your difficulty: ")
    if difficulty == "1":
        game_diff1()
    elif difficulty == "2":
        game_diff2()
    elif difficulty == "3":
        game_diff3()
    elif difficulty == "4":
        game_diff4()
    else:
        print("Invalid difficulty")
        start_game()


def game_diff1():
    number = random.randint(1, 10)
    print ("Easy")
    print ("I'm thinking of a number between 1 and 10.")
    guess = input("Guess the number: ")
    if guess.isdigit() and 1 <= int(guess) <= 10: # checks if the variable guess is an integer and if that is between 1 and 10
        if int(guess) == number:
            print ("Congratulations, you won!")
            play_again()
        else:
            print ("Sorry, that's not the number I was thinking of.")
            print ("The number I was thinking of was", number)
            play_again()

def game_diff2():
    number = random.randint(1, 20)
    print ("Medium")
    print ("I'm thinking of a number between 1 and 20.")
    guess = input("Guess the number: ")
    if guess.isdigit() and 1 <= int(guess) <= 20: # checks if the variable guess is an integer and if that is between 1 and 20
        if int(guess) == number:
            print ("Congratulations, you won!")
            play_again()
        else:
            print ("Sorry, that's not the number I was thinking of.")
            print ("The number I was thinking of was", number)
            play_again()

def game_diff3():
    number = random.randint(1, 30)
    print ("Hard")
    print ("I'm thinking of a number between 1 and 30.")
    guess = input("Guess the number: ")
    if guess.isdigit() and 1 <= int(guess) <= 30: # checks if the variable guess is an integer and if that is between 1 and 30
        if int(guess) == number:
            print ("Congratulations, you won!")
            play_again()
        else:
            print ("Sorry, that's not the number I was thinking of.")
            print ("The number I was thinking of was", number)
            play_again()

def game_diff4():
    number = random.randint(1, 50)
    print ("Insane")
    print ("I'm thinking of a number between 1 and 50.")
    guess = input("Guess the number: ")
    if guess.isdigit() and 1 <= int(guess) <= 50: # checks if the variable guess is an integer and if that is between 1 and 50
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

main() # starts the program
