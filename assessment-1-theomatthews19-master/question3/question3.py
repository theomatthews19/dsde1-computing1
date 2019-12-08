'''
question3.py

Fix the errors so that this code runs when called
from the commandline.

TOTAL POINTS AVAILABLE: 5 


Code Functionality (5)
5 points - no errors remain and code runs
3 points - only 1 error remains
1 point - multiple errors remain
0 points - all original errors remain or new ones introduced
'''
import math

def hypotenuse(side_a, side_b):
    '''Calcuates the hypotenuse given two sides of a triangle'''
    # c^2 = a^2 + b^2
    square_sum = (side_a * side_a) + (side_b * side_b)
    
    # return the square root
    return math.sqrt(square_sum)



def construct_hypot_sentence(side_a, side_b):
    '''Return a string with the three sides of a right triangle computed.'''

    # calculate the hypotenuse of the triangle
    hypot = hypotenuse(side_a, side_b)

    # put together and return the string
    sentence = 'Given the sides {:1.1f} and {:1.1f}, the hypotenuse is: {:1.1f}'.format(side_a, side_b, hypot)
    return sentence


