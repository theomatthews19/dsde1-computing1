'''
test_question4.py

Unit tests for question 4.
'''

import unittest
import question4 as q

class TestQuestion4(unittest.TestCase):
    def test_quad(self):
        '''
        Test hypotenuse calculated
        '''
        result = q.quad(2, -5, -3)
        self.assertEqual(result, (-0.5, 3))
    
    def test_negative(self):
        '''
        Test with negative roots
        '''
        result = q.positive_roots(2, -5, -3)
        self.assertFalse(result)
    
    def test_positive(self):
        '''
        Test with positive roots
        '''
        result = q.positive_roots(1, -6, 5)
        self.assertTrue(result)



if __name__ == '__main__':
    unittest.main()