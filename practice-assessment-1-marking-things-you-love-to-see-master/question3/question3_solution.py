'''
question3_solution.py

Solution for question3.py in Practice Assesment 1.

TOTAL POINTS AVAILABLE: 5 


Code Functionality (5)
5 points - no errors remain and code runs
3 points - only 1 error remains
1 point - multiple errors remain
0 points - all original errors remain or new ones introduced

'''

def count_words(input_string):
    '''Counts the number of words between spaces'''
    # create a list of each word
    words = input_string.split()
    # return the length of the list
    return len(words)



def main():
    '''Main function to be run first.'''

    my_string = 'Imperial College London'

    # count number of words in string
    num_words = count_words(my_string)

    # print how many words were counted
    print('There are {} words in the string:'.format(num_words))
    print(my_string)

if __name__ == '__main__':
    main()
