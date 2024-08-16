from code_111 import histogram
def test_histogram(self):
    self.assertEqual(histogram('a b c'), {'a': 1, 'b': 1, 'c': 1})
    self.assertEqual(histogram('a b b a'), {'a': 2, 'b': 2})
    self.assertEqual(histogram('a b c a b'), {'a': 2, 'b': 2})
    self.assertEqual(histogram('b b b b a'), {'b': 4})
    self.assertEqual(histogram(''), {})