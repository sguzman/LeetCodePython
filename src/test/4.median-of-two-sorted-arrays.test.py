#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
from typing import List


# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # If nums1 is larger than nums2, swap them
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # Get the lengths of the two lists
        m, n = len(nums1), len(nums2)
        # Calculate the start and end of the binary search range, and the half length of the combined lists
        imin, imax, half_len = 0, m, (m + n + 1) // 2

        # Start binary search
        while imin <= imax:
            # Calculate the partition points in nums1 and nums2
            i = (imin + imax) // 2
            j = half_len - i

            # If the partition point in nums1 needs to be increased
            if self.shouldIncreaseI(i, m, nums1, nums2, j):
                imin = i + 1
            # If the partition point in nums1 needs to be decreased
            elif self.shouldDecreaseI(i, nums1, nums2, j):
                imax = i - 1
            else:
                # Calculate the maximum element of the left partition
                max_of_left = self.calculateMaxOfLeft(i, j, nums1, nums2)
                # If the combined length of the lists is odd, return the maximum element of the left partition as the median
                if (m + n) % 2 == 1:
                    return max_of_left

                # Calculate the minimum element of the right partition
                min_of_right = self.calculateMinOfRight(i, j, m, n, nums1, nums2)
                # If the combined length of the lists is even, return the average of the maximum element of the left partition and the minimum element of the right partition as the median
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
if __name__ == "__main__":
    # begin
    s = Solution()
    print(s.findMedianSortedArrays([1, 3], [2]))
    print(s.findMedianSortedArrays([1, 2], [3, 4]))
    print(s.findMedianSortedArrays([0, 0], [0, 0]))
