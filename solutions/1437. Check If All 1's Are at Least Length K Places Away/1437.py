class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -1
        for i, v in enumerate(nums):
            if v == 1:
                if prev != -1 and i - prev - 1 < k:
                    return False
                prev = i
        return True
