class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def rev(x):
            return int(str(x)[::-1])
        
        last_seen = {}
        ans = float('inf')
        
        for i, num in enumerate(nums):
            if num in last_seen:
                ans = min(ans, i - last_seen[num])
            
            r = rev(num)
            last_seen[r] = i
        
        return ans if ans != float('inf') else -1