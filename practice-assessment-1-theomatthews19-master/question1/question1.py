'''
question1.py

Implementation of the flowchart in question1.png.
'''

def flowchart(input_value):
    if input_value == 0:
        return 0
    elif input_value > 0:
        if input_value % 2 == 0:
            return "positive-even"
        else:
            return "positive-odd"
            
"""asks if is divisible by 2"""
    elif input_value % 2 < 0:
        if input_value % 2 == 0:
            return "negative-even"
        else:
            return "negative-odd"