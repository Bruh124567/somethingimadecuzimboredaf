import random # used for generating the random number
import time # used for the sleep function
import sys # used for the exit function

def main():
    print("Welcome to Guess the Number!")
    difficulty = select_difficulty()
    numguess(difficulty)

def select_difficulty():
    print("To exit the game at any time, type 'exit'.")
    print("To change difficulty at any time, type 'change'.")
    print("Choose a difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Insane")
    print("5. Custom")
    difficulty = input("Enter your choice: ")
    if difficulty == "exit":
        print("Goodbye!")
        time.sleep(2)
        sys.exit()
    return difficulty

def guess_the_number(difficulty):
    print("To exit the game at any time, type 'exit'.")
    if difficulty == "1":
        min_num = 1
        max_num = 10
        number = random.randint(min_num, max_num)
        print("Easy")
        print("I'm thinking of a number between 1 and 10.")
    elif difficulty == "2":
        min_num = 1
        max_num = 20
        number = random.randint(min_num, max_num)
        print("Medium")
        print("I'm thinking of a number between 1 and 20.")
    elif difficulty == "3":
        min_num = 1
        max_num = 30
        number = random.randint(min_num, max_num)
        print("Hard")
        print("I'm thinking of a number between 1 and 30.")
    elif difficulty == "4":
        min_num = 1
        max_num = 50
        number = random.randint(min_num, max_num)
        print("Insane")
        print("I'm thinking of a number between 1 and 50.")
    elif difficulty == "5":
        print("Enter the range of the number you want to guess (e.g. 1, 100)")
        min_num = (input("Enter the minimum number: "))
        if min_num == "exit":
            print("Goodbye!")
            time.sleep(2)
            sys.exit()
        else:
            max_num = (input("Enter the maximum number: "))
            number = random.randint(min_num, max_num)
            print("I'm thinking of a number between", min_num, "and", max_num)
    elif difficulty == "change":
        difficulty = select_difficulty()
        return guess_the_number(difficulty)
    else:
        print("An error occurred. Restarting the game...")
        main()
    return number, min_num, max_num

def numguess(difficulty):
    number, min_num, max_num = guess_the_number(difficulty)
    while True:
        guess = input("Input your guess: ")
        if guess == "exit":
            print("Goodbye!")
            time.sleep(2)
            sys.exit()
        elif guess == "change":
            difficulty = select_difficulty()
            number, min_num, max_num = guess_the_number(difficulty)
        elif guess.isdigit():
            if int(guess) == number:
                print("Congratulations, you won!")
                time.sleep(2)
                difficulty = select_difficulty()
                number, min_num, max_num = guess_the_number(difficulty)
            elif int(guess) > number:
                print("Too High")
            elif int(guess) < number:
                print("Too Low")
        else:
            print("Invalid input. Please enter a number.")
main()