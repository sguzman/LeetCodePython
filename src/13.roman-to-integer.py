#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#


# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        prev_value = 0
        for c in reversed(s):
            curr_value = roman_to_int[c]
            if curr_value < prev_value:
                result -= curr_value
            else:
                result += curr_value
            prev_value = curr_value
        return result


# @lc code=end
