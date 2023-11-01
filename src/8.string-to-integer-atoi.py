#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#


# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # Step 1: Ignore leading whitespaces
        if not s:
            return 0

        # Step 2: Check for the optional sign
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            sign = 1
            s = s[1:]
        else:
            sign = 1

        # Step 3: Read in the digits and ignore the rest
        i = 0
        while i < len(s) and s[i].isdigit():
            i += 1
        num = s[:i]

        # Step 4: Convert the digits to an integer
        if not num:
            return 0
        num = int(num) * sign

        # Step 5: Handle integer overflow
        num = max(min(num, 2**31 - 1), -(2**31))

        # Step 6: Return the integer
        return num


# @lc code=end
