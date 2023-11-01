#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
from typing import List


# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        imin, imax, half_len = 0, m, (m + n + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i

            if self.shouldIncreaseI(i, m, nums1, nums2, j):
                imin = i + 1
            elif self.shouldDecreaseI(i, nums1, nums2, j):
                imax = i - 1
            else:
                max_of_left = self.calculateMaxOfLeft(i, j, nums1, nums2)
                if (m + n) % 2 == 1:
                    return max_of_left

                min_of_right = self.calculateMinOfRight(i, j, m, n, nums1, nums2)
                return (max_of_left + min_of_right) / 2

    def shouldIncreaseI(
        self, i: int, m: int, nums1: List[int], nums2: List[int], j: int
    ) -> bool:
        return i < m and nums2[j - 1] > nums1[i]

    def shouldDecreaseI(
        self, i: int, nums1: List[int], nums2: List[int], j: int
    ) -> bool:
        return i > 0 and nums1[i - 1] > nums2[j]

    def calculateMaxOfLeft(
        self, i: int, j: int, nums1: List[int], nums2: List[int]
    ) -> int:
        if i == 0:
            return nums2[j - 1]
        elif j == 0:
            return nums1[i - 1]
        else:
            return max(nums1[i - 1], nums2[j - 1])

    def calculateMinOfRight(
        self, i: int, j: int, m: int, n: int, nums1: List[int], nums2: List[int]
    ) -> int:
        if i == m:
            return nums2[j]
        elif j == n:
            return nums1[i]
        else:
            return min(nums1[i], nums2[j])


# @lc code=end
