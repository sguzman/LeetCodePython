import unittest
from _3_long_rep_wo_rep import longest_substring_without_repeating_characters


class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = longest_substring_without_repeating_characters.Solution()

        input_1: str = "abcabcbb"
        output: int = 3
        actual: int = solution.lengthOfLongestSubstring(input_1)

        self.assertEqual(output, actual)

    def test_2(self):
        solution = longest_substring_without_repeating_characters.Solution()

        input_1: str = "bbbbb"
        output: int = 1
        actual: int = solution.lengthOfLongestSubstring(input_1)

        self.assertEqual(output, actual)

    def test_3(self):
        solution = longest_substring_without_repeating_characters.Solution()

        input_1: str = "pwwkew"
        output: int = 3
        actual: int = solution.lengthOfLongestSubstring(input_1)

        self.assertEqual(output, actual)

    def test_4(self):
        solution = longest_substring_without_repeating_characters.Solution()

        input_1: str = "tmmzuxt"
        output: int = 5
        actual: int = solution.lengthOfLongestSubstring(input_1)

        self.assertEqual(output, actual)

    def test_5(self):
        solution = longest_substring_without_repeating_characters.Solution()

        input_1: str = "bbtablud"
        output: int = 6
        actual: int = solution.lengthOfLongestSubstring(input_1)

        self.assertEqual(output, actual)


if __name__ == '__main__':
    unittest.main()
