'''
question5_solutions.py

Simple functions performing operations on basic Python data structures.

TOTAL POINTS AVAILABLE: 70 (10 per function) 


Code Functionality (7)
7 points - all tests pass and code uses if/else, for structures in a 
Pythonic manner without relying on elements like pass or break or 
range() unnecessarily

5-6 points - all tests pass, but code could be significantly 
improved to be more Pythonic

3-4 points - at least one test fails, but code would work with small
changes

1-2 points - no test passes and effort has been made to answer question 
but would need significant changes/additions to function correctly

0 points - no effort made to answer question



Code Readability (3)
3 points - Well commented, clear code where PyLint returns no or 
few errors (error related to removing else/elif can be ignored)

1-2 points - Some issues related to issues such as variable names
could be improved 

0 points - multiple and repeated significant style issues, code very 
difficult to understand

'''

# Lists

# Write a function that merges two lists together only if the length of both
# lists is greater than 4. Otherwise return an empty list.
def merge_list(list1, list2):
    if len(list1) > 4 and len(list2) > 4:
        return list1 + list2

    return []

# Write a function that returns a list containing unique values from the input_list.
# In other words, any repeated values are removed.
def unique_values(input_list):
    return list(set(input_list))


# Strings

# Write a function that returns a string where first "x" characters are lower
# case. "x" is passed as the second parameter.  
def start_to_lower(string, x):
    return string[:x].lower() + string[x:]

# Write a function that returns the character which first occurs for the second
# time in the string. For example in string "abcdefcab" the character "c"
# occurs twice first. If no character occurs more than once, an empty string
# should be returned. 
def first_double_char(string):
    chars = []
    for c in string:
        if c in chars:
            return c
        else:
            chars.append(c)

    return ""


# Dictionaries

# Write function that returns a sum of all values stored in the dictionary.
def sum_of_dict(dictionary):
    return sum(dictionary.values())

# Write a function that returns a new dictionary where each value is multiplied
# by 3. Example: for input dictionary {'a': 1, 'b': 2, 'c': 3} the returned
# dictionary will be {'a': 3, 'b': 6, 'c': 9}
def multiply_dict(dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        new_dict[key] = value * 3
    return new_dict


# Arguments


# Write a function with the first argument mandatory and the second optional.
# The first argument accepts a list as an argument, the second accepts two
# strings "max" or "min". The function returns either the maximum or the
# minimum value from the list. The default operation is "max". If the operation
# is neither "max" nor "min" the function should return "None" (the value, not
# the string).
def max_min(input_list, operation = 'max'):
    if operation == 'max':
        return max(input_list)
    elif operation == 'min':
        return min(input_list)
    else:
        return None
