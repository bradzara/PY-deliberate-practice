# Write a program that stores a customer's age and a movie's time in two separate variables. Then calculate the price of a movie ticket based on the following conditions:

# If the age is 12 years old or younger, the ticket price is $5.
# If the age is between 13 and 59 years old and the movie is before 6 PM, the ticket price is $7. After 6 PM, the ticket price is $10.
# If the customer is 60 years old or older, the ticket price is $7.

age = 30
movie_time = 4

if age <= 12:
  price = 5
elif age >= 60:
  price = 7
else:
  if movie_time < 6:
    price = 7
  else:
    price = 10

print(price)


# Write a program to store the type of book (regular, reference, or special collection) and the number of days its overdue. Then calculate the fine amount based on the following conditions:

# If the book is a regular book and overdue by up to 7 days, the fine is $1 per day.
# If the book is a regular book and overdue by more than 7 days, the fine is $2 per day.
# If the book is a reference book, there is no fine, regardless of the number of days overdue.
# If the book is a special collection book, the fine is $5 per day, regardless of the number of days overdue.

type = "special collection"
overdue = 4

if type == "reference":
  fine = 0
elif type == "special collection":
  fine = overdue * 5
elif type == "regular":
  if overdue <= 7:
    fine = overdue * 1
  else:
    fine = overdue * 2

print(fine)


# Write a program that stores a person's order value and membership level (regular or premium). Then calculate a discount amount based on the following conditions:

# If the total order value is less than $50, there is no discount.
# If the total order value is between $50 and $100, the discount is 5% for regular customers and 10% for premium customers.
# If the total order value is greater than $100, the discount is 10% for regular customers and 15% for premium customers.

membership = input("What is your membership level? ")
total = int(input("What is the total cost of your order? "))

if total < 50:
  discount = total
elif total >= 50 and total <= 100:
  if membership == "regular":
    discount = total - (total * 0.05) 
  if membership == "premium":
    discount = total - (total * 0.1) 
else:
  if membership == "regular":
    discount = total - (total * 0.1) 
  if membership == "premium":
    discount = total - (total * 0.15) 

print(f"Your total after discount will be ${discount}")


# Write a Ruby program that stores the weight of a package and the destination (domestic or international). Then calculate the shipping fee based on the following conditions:

# If the destination is domestic:
# If the weight is less than or equal to 1 kg, the shipping fee is $5.
# If the weight is greater than 1 kg, the shipping fee is $10.
# If the destination is an international shipment:
# If the weight is less than or equal to 1 kg, the shipping fee is $15.
# If the weight is greater than 1 kg, the shipping fee is $25.

weight = float(input("What is the total weight of your package in kg? "))
destination = input("Is your destination domestic or international? ")

if destination == "domestic":
  if weight <= 1:
    fee = 5
  else:
    fee = 10
elif destination == "international":
  if weight <= 1:
    fee = 15
  else:
    fee = 25

print(f"Based on your input, the shipping fee for your package is ${fee} dollars.")