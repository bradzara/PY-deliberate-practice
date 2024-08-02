# Use a nested loop to convert an array of string arrays into a single string.
# For example, [["a", "man"], ["a", "plan"], ["a", "canal"], ["panama"]] becomes "amanaplanacanalpanama".

strings = [["a", "man"], ["a", "plan"], ["a", "canal"], ["panama"]]
combined_string = ""

index1 = 0 
while index1 < len(strings):
  words = strings[index1]
  index2 = 0
  while index2 < len(words):
    combined_string += words[index2]
    index2 += 1
  index1 += 1

print(combined_string)