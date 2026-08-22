class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = [0] * 51

        for i in range(len(nums) - k + 1):
            seen = set()

            for j in range(i, i + k):
                if nums[j] not in seen:
                    count[nums[j]] += 1
                    seen.add(nums[j])

        for i in range(50, -1, -1):
            if count[i] == 1:
                return i

        return -1