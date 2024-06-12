# Write a program that uses a variable to store a number, then prints that number plus 10.

number = 10
print(number + 10)

# Write a program that uses variables to store two numbers, then prints the numbers added together.

num1 = 13
num2 = 28
print(num1 + num2)

# Write a program that uses a variable to store a word, then prints the number of letters in the word.

word = "word"
print(len(word))

# Write a program that uses a variable to store a number with decimals, then prints the number as an integer.

float = 8.34
print(int(float))

# Write a program that uses a variable to store a word, then prints the word with all lowercase letters.

word = "YELLING"
print(word.lower())

# Use a variable to store a number, then write a condition that prints 0 if the number is equal to 10, and prints -1 otherwise.

number = 24
if number == 10:
  print(0)
else:
  print(-1)


# Use a variable to store a number, then write a condition that prints -1 if the number is less than 10, prints 1 if the number is greater than 10, and prints 0 if the number is equal to 10.

number = 53
if number < 10:
  print(-1)
elif number > 10:
  print(1)
else:
  print(0)

# Create an array to store 3 words. Then add two more words to the array and print the array on one line.

words = ["these", "are", "words"]
words.append("more")
words.append("letters")
print(words)

# Create an array to store 5 numbers. Then print out each number on separate lines with a while loop.

numbers = [5, 3, 7, 23, 12]
index = 0 
while index < len(numbers):
  print(numbers[index])
  index += 1

# Create an array to store 3 strings with lower case letters. Then change the third string to have all capital letters and print the array on one line.

strings = ["lower", "case", "words"]
upcase = strings[2].upper()
print(upcase)

# Create an array to store 2 strings. Then add one string to the array and print the array on one line.

strings = ["two", "strings"]
strings.append("lemons")
print(strings)

# Make a hash to store a person's first name, last name, and email address. Then print each attribute on separate lines.

person = {"first_name": "bradley", "last_name": "zara", "email": "bradley.v.zara@gmail.com"}
print(person["first_name"])
print(person["last_name"])
print(person["email"])

# Make a hash to store a book's title, author, number of pages, and language. Then print each attribute on separate lines.

book = {"title": "good book", "author": "Hubert Grape", "number_of_pages": 193, "language": "German"}
print(book["title"])
print(book["author"])
print(book["number_of_pages"])
print(book["language"])