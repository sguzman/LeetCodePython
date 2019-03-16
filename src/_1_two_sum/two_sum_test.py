import unittest
from _1_two_sum import two_sum


class MyTestCase(unittest.TestCase):
    def test_1(self):
        input_1 = [2, 7, 11, 15]
        input_2 = 9

        output = two_sum.Solution.twoSum(input_1, input_2)
        answer = [0, 1]

        self.assertListEqual(output, answer)


if __name__ == '__main__':
    unittest.main()
