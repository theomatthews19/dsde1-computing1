'''
question1.py

Implementation of the flowchart in question1.png.
'''

def flowchart(input_value):
    '''Describes the flowchart.'''
    if input_value == 0:
        return 'zero'
    if input_value > 0:
        if (input_value % 2) == 0:
            return 'positive-even'
        return 'positive-odd'
    if (input_value % 2) == 0:
        return 'negative- even'
    return 'negative-odd'
