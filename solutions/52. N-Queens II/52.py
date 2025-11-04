class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        cols = set()
        posDiag = set()
        negDiag = set()

        def backtrack(r):
            nonlocal count
            if r == n:
                count += 1
                return
            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                backtrack(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)
        return count
