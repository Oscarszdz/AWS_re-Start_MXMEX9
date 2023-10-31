import random

# Printing the game rules
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1, 10)

# Track whether the user guessed your number by creating a variable called is_guess_right
is_guess_right = False

# TO handle the game logic, create a while loop
while is_guess_right != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print(f"You guessed {guess}. That is correct!. You win champion!")
        is_guess_right = True
    else:
        print(f"You guessed {guess}. Sorry that is not it. Try again!.")