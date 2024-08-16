from code_86 import anti_shuffle

import unittest

def test():
    class TestAntiShuffle(unittest.TestCase):
        def test_anti_shuffle(self):
            self.assertEqual(anti_shuffle('Hi'), 'Hi')
            self.assertEqual(anti_shuffle('hello'), 'ehllo')
            self.assertEqual(anti_shuffle('Hello World!!!'), 'Hello !!!Wdlor')

    suite = unittest.TestLoader().loadTestsFromTestCase(TestAntiShuffle)
    unittest.TextTestRunner(verbosity=2).run(suite)

test()
