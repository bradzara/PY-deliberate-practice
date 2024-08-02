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

# Convert an array of arrays into a hash.
# For example, [[1, 3], [8, 9], [2, 16]] becomes {1 => 3, 8 => 9, 2 => 16}.

pairs = [[1, 3], [8, 9], [2, 16]]
pairs_hash = {}
index = 0
while index < len(pairs):
  key = pairs[index][0]
  value = pairs[index][1]
  pairs_hash[key] = value
  index += 1
print(pairs_hash)


# Convert an array of hashes into a hash using the :id key from the array's hashes as the keys in the new hash. For example, [{id: 1, color: "blue", price: 32}, {id: 2, color: "red", price: 12}] becomes {1 => {id: 1, color: "blue", price: 32}, 2 => {id: 2, color: "red", price: 12}}.

array = [{"id": 1, "color": "blue", "price": 32}, {"id": 2, "color": "red", "price": 12}]
hash = {}
index = 0
while index < len(array):
  hash[array[index]["id"]] = array[index]
  index += 1
print(hash)