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