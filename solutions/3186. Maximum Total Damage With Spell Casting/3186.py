class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        nums = sorted(freq.keys())
        dp = [0] * (len(nums) + 1)
        
        for i, num in enumerate(nums):
            val = num * freq[num]
            j = i - 1
            while j >= 0 and nums[j] >= num - 2:
                j -= 1
            dp[i + 1] = max(dp[i], dp[j + 1] + val)
        return dp[-1]
