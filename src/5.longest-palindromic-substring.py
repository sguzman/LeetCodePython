#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = 0  # Start index of the longest palindrome found
        end = 0  # End index of the longest palindrome found

        for i in range(len(s)):
            # For odd length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1  # Correcting the overshoot
            if r - l > end - start:
                start, end = l, r

            # For even length palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1  # Correcting the overshoot
            if r - l > end - start:
                start, end = l, r

        return s[start:end]


# @lc code=end
