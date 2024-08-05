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

# Start with an array of strings and create a new array with each string's length.
# For example, ["hello", "goodbye"] becomes [5, 7].

strings = ["hello", "goodbye"]
strings_count = [len(string) for string in strings]
print(strings_count)

# Start with an array of hashes and create a new array of number values from each hash's :age key.
# For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes [27, 16]

people = [{"name": "Alice", "age": 27}, {"name": "Blane", "age": 16}]
ages = [age["age"] for age in people]
print(ages)

# Start with an array of numbers and create a new array with only the numbers less than 20.
# For example, [2, 32, 80, 18, 12, 3] becomes [2, 18, 12, 3].

numbers = [2, 32, 80, 18, 12, 3]
new_numbers = [number for number in numbers if number < 20]
print(new_numbers)

# Start with an array of strings and create a new array with only the strings that start with the letter "w".
# For example, ["winner", "winner", "chicken", "dinner"] becomes ["winner", "winner"].

strings = ["winner", "winner", "chicken", "dinner"]
new_strings = [string for string in strings if string[0] == "w"]
print(new_strings)

# Start with an array of hashes and create a new array with only the hashes with names shorter than 6 letters (from the :name key).
# For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "chair", price: 100}, {name: "book", price: 4}].

items = [{"name": "chair", "price": 100}, {"name": "pencil", "price": 1}, {"name": "book", "price": 4}]
new_items = [item for item in items if len(item["name"]) < 6]
print(new_items)

# Start with an array of numbers and compute the sum of all the numbers.
# For example, [5, 10, 8, 3] becomes 26.

numbers = [5, 10, 8, 3]
sum = 0
for number in numbers:
  sum += number
print(sum)

# Start with an array of hashes and compute the sum of the prices (from the :price key).
# For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes 105.

items = [{"name": "chair", "price": 100}, {"name": "pencil", "price": 1}, {"name": "book", "price": 4}]
sum = 0
for item in items:
  sum += item["price"]
print(sum)

# Start with an array of numbers and compute the the minimum number.
# For example, [5, 10, 8, 3, 9] becomes 3.

numbers = [5, 10, 8, 3, 9]
smallest = numbers[0]
for number in numbers:
  if number < smallest:
    smallest = number
print(smallest)

# Write a program that stores a person's order value and membership level (regular or premium). Then calculate a discount amount based on the following conditions:

# If the total order value is less than $50, there is no discount.
# If the total order value is between $50 and $100, the discount is 5% for regular customers and 10% for premium customers.
# If the total order value is greater than $100, the discount is 10% for regular customers and 15% for premium customers.

total = 108.73
membership = "regular"

if total < 50:
  total = total
elif total >= 50 and total <= 100:
  if membership == "regular":
    total *= .95
  else:
    total *= .90
else:
  if membership == "regular":
    total *= .90
  else:
    total *= .85
total = round(total, 2)
print(f"${total}")