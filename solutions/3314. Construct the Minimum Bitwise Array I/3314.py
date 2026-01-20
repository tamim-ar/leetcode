class Solution:
    def minBitwiseArray(self, nums):
        ans = []
        for x in nums:
            if x & 1 == 0:
                ans.append(-1)
            else:
                k = 0
                while (x >> k) & 1:
                    k += 1
                ans.append(x - (1 << (k - 1)))
        return ans
