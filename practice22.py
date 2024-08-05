# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

number = int(input('Enter a number and see what its divisors are: '))
divisors = []
index = number
while index > 0:
  if number % index == 0:
    divisors.append(index)
  index -= 1
print(divisors)