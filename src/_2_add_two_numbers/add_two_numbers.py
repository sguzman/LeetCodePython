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

        while l1_idx is not None or l2_idx is not None:
            base_idx.next = ListNode(0)
            base_idx = base_idx.next

            local_sum = carry
            if l1_idx is not None:
                local_sum += l1_idx.val
                l1_idx = l1_idx.next
            if l2_idx is not None:
                local_sum += l2_idx.val
                l2_idx = l2_idx.next

            if local_sum > 9:
                carry = 1
                local_sum -= 10
            else:
                carry = 0

            base_idx.val = local_sum

        if carry == 1:
            base_idx.next = ListNode(1)

        return base.next
