import unittest
from .parentheses import is_valid_parentheses


class TestIsValidParentheses(unittest.TestCase):
    def test_valid_strings(self):
        self.assertTrue(is_valid_parentheses("()"))
        self.assertTrue(is_valid_parentheses("[()]"))
        self.assertTrue(is_valid_parentheses("{([])}"))
        self.assertTrue(is_valid_parentheses("asd{qe 12([ AD]_)@)}@$"))
        self.assertTrue(is_valid_parentheses("{(ad[ad aawd]qwe)q}r"))

    def test_invalid_strings(self):
        self.assertFalse(is_valid_parentheses(""))
        self.assertFalse(is_valid_parentheses("123"))
        self.assertFalse(is_valid_parentheses("asldkaskdj*&@#!__"))

    def test_invalid_indices(self):
        self.assertEqual(is_valid_parentheses("(]"), [0, 1])
        self.assertEqual(is_valid_parentheses("[(])"), [0, 1, 2, 3])
        self.assertEqual(is_valid_parentheses("{[}"), [0, 1, 2])
        self.assertEqual(is_valid_parentheses("asd][asd]ddd((a)dd)"), [3, 4, 8, 12, 13, 15, 18])
        self.assertEqual(is_valid_parentheses("[asd][a{}sd]d{dd((a)d}d)"),
                         [0, 4, 5, 7, 8, 11, 13, 16, 17, 19, 21, 23])


if __name__ == '__main__':
    unittest.main()
