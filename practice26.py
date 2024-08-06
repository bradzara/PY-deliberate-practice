# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

number = random.randint(1, 9)

print("The computer has picked a random number 1 through 9, guess the number. You can also type 'exit' to quit.")

counter = 0

while True:
  guess = int(input("Your guess: "))
  if guess < number:
    counter += 1
    print("Your guess is too low.. guess again")
    continue
  elif guess > number:
    counter += 1
    print("Your guess is too low.. guess again")
    continue
  elif guess == number:
    counter += 1
    print(f"You guessed it! It took you {counter} tries.")
    break
  elif guess == "exit":
    break
  else:
    print("Invalid command. Please pick a number 1 through 9 or type 'exit' to quit.")
    continue
