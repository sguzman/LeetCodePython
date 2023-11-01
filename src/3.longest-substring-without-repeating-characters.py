#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used_chars = set()
        max_length = start = 0
        for end in range(len(s)):
            while s[end] in used_chars:
                used_chars.remove(s[start])
                start += 1
            used_chars.add(s[end])
            max_length = max(max_length, end - start + 1)
        return max_length


# @lc code=end
