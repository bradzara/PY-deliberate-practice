# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year).

# name = input("What is your name? ")
# age = int(input("Enter your age? "))
# year = 2024 - age + 100
# print(f"You will turn 100 in the year {year}")

# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number = int(input("Enter a number: "))
if(number / 4 % 2 == 0):
  print("That number is divisible by 4")
else:
  print("That number was odd")
