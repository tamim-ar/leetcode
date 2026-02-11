from typing import List
from collections import defaultdict

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        evenD = 0
        oddD = 0
        l = 0
        ans = 0

        for r, x in enumerate(nums):
            freq[x] += 1
            if freq[x] == 1:
                if x % 2 == 0:
                    evenD += 1
                else:
                    oddD += 1

            # shrink until we can potentially make evenD == oddD
            # (keep reducing when one side is strictly larger)
            while l <= r and (evenD > oddD or oddD > evenD):
                y = nums[l]
                freq[y] -= 1
                if freq[y] == 0:
                    if y % 2 == 0:
                        evenD -= 1
                    else:
                        oddD -= 1
                l += 1

            if evenD == oddD:
                ans = max(ans, r - l + 1)

        return ans
