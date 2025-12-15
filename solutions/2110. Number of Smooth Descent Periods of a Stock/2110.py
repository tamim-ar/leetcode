class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        cur = 0
        for i in range(len(prices)):
            if i > 0 and prices[i] == prices[i - 1] - 1:
                cur += 1
            else:
                cur = 1
            ans += cur
        return ans
