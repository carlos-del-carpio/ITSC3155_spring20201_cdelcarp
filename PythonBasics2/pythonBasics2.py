# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


#Part A (count_threes) now needs to return the multiple of three that occurs the most in a string.
# For example, 0939639 would return 9 since it appeared 3 times while the other multiple of three appeared less than that.
# You only need to worry about single digit multiples of 3 (3, 6, 9). You must use a dictionary to accomplish this.

def count_threes(n):
    dictionary = {}
    highest_count = 0
    returnNum = ""

    for num in n:
        if int(num) % 3 == 0:
            if num not in dictionary:
                dictionary[num] = 0
            dictionary[num] += 1

    for key in dictionary:
        if dictionary[key] > highest_count:
            highest_count = dictionary[key]
            returnNum = key

    return int(returnNum)


#Part B (longest_consecutive_repeating_char) now needs to account for the edge case where two characters have the same
# consecutive repeat length. The return value should now be a list containing all characters with the longest
# consecutive repeat. For example, the longest_consecutive_repeating_char('aabbccd') would return ['a', 'b', 'c']
# (order doesn't matter). You must use a dictionary to accomplish this.

def longest_consecutive_repeating_char(s):
    dictionary = {}
    returning_list = []
    previous_letter = ""

    for letter in s:
        if letter == previous_letter:
            dictionary[letter] += 1
        elif letter not in dictionary:
            dictionary[letter] = 1

        previous_letter = letter

    all_values = dictionary.values()
    max_value = max(all_values)

    for key in dictionary:
        if dictionary[key] == max_value:
            returning_list.append(key)

    return returning_list


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
