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

# Use a nested loop to find the largest sum of any two different numbers within an array.
# For example, [1, 8, 3, 10] becomes 18.

numbers = [1, 8, 3, 10]
largest = numbers[0] + numbers[1]
index1 = 0
while index1 < len(numbers):
  number = numbers[index1]            
  index2 = 0
  while index2 < len(numbers):
    if numbers[index2] != number:
      sum = number + numbers[index2]   
      if sum > largest:
        largest = sum
    index2 += 1
  index1 += 1
print(largest)

# Use nested loops with an array of numbers to compute a new array containing the first two numbers (from the original array) that add up to the number 10. If there are no two numbers that add up to 10, return false. For example, [2, 5, 3, 1, 0, 7, 11] becomes [3, 7].

numbers = [2, 5, 3, 7, 0, 1, 11]
ten = False
index1 = 0
while index1 < len(numbers):
  number = numbers[index1]
  index2 = 0
  while index2 < len(numbers):
    if index1 != index2:
      other_number = numbers[index2]
      if number + other_number == 10 and ten == False:
        ten = [number, other_number]
    index2 += 1
  index1 += 1
print(ten)