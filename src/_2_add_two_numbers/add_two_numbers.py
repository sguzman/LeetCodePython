# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0

        base = ListNode(0)
        base_idx = base

        l1_idx = l1
        l2_idx = l2

        while l1_idx is not None and l2_idx is not None:
            local_sum = l1.val + l2.val + carry
            if local_sum > 9:
                carry = 1
                local_sum = local_sum - 10
            else:
                carry = 0
            base_idx.val = local_sum
            base_idx.next = ListNode(0)

            l1_idx = l1_idx.next
            l2_idx = l2_idx.next

        return base
