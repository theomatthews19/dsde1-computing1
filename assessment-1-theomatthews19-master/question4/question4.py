'''
question4.py

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

def quad(a, b, c):
    '''Applies quadratic formula to a, b, and c to return the roots.'''
    # x = (-b +- sqrt(b^2 + 4ac)) / 2a
    sq = math.sqrt((b * b) - (4 * a * c))
    x0 = (-b - sq)/(2*a)
    x1 = (-b + sq)/(2*a)

    # return the zeroes
    return (x0, x1)



def positive_roots(a, b, c):
    '''Returns True or False for if the roots of the quadratric 
       equation are both positive.

       ax^2 + bx + c = 0'''

    # apply the quadratic formula
    roots = quad(a, b, c)

    # check if both roots are positive
    if roots[0]>0 and roots[1]>0:
        return True

    return