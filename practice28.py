# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.).

import sys

number = int(input("Enter a number to see if it is prime: "))

# if number > 0:
#   for x in range(2, number):
#     if number % x != 0:
#       continue
#     elif number % x == 0:
#       sys.exit('The number is not prime')
#   sys.exit('The number is prime')
# elif number == 0:
#   sys.exit("The number is not prime")
# else:
#   sys.exit("The number is not prime")

input = [x for x in range(2, number) if number % x == 0]

def is_prime(n):
  if number > 1:
    if len(input) == 0:
      return('prime')
    else:
      return('Not prime')

print(is_prime(number))