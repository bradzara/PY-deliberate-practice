# Use a nested loop to find the largest product of any two different numbers within a given array.
# For example, [5, -2, 1, -9, -7, 2, 6] becomes 63.

numbers = [5, -2, 1, -9, -7, 2, 6]
max_product = numbers[0] * numbers[1]
index1 = 0 
while index1 < len(numbers):
  first_number = numbers[index1]
  index2 = 0
  while index2 < len(numbers):
    if first_number != numbers[index2]:
      second_number = numbers[index2]
      product = first_number * second_number
      if max_product < product:
        max_product = product
    index2 +=1
  index1 += 1

print(max_product)

# Use a nested loop to compute the sum of all the numbers in an array of number pairs.
# For example, [[1, 3], [8, 9], [2, 16]] becomes 39.

numbers = [[1, 3], [8, 9], [2, 16]]
total = 0
index1 = 0
while index1 < len(numbers):
  number_pair = numbers[index1]
  index2 = 0
  while index2 < len(number_pair):
    number = number_pair[index2]
    total += number
    index2 += 1
  index1 += 1

print(total)

# Use a nested loop with two arrays of numbers to create a new array of the sums of each combination of numbers. For example, [1, 2] and [6, 7, 8] becomes [7, 8, 9, 8, 9, 10].

numbers1 = [1, 2]
numbers2 = [6, 7, 8]
new_numbers = []
index1 = 0
while index1 < len(numbers1):
  number = numbers1[index1]
  index2 = 0
  while index2 < len(numbers2):
    number2 = numbers2[index2]
    new_numbers.append(number + number2)
    index2 += 1
  index1 += 1
print(new_numbers)