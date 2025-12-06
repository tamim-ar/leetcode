import collections
from typing import List

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7

        dp = [0] * (n + 1)
        dp[0] = 1
        
        prefix_sum = [0] * (n + 2)
        prefix_sum[1] = 1

        left = 0
        max_dq = collections.deque()
        min_dq = collections.deque()

        for right in range(n):
            while max_dq and nums[max_dq[-1]] <= nums[right]:
                max_dq.pop()
            max_dq.append(right)

            while min_dq and nums[min_dq[-1]] >= nums[right]:
                min_dq.pop()
            min_dq.append(right)

            while nums[max_dq[0]] - nums[min_dq[0]] > k:
                left += 1
                if max_dq[0] < left:
                    max_dq.popleft()
                if min_dq[0] < left:
                    min_dq.popleft()
            
            current_ways = (prefix_sum[right + 1] - prefix_sum[left] + MOD) % MOD
            dp[right + 1] = current_ways
            prefix_sum[right + 2] = (prefix_sum[right + 1] + dp[right + 1]) % MOD

        return dp[n]