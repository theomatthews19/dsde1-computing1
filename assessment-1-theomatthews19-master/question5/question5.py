'''
question5.py

Fix the errors so that this code runs when called
from the commandline.

TOTAL POINTS AVAILABLE: 5 


Code Functionality (5)
5 points - no errors remain and code runs
3 points - only 1 error remains
1 point - multiple errors remain
0 points - all original errors remain or new ones introduced

'''
def find_start(word):
    ''' '''
    
    # all vowels
    vowels = ('a', 'e', 'i', 'o' , 'u')

    # check if starts with a vowel
    if word[0] in vowels:
        # return an empty string
        return None

    # if doesn't start with a vowel
    # go through each character 
    # (save character in ch and index in i)
    for i, ch in enumerate(word):
        # letter is a vowel
        if ch in vowels:
            # return index of first vowel
            return i
    
def simple_pig_latin(word):
    '''Takes any word and returns a simple translation
       of that word in Pig Latin'''
    # word ending
    tail = 'ay'

    # find when pig latin word should start
    start = find_Start(word)
    
    # if didn't start with a vowel
    if start is not None:
        return word[start::] + word[:start] + tail
    
    # otherwise it did start with a vowel
    return word + tail

