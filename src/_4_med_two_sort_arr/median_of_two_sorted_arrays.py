class Solution:
    def findMedianSortedArrays(self, A, B):
        total_len = len(A) + len(B)
        len_half = total_len // 2

        if total_len % 2 == 1:
            return self.kth(A, B, len_half)
        else:
            return (self.kth(A, B, len_half) + self.kth(A, B, len_half - 1)) / 2.

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]

        a_half, b_half = len(a) // 2, len(b) // 2
        a_med, b_med = a[a_half], b[b_half]

        # when k is bigger than the sum of a and b's median indices
        if a_half + b_half < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if a_med > b_med:
                return self.kth(a, b[b_half + 1:], k - b_half - 1)
            else:
                return self.kth(a[a_half + 1:], b, k - a_half - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if a_med > b_med:
                return self.kth(a[:a_half], b, k)
            else:
                return self.kth(a, b[:b_half], k)

