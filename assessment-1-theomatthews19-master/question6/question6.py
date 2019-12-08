def list_of_dicts_empty(input_list):
    """Return True if list has only empty dictionaries, otherwise 
    return false"""
    # go through each dict in the list
    for dictionary in input_list:
    # determine if it is empty
    # if one isn't empty, return False 
        if dictionary != {}:
            return False

    # if none are empty, return True
    return True

def all_but_first_and_last(input_list):
    """Returns a list with the first and last values removed"""
    # use lsit slicing to return second item to penultimate item
    return input_list[1:-1]

def merge_sentences(sentence1, sentence2):
    """joins two strings, with the shorter string always being returned first"""
    # remove the leading and trailing whitespace
    sentence1 = sentence1.strip()
    sentence2 = sentence2.strip()
    # compare the length of the two sentences 
    # if sentence 1 shorter or equal to sentence 2
    if len(sentence1) <= len(sentence2):
        # return sentence 1 them sentence 2 
        return sentence1 + ' ' + sentence2
    # else return sentence 2 then sentence 1 
    # if the length of sentence1 is less than sentence2
    return sentence2 + ' ' + sentence1        

def upper_case(string):
    """returns string in upper case if there a 3 out of the first 5 letters as uppercase
    if not, will return the original string"""
    #create variable to count the number of uppercase letters
    count = 0
    for letter in string[0:5]:
        # if letter is uppercase
        if letter.isupper():
            # increment to my counter
            count += 1
    # if 3 uppercase letters in the string's first 5 letters
    if count >= 3:
        # return uppercase string
        return string.upper()

    # else return original string  
    return string

def key_longer(dictionary):
    """returns True if key length in dictionary is more than 3
    otherwise returns False"""
    # go through each key in the dictionary
    for key in dictionary.keys():
    # check if longer than 3 characters
        if len(key) > 3:
        # return true
            return True
    # else return False
    return False


def value_greater(dictionary):
    """checks if a value in dictionary is greater than 5"""
    # go through each value in the dictionary
    for val in dictionary.values():
    # check if greater than 5
        if val > 5:
        # return true
            return True
    # else return False
    return False


def shape_colour(shape = "circle", colour = "black"):
    """returns a sentence with the parameters "shape" and "colour" inserted
    default colour is set to "circle" (for shape) and "black" for colour
    if colour is none, will read "colour" as "colourless"."""
    #if colour is None
    if colour is None:  
        return "Shape {} is colourless.".format(shape)
    # else use default values, return string
    return "Shape {} has colour {}".format(shape, colour)                              