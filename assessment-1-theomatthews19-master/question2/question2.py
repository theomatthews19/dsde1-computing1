"""def flowchart(input_value):
    #user inputs value for code to check
    if input_value < 60:    # if input_value is less than 60
        if input_value % 2 == 0:    # checks if input_value is divisible by 2
            return "small-even"
        else:
            return "small-odd"
    
    elif input_value > 60 and input_value < 100:    # if input_value is more than 60 and less than 100
        if input_value % 2 == 0:    # checks if input_value is divisible by 2
            return "medium-even"
        else:
            return "medium-odd"
    
    else:     # if input_value is more than 100
        if input_value % 2 == 0:    # checks if input_value is divisible by 2
            return "large-even"
        else:
            return "large-odd" """

#model answer

def flowchart(input_value):
    """Return a string indicating
    if a number is small, medium, large,
    or even and odd"""

    if input_value<60:    # if input_value is less than 60
        if input_value % 2 == 0:    # checks if input_value is divisible by 2
            return "small-even"
        else:
            return "small-odd"
    
    elif input_value<100:    # if input_value is more than 60 and less than 100
        if input_value % 2 == 0:    # checks if input_value is divisible by 2
            return "medium-even"
        else:
            return "medium-odd"

    else:                        # if input_value is more than 100
        if input_value % 2 == 0:    # checks if input_value is divisible by 2
            return "large-even"
        else:
            return "large-odd"