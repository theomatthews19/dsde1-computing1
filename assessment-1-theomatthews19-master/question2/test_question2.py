'''
test_question2.py

Unit tests for question 2.
'''

import unittest
import question2 as fc

class TestFlowchart(unittest.TestCase):
    def test_small_even(self):
        '''
        Test small even
        '''
        result = fc.flowchart(10)
        self.assertEqual(result, 'small-even')

    def test_small_odd(self):
        '''
        Test small odd
        '''
        result = fc.flowchart(15)
        self.assertEqual(result, 'small-odd')


    def test_medium_even(self):
        '''
        Test medium even
        '''
        result = fc.flowchart(60)
        self.assertEqual(result, 'medium-even')

    def test_medium_odd(self):
        '''
        Test medium odd
        '''
        result = fc.flowchart(75)
        self.assertEqual(result, 'medium-odd')
    
    def test_large_even(self):
        '''
        Test two valid number inputs
        '''
        result = fc.flowchart(110)
        self.assertEqual(result, 'large-even')

    def test_large_odd(self):
        '''
        Test two valid number inputs
        '''
        result = fc.flowchart(117)
        self.assertEqual(result, 'large-odd')


if __name__ == '__main__':
    unittest.main()