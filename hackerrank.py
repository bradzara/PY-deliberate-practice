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

# Output the integer number indicating the total number of occurrences of the substring in the original string.

string = "ABCDCDC"
substring = "CDC"

def count_substring(string, substring):
    count = 0
    sub_len = len(substring)
    for i in range(len(string) - sub_len + 1):
        if string[i:i + sub_len] == substring:
            count += 1
    return count

print(count_substring(string, substring))

# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

n = 5
arr = [2, 3, 6, 6, 5]

unique_scores = list(set(arr))
unique_scores.sort(reverse=True)

runner_up_score = unique_scores[1]
print(runner_up_score)


# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

s = "qA2"

print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))


number = int(input("Enter a number: "))

def increment_or_reset(n):
    if 0 <= n <= 8:
        return n + 1
    elif n == 9:
        return 0
    else:
        return -1
    
print(increment_or_reset(5))