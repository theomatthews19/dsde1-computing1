import math
def period(L, g):
    T=''
    try:
        T = 2 * math.pi * math.sqrt(L/g)
    except TypeError or ValueError or ZeroDivisionError:
        print("you did not enter a number")