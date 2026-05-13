class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b) + 1
            high = max(a, b) + limit
            s = a + b

            diff[2] += 2
            diff[low] -= 1
            diff[s] -= 1
            diff[s + 1] += 1
            diff[high + 1] += 1

        ans = float('inf')
        cur = 0

        for x in range(2, 2 * limit + 1):
            cur += diff[x]
            ans = min(ans, cur)

        return ans