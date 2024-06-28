first_name = "Bradley"
last_name = "Zara"

print(first_name + " " + last_name)
print(f"{first_name} {last_name}")

numbers = [1, 2, 3]
new_numbers = []
i = 0
while i < len(numbers):
  new_numbers.append(numbers[i] * 3)
  i += 1

print(new_numbers)

words = ["hello", "goodbye"]
new_words = []
i = 0
while i < len(words):
  new_words.append(words[i].upper())
  i += 1
print(new_words)

words = ["hello", "goodbye"]
new_words = []
i = 0
while i < len(words):
  new_words.append(len(words[i]))
  i += 1
print(new_words)

people = [{"name": "Alice", "age": 27}, {"name": "Blane", "age": 16}]
ages = []
i = 0
while i < len(people):
  ages.append(people[i]["age"])
  i += 1
print(ages)