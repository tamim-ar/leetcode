from collections import Counter
import heapq

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []
        cnt = Counter(nums[:k])

        def get_x_sum():
            freq = sorted(cnt.items(), key=lambda y: (-y[1], -y[0]))
            top = freq[:x]
            return sum(v * c for v, c in top)

        ans.append(get_x_sum())

        for i in range(k, n):
            left = nums[i - k]
            cnt[left] -= 1
            if cnt[left] == 0:
                del cnt[left]
            cnt[nums[i]] += 1
            ans.append(get_x_sum())
        return ans
