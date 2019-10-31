'''
question1_solution.py

Corresponding solution file for question1.png from
Practice Assessment 1.


NOTE: This is only one possible solution, logically
equivalent ones also acceptable.

TOTAL POINTS AVAILABLE: 10 


Code Functionality (7)
7 points - all tests pass and code uses if/else structures in a 
Pythonic manner without relying on elements like pass or break

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

def flowchart(input_value):
    if input_value == 0:
        return 'zero'
    elif input_value > 0:
        if input_value%2:
            return 'positive-odd'
        else:
            return 'positive-even'
    else:
        if input_value%2:
            return 'negative-odd'
        else:
            return 'negative-even'

