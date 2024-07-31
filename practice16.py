# Use a nested loop with an array of numbers to compute an array with every combination of products from each number. For example, [2, 8, 3] becomes [4, 16, 6, 16, 64, 24, 6, 24, 9].

numbers = [2, 8, 3]
new_numbers = []

index1 = 0
while index1 < len(numbers):
  number = numbers[index1]
  index2 = 0
  while index2 < len(numbers):
    new_numbers.append(number * numbers[index2])
    index2 += 1
  index1 += 1
print(new_numbers)

