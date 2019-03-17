from typing import List
from typing import Dict


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        storage: Dict[int, int] = {}
        answer: List[int] = [0, 1]

        for i, n in enumerate(nums):
            idx = storage.get(n)

            if idx is None:
                storage[target - n] = i
            else:
                answer = [idx, i]
                break

        return answer
