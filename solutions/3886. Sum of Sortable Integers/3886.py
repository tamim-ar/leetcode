class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            prev = float("-inf")
            valid = True

            for start in range(0, n, k):
                block = nums[start:start + k]
                drops = [
                    i for i in range(k - 1)
                    if block[i] > block[i + 1]
                ]

                circular_drops = len(drops) + (
                    block[-1] > block[0]
                )

                if circular_drops > 1:
                    valid = False
                    break

                if drops:
                    p = drops[0] + 1
                    block = block[p:] + block[:p]

                if block[0] < prev:
                    valid = False
                    break

                prev = block[-1]

            if valid:
                ans += k

        return ans