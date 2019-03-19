from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen: Dict[str, int] = {}
        global_sum: int = 0
        start_idx: int = 0

        for i, c in enumerate(s):
            if last_seen.get(c) is None or start_idx > last_seen[c]:
                global_sum = max(i - start_idx + 1, global_sum)
            elif start_idx <= last_seen[c]:
                start_idx = last_seen[c] + 1

            last_seen[c] = i

        return global_sum
