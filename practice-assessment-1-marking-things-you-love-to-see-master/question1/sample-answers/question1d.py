'''
question1.py

Implementation of the flowchart in question1.png.
'''
# Defined the function
def flowchart(input_value):

# If input valu is zero, it returns 'zero' and function ends
    if input_value == 0:
        return 'zero'

# Otherwise, the function continues
    else:

# If input value is greater than zero, then it is determined,
# whether the value is even or odd, and then the answe is returned.
        if input_value > 0:
            if input_value % 2 == 0:
                return 'positive-even'
            else:
                return 'positive-odd'

# If input value is smaller than zero, then it is determined,
# whether the value is even or odd, and then the answe is returned.
        elif input_value < 0:
            if input_value % 2 == 0:
                return 'negative-even'
            else:
                return 'negative-odd'
