'''
question5.py

Simple functions performing operations on basic Python data structures.
'''

# Lists

# Write a function that merges two lists together only if the length of both
# lists is greater than 4. Otherwise return an empty list.
def merge_list(list1, list2):
    '''a function that merges two lists together only if the length of both
    lists is greater than 4. Otherwise return an empty list. '''
    if len(list1) > 4 and len(list2) > 4:
        list3 = list1 + list2
        return list3
    else:
        return []

# Write a function that returns a list containing unique values from the input_list.
# In other words, any repeated values are removed.
def unique_values(input_list):
    '''a function that returns a list containing unique values from the input_list.'''
    output_list = list(set(input_list))
    return output_list

# Strings

# Write a function that returns a string where first "x" characters are lower
# case. "x" is passed as the second parameter.
def start_to_lower(string, x):
    '''a function that returns a string where first "x" characters are lowercase.
    "x" is passed as the second parameter.'''
    first_part = string[:x]
    second_part = string[x:]
    return first_part.lower() + second_part

# Write a function that returns the character which first occurs for the second
# time in the string. For example in string "abcdefcab" the character "c"
# occurs twice first. If no character occurs more than once, an empty string
# should be returned.
def first_double_char(string):
    '''a function that returns the character which first occurs for the second
    time in the string. If no character occurs more than once,
    an empty string should be returned.'''
    duplicates = []
    for i in string:
        if i in duplicates:
            return i
        else:
            duplicates.insert(0, i)
    return []
# Dictionaries

# Write function that returns a sum of all values stored in the dictionary.
def sum_of_dict(dictionary):
    '''function that returns a sum of all values stored in the dictionary.'''
    return sum(dictionary.values())

# Write a function that returns a new dictionary where each value is multiplied
# by 3. Example: for input dictionary {'a': 1, 'b': 2, 'c': 3} the returned
# dictionary will be {'a': 3, 'b': 6, 'c': 9}
def multiply_dict(dictionary):
    '''a function that returns a new dictionary where each value is multiplied by 3.'''
    new_dictionary = {}
    for key in dictionary:
        new_dictionary[key] = dictionary[key] * 3
    return new_dictionary

# Arguments


# Write a function with the first argument mandatory and the second optional.
# The first argument accepts a list as an argument, the second accepts two
# strings "max" or "min". The function returns either the maximum or the
# minimum value from the list. The default operation is "max". If the operation
# is neither "max" nor "min" the function should return "None" (the value, not
# the string).
def max_min(input_list, operation="max"):
    '''a function with the first argument mandatory and the second optional.
    The first argument accepts a list as an argument, the second accepts two
    strings "max" or "min". The function returns either the maximum or the
    minimum value from the list. The default operation is "max". If the operation
    is neither "max" nor "min" the function should return "None"'''
    if operation == "max":
        no_integers = [i for i in input_list if not isinstance(i, int)]
        all_integers = [i for i in input_list if i not in no_integers]
        return max(all_integers)
    elif operation == "min":
        no_integers = [i for i in input_list if not isinstance(i, int)]
        all_integers = [i for i in input_list if i not in no_integers]
        return min(all_integers)
    else:
        return
