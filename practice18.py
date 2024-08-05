# Write a program that uses variables to store a first and last name, then prints the full name in one line using string concatenation (the + operator).

first = "John"
last = "Smith"
print(first + " " + last)

# Write a program that uses variables to store a first and last name, then prints the full name in one line using string interpolation (the #{} operator).

first = "John"
last = "Smith"
print(f"{first} {last}")

# Write a program that asks the user to input a word. If the word is "marco", print "polo".

word = input("Input a word: ")
if word == "marco":
  print("polo")