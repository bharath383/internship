import random
import time

def generate_number():
    return random.randint(1, 200)

def intro():
    print("May I ask you for your name?")
    name = input()  # asks for the name
    print(f"{name}, we are going to play a game. I am thinking of a number between 1 and 200.")
    time.sleep(0.5)
    print("Go ahead. Guess!")
    return name

def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if 1 <= guess <= 200:
                return guess
            else:
                print("Silly Goose! That number isn't in the range! Please enter a number between 1 and 200.")
        except ValueError:
            print("I don't think that is a number. Sorry.")

def pick(number, name):
    guesses_taken = 0
    while guesses_taken < 6:
        guess = get_guess()
        guesses_taken += 1
        if guess < number:
            print("The guess of the number that you have entered is too low.")
        elif guess > number:
            print("The guess of the number that you have entered is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            return
        if guesses_taken < 6:
            print("Try Again!")

    print(f'Nope. The number I was thinking of was {number}.')

def play_game():
    play_again = "yes"
    while play_again.lower() in ["yes", "y"]:
        number = generate_number()
        name = intro()
        pick(number, name)
        print("Do you want to play again?")
        play_again = input().strip()

if __name__ == "__main__":
    play_game()