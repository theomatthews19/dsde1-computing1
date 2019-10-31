'''
question1.py

Implementation of the flowchart in question1.png.
'''
def flowchart(input_value):
    #if the value is equal to zero, returns zero
    if input_value == 0:
        return 'zero'
    else:
        #asks if positive or negtive
        if input_value > 0:
            #if the value is bigger than zero and even, returns positive-even
            if input_value % 2 == 0:
                return 'positive-even'
            else:
                #if the value is bigger than zero and odd, returns positive-odd
                if input_value % 2 == 1:
                    return 'positive-odd'
        else:
            if input_value < 0:
                #if the value is smaller than zero and even, returns negative-even
                if input_value % 2 == 0:
                    return 'negative-even'
                #if the value is smaller than zero and odd, returns negative-odd
                else:
                    if input_value % (-2) == (-1):
                        return 'negative-odd'