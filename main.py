import random

top_range = input("Pick a number to set the range: ")

if top_range.isdigit():
    top_range = int(top_range)
    if top_range <= 0:
        print("Please enter a number greater than zero.")
        quit()
else:
    print("That’s not a valid number. Please try again.")
    quit()

random_number = random.randint(0, top_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Take a guess: ")
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("That’s not a number. Try again.")
        continue

    if user_guess == random_number:
        print(f"Well done! You guessed it in {guesses} tries.")
        break
    elif user_guess > random_number:
        print("Too high. Try again.")
    else:
        print("Too low. Try again.")
