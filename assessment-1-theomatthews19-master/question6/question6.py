'''
question5.py

Simple functions performing operations on basic Python data structures.
'''

# Lists

# Write a function that checks if all dictionaries in a list are empty or not.
# return True if all dictionaries are empty, False otherwise
def list_of_dicts_empty(input_list):
    all_empty = True
    for i in input_list:
        if i:
            all_empty = False

# Write a function that returns a list containig all but the first and the last
# element of "the_list". 
# example: the_list = [1,2,3,4,5,6]
# returns [2,3,4,5]
def all_but_first_and_last(input_list):
    del all_but_first_and_last[0]
    del all_but_first_and_last[-1]
    return all_but_first_and_last



# Strings

# Write a function that concatenates two sentences passed as parameters. The
# returned string contains the shorter sentence first. There is exactly one space 
# between the fullstop of the first sentence and the beginning of the second 
# sentence. All whitespace at the beginning and end of the sentences passed as 
# parameters should be ignored and not include in the length of the sentence (when
# determining which sentence should go first).
def merge_sentences(sentence1, sentence2):
    if len(sentence1) < len(sentence2):
        merge_sentences.join((sentence1, sentence2))
    else:
        merge_sentences.join((sentence2, sentence1))

    return merge_sentences

# Write a function that returns the string in upper case if there are at least
# 3 uppercase letters in the first 5 letters of the string. If there are not 
# at least 3 uppercase letters in the first 5 letters of the string, return the
# original string.
def upper_case(string):
    number_of_upper = 0
    for char in string[:5]:
        if char.upper == char:
            number_of_upper += 1
    if number_of_upper >= 3:
        return string.upper()
    else:
        return string.lower()

# Dictionaries

# Write a function that checks whether there is a key in the dictionary whose
# length is > 3. Function returns True or False.
def key_longer(dictionary):
    for i in dictionary():
        if len(dictionary.key(i)) > 3:
            return True
        else:
            return False

# Write function that checks whether there is a value in the dictionary greater
# than 5. Function returns True or False
def value_greater(dictionary):


# Parameters

# Write a function with two parameters "shape" and "colour". The function
# should return text "The {shape} has colour {coulour}." The default shape
# should be "circle" and the default colour should be "black". If the parameter
# colour is None then the text should read as "Shape {shape} is colourless."
def shape_colour():


