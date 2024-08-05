# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


number = int(input('Enter a number: '))
check = int(input('Enter a number to divide your first number by: '))

if number % 2 == 0:
  if number % 4 == 0:
    print("This is an even number that is divisible by 4")
  else:
    print("This is an even number")
elif number % 2 == 1:
  print("This is an odd number")

if number % check == 0:
  print(f'{check} divides evenly into {number}')
else:
  print(f'{check} does not divide evenly into {number}')