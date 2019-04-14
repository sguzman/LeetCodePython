from typing import List


class Solution:
    @staticmethod
    def pre_process(s: str) -> str:
        s_new: List[str] = ["#"]
        for i in s:
            s_new.append(i)
            s_new.append("#")

        return ''.join(s_new)

    def longestPalindrome(self, s: str) -> str:
        table: List[int] = []
        new_string: str = Solution.pre_process(s)
        max_substr_idx: int = 0

        for i in range(len(new_string)):
            table.append(1)

            pre_idx: int = i - 1
            post_idx: int = i + 1

            while pre_idx > -1 and post_idx < len(new_string):
                if new_string[pre_idx] is new_string[post_idx]:
                    table[i] += 2

                    pre_idx -= 1
                    post_idx += 1
                else:
                    break

            if table[i] > table[max_substr_idx]:
                max_substr_idx = i

        half_idx: int = (table[max_substr_idx] - 1) // 2
        left_idx: int = max_substr_idx - half_idx
        right_idx: int = max_substr_idx + half_idx

        substr: str = new_string[left_idx:right_idx]
        cleaned_substr: str = substr.replace('#', '')

        return cleaned_substr
