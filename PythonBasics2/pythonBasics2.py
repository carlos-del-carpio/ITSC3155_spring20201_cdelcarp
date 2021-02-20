# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
  count = 0
  if (n > 0):
    for num in range(1, n + 1):
      if num % 3 == 0:
        count += 1

  return count


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  repeating_letter = ""
  repeating_count = 0
  current_letter = ""
  current_count = 0
  for letter in s:
    if repeating_letter == "":
      repeating_letter = letter
      repeating_count += 1
      current_letter = letter
      current_count + 1

    if letter == current_letter:
      current_count += 1
    else:
      if current_count >= repeating_count:
        repeating_letter = current_letter
        repeating_count = current_count
      current_letter = letter
      current_count = 1

    if current_count >= repeating_count:
      repeating_letter = current_letter
      repeating_count = current_count
  return repeating_letter


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  string = s.upper().replace(' ', '')

  for index in range(len(string)):
    if (string[index] != string[len(string) - 1 - index]):
      return False
  return True
