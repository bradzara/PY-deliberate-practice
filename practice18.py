# Write a program that uses variables to store a first and last name, then prints the full name in one line using string concatenation (the + operator).

first = "John"
last = "Smith"
print(first + " " + last)

# Write a program that uses variables to store a first and last name, then prints the full name in one line using string interpolation (the #{} operator).

first = "John"
last = "Smith"
print(f"{first} {last}")

# Write a program that asks the user to input a word. If the word is "marco", print "polo".

# word = input("Input a word: ")
# if word == "marco":
#   print("polo")


# Start with an array of numbers and create a new array with each number times 3.
# For example, [1, 2, 3] becomes [3, 6, 9].

numbers = [1, 2, 3]
new_numbers = [number * 3 for number in numbers]
print(new_numbers)

# Start with an array of numbers and create a new array with each number plus 7.
# For example, [1, 2, 3] becomes [8, 9, 10].

numbers = [1, 2, 3]
new_numbers = [number + 7 for number in numbers]
print(new_numbers)