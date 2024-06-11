# Start with an array of strings and create a new array with only the strings that start with the letter "w".
# For example, ["winner", "winner", "chicken", "dinner"] becomes ["winner", "winner"].

strings = ["winner", "winner", "chicken", "dinner"]
new_strings = []
for string in strings:
  if string[0] == "w":
    new_strings.append(string)
print(new_strings)

# Start with an array of numbers and create a new array with only the odd numbers.
# For example, [2, 4, 5, 1, 8, 9, 7] becomes [5, 1, 9, 7].

numbers = [2, 4, 5, 1, 8, 9, 7]
odd_numbers = []
for number in numbers:
  if number % 2 == 1:
    odd_numbers.append(number)
print(odd_numbers)

# Start with an array of strings and combine them all into a single string.
# For example, ["volleyball", "basketball", "badminton"] becomes "volleyballbasketballbadminton".

strings = ["volleyball", "basketball", "badminton"]
string_combo = strings[0]
for string in strings:
  if string != string_combo:
    string_combo += string
print(string_combo)