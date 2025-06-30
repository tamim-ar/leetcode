class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        max_len = 0
        for key in count:
            if key + 1 in count:
                max_len = max(max_len, count[key] + count[key + 1])
        return max_len
