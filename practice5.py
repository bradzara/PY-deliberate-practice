# Use a variable to store a number, then write a condition that prints 0 if the number is equal to 10, and prints -1 otherwise.

# number = 5
# if number == 10:
#   print(0)
# else:
#   print(-1)

# # Use a variable to store a number, then write a condition that prints -1 if the number is less than 10, prints 1 if the number is greater than 10, and prints 0 if the number is equal to 10.

# number = 7
# if number < 10:
#   print(-1)
# elif number > 10:
#   print(1)
# elif number == 10:
#   print(0)

# # Use variables to store two numbers, then write a condition that prints 1 if the numbers are both less than 10, and prints 0 otherwise.

# num1 = 4
# num2 = 9
# if num1 < 10 & num2 < 10:
#   print(1)
# else:
#   print(0)

# # Use a variable to store a number, then write a condition that prints 9 if the number is less than 10, prints 19 if the number is less than 20, prints 29 if the number is less than 30, and prints -1 otherwise (only one print statement should occur).

# number = 6
# if number < 10:
#   print(9)
# elif number < 20:
#   print(19)
# elif number < 30:
#   print(29)
# else:
#   print(-1)

print("----")
# Write a while loop to print the numbers 1 through 10.

# i = 1
# while i <= 10:
#   print(i)
#   i += 1


# Write a while loop that asks the user to enter a word and will run forever until the user enters the word "stop".

# while True:
#   word = input("Enter a word: ")
#   if word == "stop":
#     break



# Write a while loop that prints the numbers 0 through 100, increasing by 5 each time.

# i = 0
# while i <= 100:
#   print(i)
#   i += 5



# Write a while loop that asks the user to enter a number and will run forever until the user enters a number greater than 10.

# while True:
#   number = input("Enter a number: ")
#   if int(number) > 10:
#     break

# Write a while loop that asks the user to enter a word and will run forever until the user enters a word with more than 5 letters.

# while True:
#   word = input("Entera word: ")
#   if len(word) > 5:
#     break


# Write a while loop that prints the even numbers from 2 to 40.

# number = 2
# while number <= 40:
#   print(number)
#   number += 2

# Create an array to store 3 words. Then add two more words to the array and print the array on one line.

# words = ["These", "are", "words"]
# words.append("more")
# words.append("words")
# print(words)

# Create an array to store 4 letters. Then change the second letter to a number and print the array on one line.

# array = ["a", "t", "o", "f"]
# array[1] = 2
# print(array)

# Create an array to store 5 numbers. Then print out each number on separate lines with a while loop.

# numbers = [4, 5, 2, 6]
# for number in numbers:
#   print(number)

# Create an array to store 3 strings with lower case letters. Then change the third string to have all capital letters and print the array on one line.

words = ["asdf", "qwer", "zxcv"]
words[2] = words[2].upper()
print(words)