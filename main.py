import random # used for generating the random number
import time # used for the sleep function
import sys # used for the exit function

def main():
    print("To exit the game at any time, type 'exit'.")
    print ("Welcome to Guess the Number!")
    print ("Choose an option:")
    print ("1. Guess the Number")
    print ("2. Guess the Number (Infinite)")
    option = input("Enter your option: ")
    if option == "1":
        guess_the_number()
    elif option == "2":
        guess_the_number_infinite()
    elif option == "3":
        print ("Goodbye!")
        sys.exit()
    elif option == "exit":
        print("Goodbye!")
        sys.exit()    
    else:
        print ("An error occoured. Restarting the program...")
        main()  # restarts the program

def select_difficulty():
    print ("I might have broken this thing but idc.")
    print("To exit the game at any time, type 'exit'.")
    print("To change difficulty at any time, type 'change'.")
    print("Choose a difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Insane")
    print ("5. Custom")
    difficulty = input("Enter your choice: ")
    if difficulty == "exit":
        print("Goodbye!")
        sys.exit()
    return difficulty

difficulty = select_difficulty()

def guess_the_number():
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
    elif difficulty == "5":
        print("Warning: This feature is in development and may not work as expected.")
        print("Enter the range of the number you want to guess (e.g. 1, 100)")
        min_num = int(input("Enter the minimum number: "))
        max_num = int(input("Enter the maximum number: "))
        number = random.randint(min_num, max_num)
        print("I'm thinking of a number between", min_num, "and", max_num)
    elif difficulty == "change":
        select_difficulty()
    else:
        print("An error occoured. Restarting the game...")
        guess_the_number()
    guess = input("Guess the number: ")
    if guess.isdigit() and 1 <= int(guess) <= 50: # checks if the variable guess is an integer and if it's between 1 and 50
        if int(guess) == number:
            print ("Congratulations, you won!")
            play_again()
        else:
            print ("Sorry, that's not the number I was thinking of.")
            print ("The number I was thinking of was", number)
            play_again()

def guess_the_number_infinite():
    print("To exit the game at any time, type 'exit'.")
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
    elif difficulty == "5":
        print("Warning: This feature is in development and may not work as expected.")
        print("Enter the range of the number you want to guess (e.g. 1, 100)")
        min_num = int(input("Enter the minimum number: "))
        max_num = int(input("Enter the maximum number: "))
        number = random.randint(min_num, max_num)
        print("I'm thinking of a number between", min_num, "and", max_num)
    elif difficulty == "change":
        select_difficulty()
    else:
        print("An error occoured. Restarting the game...")
        guess_the_number_infinite()
    guess = input("Guess the number: ")
    if guess == "exit":
        print("Goodbye!")
        sys.exit()
    if guess.isdigit() and 1 <= int(guess) <= 50: # checks if the variable guess is an integer and if it's between 1 and 50
        if int(guess) == number:
            print ("Congratulations, you won!")
            guess_the_number_infinite()
        else:
            print ("Sorry, that's not the number I was thinking of.")
            print ("The number I was thinking of was", number)
            guess_the_number_infinite()

def play_again():
    print ("Would you like to play again?")
    print ("1. Yes")
    print ("2. No")
    wyltpa = input("Enter your choice: ")
    if wyltpa == "1":
        guess_the_number()
    else:
        print ("Goodbye!")
        sys.exit()

main() # starts the program
