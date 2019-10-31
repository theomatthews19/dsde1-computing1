'''
question1.py

Implementation of the flowchart in question1.png.
'''

def flowchart(input_value):
    '''q1'''
    if input_value == 0:
        return 'zero'
    else:
        if input_value > 0:
            if input_value%2 == 0:
                return 'positive-even'
            else:
                return 'positive-odd'
        else:
            if input_value%2 == 0:
                return 'negative-even'
            else:
                return 'negative-odd'



