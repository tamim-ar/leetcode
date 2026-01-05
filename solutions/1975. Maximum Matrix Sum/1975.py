class Solution:
    def maxMatrixSum(self, matrix):
        total = 0
        neg = 0
        mn = 10**18
        for r in matrix:
            for x in r:
                if x < 0:
                    neg += 1
                total += abs(x)
                mn = min(mn, abs(x))
        return total if neg % 2 == 0 else total - 2 * mn
