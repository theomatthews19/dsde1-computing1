'''
test_question3.py

Unit tests for question 3.
'''

import unittest
import question3 as q

class TestQuestion3(unittest.TestCase):
    def test_hypot(self):
        '''
        Test hypotenuse calculated
        '''
        result = q.hypotenuse(3, 4)
        self.assertEqual(result, 5)
    
    def test_sentence(self):
        '''
        Test full sentence
        '''
        result = q.construct_hypot_sentence(3.6, 4.4)
        self.assertEqual(result, 'Given the sides 3.6 and 4.4, the hypotenuse is: 5.7')



if __name__ == '__main__':
    unittest.main()