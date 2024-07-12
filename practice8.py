# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year).

name = input("What is your name? ")
age = int(input("Enter your age? "))
year = 2024 - age + 100
print(f"You will turn 100 in the year {year}")

