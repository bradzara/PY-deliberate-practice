# Write a program that uses variables to store a first and last name, then prints the full name in one line using string concatenation (the + operator).

first_name = "Bradley"
last_name = "Zara"

print(first_name + " " + last_name)

# Write a program that uses variables to store three different colors, then prints out a sentence using the colors with string interpolation (the #{} operator).

color1 = "red"
color2 = "blue"
color3 = "green"

print(f"The colors i chose were {color1}, {color2}, {color3}.")

# Write a program that asks the user to enter a password. If the password is "Joshua", the program responds "Shall we play a game?". For any other password, the program responds "Access denied"

password = input("Enter a password: ")
if password == "Joshua":
  print("Shall we play a game?")
else:
  print("Access denied")