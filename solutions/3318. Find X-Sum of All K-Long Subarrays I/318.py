class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n - k + 1):
            sub = nums[i:i + k]
            freq = Counter(sub)
            top = sorted(freq.items(), key=lambda a: (-a[1], -a[0]))[:x]
            keep = {v for v, _ in top}
            res.append(sum(v for v in sub if v in keep))
        return res
