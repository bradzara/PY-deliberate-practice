#Swap the cases

string = "This is A RANdom stRiNG"

def swap_case(s):
  return s.swapcase()

print(swap_case(string))

# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

start = "This is a string"

def split_and_join(string):
  string = start.split(" ")
  string = "-".join(string)
  return string
print(split_and_join(string))

# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
# Hello firstname lastname! You just delved into python.

first = "John"
last = "Smith"

def print_full_name(first, last):
  return f"Hello {first} {last}! You just delved into python."

print(print_full_name(first, last))

# Read a given string, change the character at a given index and then print the modified string.

string = "abracadabra"
position = 5
character = "k"

def mutate_string(string, position, character):
  l = list(string)
  l[position] = character
  string = "".join(l)
  return string

print(mutate_string(string, position, character))