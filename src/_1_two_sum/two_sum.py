from typing import List
from typing import Dict


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        storage: Dict[int, int] = {}
        answer: List[int] = [0, 1]

        for i, n in enumerate(nums):
            diff = target - n
            idx = storage.get(diff)

            if idx is None:
                storage[diff] = i
            else:
                answer = [idx, i]
                break

        return answer
