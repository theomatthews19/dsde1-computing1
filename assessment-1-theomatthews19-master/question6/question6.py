def list_of_dicts_empty(input_list):
    """checks if all dictionaries in list_of_dicts_empty are empty"""
    all_empty = True             
    for i in input_list:
        if i:
            all_empty = False


def all_but_first_and_last(input_list):
    """Returns a list with the first and last values removed"""
    input_list = []
    return input_list[1:-1]   #returns values from the second in the list to the penultimate value


def merge_sentences(sentence1, sentence2):
    """joins two strings, with the shorter string always being returned first"""
    string = ()
    if len(sentence1) < len(sentence2):     # if the length of sentence1 is less than sentence2
        return string.join((sentence1, sentence2))        # join sentences in specific order
    else:                                                  # if the length of sentence1 is greater than sentence2
        return string.join((sentence2, sentence1))        # join sentences in specific order


def upper_case(string):
    """returns string in upper case if there a 3 out of the first 5 letters as uppercase
    if not, will return the original string"""
    number_of_upper = 0         # sets initial number of uppercase letters to 0
    for char in string[:5]:         # for the first 5 characters in the string
        if char.upper == char:      # sets char = uppercase
            number_of_upper += 1        
    if number_of_upper >= 3:        # if number of uppercase letters is greater than or equal to 3
        return string.upper()        # returns the string in ALL uppercase
    else:
        return string.lower()          #otherwise, returns string in ALL lovercase


def key_longer(dictionary):
    """returns True if key length in dictionary is more than 3
    otherwise returns False"""
    for i in dictionary():                     # any word in the dictionary
        if len(dictionary.key(i)) > 3:             # if it's length is greater than 3
            return True                         #return True 
        else:
            return False


def value_greater(dictionary):
    """checks if a value in dictionary is greater than 5"""
    for i in dictionary():
        if i > 5:               # if the value in the dictionary is greater than 5
            return True         # return true 
        else:
            return False


def shape_colour(shape = "circle", colour = "black"):
    """returns a sentence with the parameters "shape" and "colour" inserted
    default colour is set to "circle" (for shape) and "black" for colour
    if colour is none, will read "colour" as "colourless"."""
    if colour != None:                                  # if colour is not equal to nothing
        return "The {shape} has colour {colour}."       # return printed sentence
    else:
        colour = "colourless"                            # if colour = none, 
                                                        # print colourless instead