'''
test_question5.py

Unit tests for question 5.
'''

import unittest
import question5 as q

class TestQuestion5(unittest.TestCase):
    def test_start_vowel(self):
        '''
        Test word starting with vowel
        '''
        result = q.find_start('action')
        self.assertIsNone(result)
    
    def test_start_consonants(self):
        '''
        Test word starting with consonant
        '''
        result = q.find_start('banana')
        self.assertEqual(result, 1)
    
    def test_start_multiple_consonants(self):
        '''
        Test word starting with muliple consonants
        '''
        result = q.find_start('track')
        self.assertEqual(result, 2)

    def test_full_word(self):
        '''
        Test word starting with multiple consonants
        '''
        result = q.simple_pig_latin('track')
        self.assertEqual(result, 'acktray')
    



if __name__ == '__main__':
    unittest.main()