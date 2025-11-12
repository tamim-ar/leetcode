from typing import List
import math

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        g_all = nums[0]
        for x in nums[1:]:
            g_all = math.gcd(g_all, x)
        if g_all != 1:
            return -1
        ones = nums.count(1)
        if ones > 0:
            return n - ones
        min_len = 10**9
        for i in range(n):
            g = nums[i]
            if g == 1:
                min_len = 1
                break
            for j in range(i + 1, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break
        return (min_len - 1) + (n - 1)
