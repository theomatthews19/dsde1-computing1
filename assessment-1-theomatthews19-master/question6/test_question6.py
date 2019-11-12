'''
test_question6.py

Unit tests for question6 functions.
'''


import unittest
import unittest.mock
import io

import question6 as q

class TestStructures(unittest.TestCase):
    def set_up(self):
        pass


    def test_list_of_dicts_empty1(self):
        '''
        Test empty
        '''
        result = q.list_of_dicts_empty([{}, {}, {}])
        self.assertIs(result, True)

    def test_list_of_dicts_empty2(self):
        '''
        Test only one empty
        '''
        result = q.list_of_dicts_empty([{}, {'a': 1}, {}])
        self.assertIs(result, False)

    def test_all_but_first_and_last(self):
        '''
        Test with list
        '''
        result = q.all_but_first_and_last([2,3,4,5,6,7,8])
        self.assertEqual(result, [3,4,5,6,7])

    def test_merge_sentences1(self):
        '''
        Test merging two strings of same length
        '''
        result = q.merge_sentences("Sentence 1.", "Sentence 2.")
        self.assertEqual(result, "Sentence 1. Sentence 2.")

    def test_merge_sentences2(self):
        '''
        Test merge with strings of different length
        '''
        result = q.merge_sentences("Sentence 1.", "Sent 2.")
        self.assertEqual(result, "Sent 2. Sentence 1.")

    def test_merge_sentences3(self):
        '''
        Test merge with strings of different length
        '''
        result = q.merge_sentences("     Sent 1.       ", " Sentence 2. ")
        self.assertEqual(result, "Sent 1. Sentence 2.")

    def test_upper_case1(self):
        '''
        Test with not enough upper case letters
        '''
        result = q.upper_case('PytHon_test')
        self.assertEqual(result, 'PytHon_test')

    def test_upper_case2(self):
        '''
        Test with enough upper case letters
        '''
        result = q.upper_case('PyTHon_test')
        self.assertEqual(result, 'PYTHON_TEST')

    def test_key_longer1(self):
        '''
        Test with no longer key
        '''
        result = q.key_longer({'ab': 1, 'abc': 2, 'c': 3})
        self.assertIs(result, False)

    def test_key_longer2(self):
        '''
        Test with longer key
        '''
        result = q.key_longer({'ab': 1, 'abcd': 2, 'c': 3})
        self.assertIs(result, True)

    def test_value_greater1(self):
        '''
        Test without greater value
        '''
        result = q.value_greater({'ab': 1, 'abc': 2, 'c': 3})
        self.assertIs(result, False)

    def test_value_greater2(self):
        '''
        Test with greater value
        '''
        result = q.value_greater({'ab': 1, 'abc': 2, 'c': 7})
        self.assertIs(result, True)

    def test_shape_colour1(self):
        '''
        Test without arguments
        '''
        result = q.shape_colour()
        self.assertEqual(result, 'Shape circle has colour black.')

    def test_shape_colour2(self):
        '''
        Test with two arguments
        '''
        result = q.shape_colour('square', 'red')
        self.assertEqual(result, 'Shape square has colour red.')

    def test_shape_colour3(self):
        '''
        Test with one argument and None
        '''
        result = q.shape_colour('square', None)
        self.assertEqual(result, 'Shape square is colourless.')



if __name__ == '__main__':
    unittest.main()
