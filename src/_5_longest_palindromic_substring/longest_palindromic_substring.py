from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        total_len = 2 * len(s) - 1
        lens: List[int] = []

        for i in range(total_len):
            if i % 2 == 0:
                lens += [1]
            else:
                lens += [0]

        for i in range(total_len):
            if i % 2 == 0:
                pre_idx = i - 1
                post_idx = i + 1

                while pre_idx > -1 and post_idx < total_len:
                    if s[pre_idx] == s[pre_idx]:
                        lens[i] += 1

                        pre_idx -= 1
                        post_idx += 1
                    else:
                        break

        return s
