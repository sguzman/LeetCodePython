from typing import List


class Solution:
    def convert(self, s: str, n: int) -> str:
        store: List[str] = []
        if n is 1:
            return s

        if len(s) <= n:
            return s

        # First row
        i: int = 0
        while i < len(s):
            store.append(s[i])
            i = i + (2 * (n - 1))

        # Middle rows
        for j in range(1, n - 1):
            k: int = j
            column: bool = True
            column_to_diag_offset: int = 2 * (n - j - 1)
            diag_to_column_offset: int = 2 * j

            while k < len(s):
                store.append(s[k])
                if column:
                    k += column_to_diag_offset
                    column = False
                else:
                    k += diag_to_column_offset
                    column = True

        # Last row
        i = n - 1
        while i < len(s):
            store.append(s[i])
            i = i + (2 * (n - 1))

        return ''.join(store)
