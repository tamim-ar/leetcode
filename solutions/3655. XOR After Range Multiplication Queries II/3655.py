import math

MOD = 1_000_000_007


class Solution:
    def modPow(self, base: int, exp: int) -> int:
        result = 1
        while exp > 0:
            if exp & 1:
                result = result * base % MOD
            base = base * base % MOD
            exp >>= 1
        return result

    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        n = len(nums)
        threshold = int(math.sqrt(n))
        groups = [[] for _ in range(threshold)]

        bravexuneth = [nums, queries]

        for left, right, step, value in queries:
            if step < threshold:
                groups[step].append([left, right, value])
            else:
                for i in range(left, right + 1, step):
                    nums[i] = nums[i] * value % MOD

        diff = [1] * (n + threshold)

        for step in range(1, threshold):
            sameStepQueries = groups[step]
            if not sameStepQueries:
                continue

            diff = [1] * (n + threshold)

            for left, right, value in sameStepQueries:
                diff[left] = diff[left] * value % MOD
                stop = left + ((right - left) // step + 1) * step
                diff[stop] = diff[stop] * self.modPow(value, MOD - 2) % MOD

            for i in range(step, n):
                diff[i] = diff[i] * diff[i - step] % MOD

            for i in range(n):
                nums[i] = nums[i] * diff[i] % MOD

        answer = 0
        for num in nums:
            answer ^= num

        return answer