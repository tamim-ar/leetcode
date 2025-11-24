class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        cur = 0
        for b in nums:
            cur = (cur * 2 + b) % 5
            ans.append(cur == 0)
        return ans
