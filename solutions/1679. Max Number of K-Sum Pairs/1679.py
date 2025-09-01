class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import Counter
        count = Counter(nums)
        ops = 0
        
        for num in list(count.keys()):
            target = k - num
            if target not in count:
                continue
            if num == target:
                ops += count[num] // 2
            else:
                pairs = min(count[num], count[target])
                ops += pairs
                count[num] -= pairs
                count[target] -= pairs
        return ops
