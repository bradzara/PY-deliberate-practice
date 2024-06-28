# Write a program that uses variables to store a first and last name, then prints the full name in one line using string concatenation (the + operator).

first_name = "Bradley"
last_name = "Zara"
print (first_name + ' ' + last_name)

# Write a program that uses variables to store three different colors, then prints out a sentence using the colors with string interpolation (the #{} operator).

color1 = "Red"
color2 = "green"
color3 = "blue"
print(f"{color1}, {color2}, {color3}.")

# Write a program that uses variables to store the names of three cities, then prints out a sentence using that information with string concatenation (the + operator).

city1 = "Philadelphia"
city2 = "Trenton"
city3 = "Los Angeles"
print("The three cities I have lived in are: " + city1 + ", " + city2 + ", and " + city3 + ".")

# Start with an array of numbers and create a new array with each number times 3.
# For example, [1, 2, 3] becomes [3, 6, 9].

numbers = [1, 2, 3]
new_numbers = []
i = 0
while i < len(numbers):
  new_numbers.append(numbers[i] * 3)
  i += 1
print(new_numbers)