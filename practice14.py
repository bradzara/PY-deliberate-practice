# Use a nested loop to convert an array of number pairs into a single flattened array.
# For example, [[1, 3], [8, 9], [2, 16]] becomes [1, 3, 8, 9, 2, 16].

numbers = [[1, 3], [8, 9], [2, 16]]
flattened = []

index1 = 0
while index1 < len(numbers):
  numbered_pair = numbers[index1]
  index2 = 0
  while index2 < len(numbered_pair):
    flattened.append(numbered_pair[index2])
    index2 += 1
  index1 += 1

print(flattened)

# Use a nested loop with two arrays of strings to create a new array of strings with each string combined. For example, ["a", "b", "c"] and ["d", "e", "f", "g"] becomes ["ad", "ae", "af", "ag", "bd", "be", "bf", "bg", "cd", "ce", "cf", "cg"].

string1 = ["a", "b", "c"]
string2 = ["d", "e", "f", "g"]
new_string = []
index = 0
while index < len(string1):
  index1 = 0
  while index1 < len(string2):
    new_string.append(string1[index] + string2[index1])
    index1 += 1
  index += 1

print(new_string)

# Use a nested loop with one array of strings to create a new array that contains every combination of each string with every other string in the array.
# For example, ["a", "b", "c", "d"] becomes ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"].

strings = ["a", "b", "c", "d"]
combos = []
index = 0
while index < len(strings):
  index1 = 0
  while index1 < len(strings):
    if strings[index] != strings[index1]:
      combos.append(strings[index] + strings[index1])
    index1 += 1
  index += 1

print(combos)

