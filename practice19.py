import datetime

# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). 
# Extras: 
# 1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
# 2. Print out that many copies of the previous message on separate lines. 

# Current year
now = datetime.datetime.now()

# Get user info
name = input('Enter you name: ')
age = int(input('Enter your age: '))
copies = int(input('How many copies of the message would you like?: '))

# Compute age
years_to_100 = 100 - age

# Print statement telling user the year they will turn 100
print(f'{name}, you will turn 100 years old in the year {now.year + years_to_100}\n' * copies)

