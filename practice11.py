# Start with an array of numbers and create a new array with only the numbers less than 20.
# For example, [2, 32, 80, 18, 12, 3] becomes [2, 18, 12, 3].

numbers = [2, 32, 80, 18, 12, 3]
small_numbers = [number for number in numbers if number < 20]
print(small_numbers)

# Start with an array of strings and create a new array with only the strings that start with the letter "w". For example, ["winner", "winner", "chicken", "dinner"] becomes ["winner", "winner"].

strings = ["winner", "winner", "chicken", "dinner"]
w_strings = [string for string in strings if string[0] == "w"]
print(w_strings)

# Start with an array of hashes and create a new array with only the hashes with prices greater than 5 (from the :price key). For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "chair", price: 100}].

items = [{"name": "chair", "price": 100}, {"name": "pencil", "price": 1}, {"name": "book", "price": 4}]
expensive_items = [item for item in items if item["price"] > 5]
print(expensive_items)

# Start with an array of numbers and create a new array with only the even numbers.
# For example, [2, 4, 5, 1, 8, 9, 7] becomes [2, 4, 8].

numbers = [2, 4, 5, 1, 8, 9, 7]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# Start with an array of strings and create a new array with only the strings shorter than 4 letters.
# For example, ["a", "man", "a", "plan", "a", "canal", "panama"] becomes ["a", "man", "a", "a"].

strings = ["a", "man", "a", "plan", "a", "canal", "panama"]
short_strings = [string for string in strings if len(string) < 4]
print(short_strings)

# Start with an array of hashes and create a new array with only the hashes with names shorter than 6 letters (from the :name key). For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "chair", price: 100}, {name: "book", price: 4}].

items = [{"name": "chair", "price": 100}, {"name": "pencil", "price": 1}, {"name": "book", "price": 4}]
short_names = [item for item in items if len(item["name"]) < 6]
print(short_names)


# Start with an array of numbers and create a new array with only the numbers less than 10.
# For example, [8, 23, 0, 44, 1980, 3] becomes [8, 0, 3].

numbers = [8, 23, 0, 44, 1980, 3]
small_numbers = [number for number in numbers if number < 10]
print(small_numbers)

# Start with an array of strings and create a new array with only the strings that don't start with the letter "b". For example, ["big", "little", "good", "bad"] becomes ["little", "good"].

strings = ["big", "little", "good", "bad"]
new_strings = [string for string in strings if string[0] != "b"]
print(new_strings)

# Start with an array of hashes and create a new array with only the hashes with prices less than 10 (from the :price key). For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes [{name: "pencil", price: 1}, {name: "book", price: 4}].

items = [{"name": "chair", "price": 100}, {"name": "pencil", "price": 1}, {"name": "book", "price": 4}]
inexpensive_items = [price for price in items if price["price"] < 10]
print(inexpensive_items)

# Start with an array of numbers and create a new array with only the odd numbers.
# For example, [2, 4, 5, 1, 8, 9, 7] becomes [5, 1, 9, 7].

numbers = [2, 4, 5, 1, 8, 9, 7]
odd_numbers = [number for number in numbers if number % 2 == 1]
print(odd_numbers)