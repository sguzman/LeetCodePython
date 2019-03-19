import unittest
from _2_add_two_numbers import add_two_numbers


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyTestCase(unittest.TestCase):
    def test_1(self):
        input_1 = ListNode(2)
        input_1.next = ListNode(4)
        input_1.next.next = ListNode(3)

        input_2 = ListNode(5)
        input_2.next = ListNode(6)
        input_2.next.next = ListNode(4)

        expected = ListNode(7)
        expected.next = ListNode(0)
        expected.next.next = ListNode(8)

        actual = add_two_numbers.Solution.addTwoNumbers(input_1, input_2)

        self.assertEqual(expected.val, actual.val)
        self.assertEqual(expected.next.val, actual.next.val)
        self.assertEqual(expected.next.next.val, actual.next.next.val)


if __name__ == '__main__':
    unittest.main()
