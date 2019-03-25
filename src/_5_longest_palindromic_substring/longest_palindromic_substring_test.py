import unittest
from _5_longest_palindromic_substring import longest_palindromic_substring


class MyTestCase(unittest.TestCase):
    def test1(self):
        sol = longest_palindromic_substring.Solution()
        input1 = "babad"
        output = "bab"

        actual = sol.longestPalindrome(input1)
        self.assertEqual(output, actual)

    def test2(self):
        sol = longest_palindromic_substring.Solution()
        input1 = "cbbd"
        output = "bb"

        actual = sol.longestPalindrome(input1)
        self.assertEqual(output, actual)


if __name__ == '__main__':
    unittest.main()
