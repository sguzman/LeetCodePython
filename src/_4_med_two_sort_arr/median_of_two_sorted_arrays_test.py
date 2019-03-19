import unittest
from _4_med_two_sort_arr import median_of_two_sorted_arrays


class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = median_of_two_sorted_arrays.Solution()
        nums1 = [1, 3]
        nums2 = [2]

        output = 2
        actual = solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(output, actual)

    def test_2(self):
        solution = median_of_two_sorted_arrays.Solution()
        nums1 = [1, 2]
        nums2 = [3, 4]

        output = 2.5
        actual = solution.findMedianSortedArrays(nums1, nums2)
        self.assertEqual(output, actual)



if __name__ == '__main__':
    unittest.main()
