# Start with an array of numbers and create a new array with each number times 3.
# For example, [1, 2, 3] becomes [3, 6, 9].

numbers = [1, 2, 3]
new_numbers = [number * 3 for number in numbers]
print(new_numbers)

# Start with an array of strings and create a new array with each string upcased.
# For example, ["hello", "goodbye"] becomes ["HELLO", "GOODBYE"].

strings = ["hello", "goodbye"]
new_strings = [string.upper() for string in strings]
print(new_strings)

# Start with an array of hashes and create a new array of string values from each hash's :name key.
# For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes ["Alice", "Blane"].

people = [{"name": "Alice", "age": 27}, {"name": "Blane", "age": 16}]
people_names = [name["name"] for name in people]
print(people_names)

# Start with an array of numbers and create a new array with each number plus 7.
# For example, [1, 2, 3] becomes [8, 9, 10].

numbers = [1, 2, 3]
new_numbers = [number + 7 for number in numbers]
print(new_numbers)

# Start with an array of strings and create a new array with each string's length.
# For example, ["hello", "goodbye"] becomes [5, 7].

strings = ["hello", "goodbye"]
new_strings = [len(string) for string in strings]
print(new_strings)

# Start with an array of hashes and create a new array of number values from each hash's :age key.
# For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes [27, 16].

strings = [{"name": "Alice", "age": 27}, {"name": "Blane", "age": 16}]
new_strings = [ages["age"] for ages in strings]
print(new_strings)

# Start with an array of numbers and create a new array with each number divided by 2.
# For example, [1, 2, 3] becomes [0.5, 1.0, 1.5].

numbers = [1, 2, 3]
new_numbers = [number / 2 for number in numbers ]
print(new_numbers)

# Start with an array of strings and create a new array with each string's first letter only.
# For example, ["hello", "goodbye"] becomes ["h", "g"].

strings = ["hello", "goodbye"]
new_strings = [string[0] for string in strings]
print(new_strings)

# Start with an array of hashes and create a new array of number values from each hash's :age key times 2. For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes [54, 32].

people = [{"name": "Alice", "age": 27}, {"name": "Blane", "age": 16}]
multiplied_age = [ages["age"] * 2 for ages in people]
print(multiplied_age)

# Start with an array of numbers and create a new array with each number converted into a string.
# For example, [1, 2, 3] becomes ["1", "2", "3"].

numbers = [1, 2, 3]
number_to_string = [str(number) for number in numbers]
print(number_to_string)