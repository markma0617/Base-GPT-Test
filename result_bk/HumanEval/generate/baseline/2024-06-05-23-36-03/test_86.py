from code_86 import anti_shuffle

import unittest

def test():
    class TestAntiShuffle(unittest.TestCase):
        
        def test_single_word(self):
            self.assertEqual(anti_shuffle('Hi'), 'Hi')
        
        def test_single_word_sorted(self):
            self.assertEqual(anti_shuffle('hello'), 'ehllo')
        
        def test_multiple_words_sorted(self):
            self.assertEqual(anti_shuffle('Hello World!!!'), 'Hello !!!Wdlor')
    
    return TestAntiShuffle
