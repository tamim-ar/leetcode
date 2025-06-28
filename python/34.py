class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findLeft():
            left, right = 0, len(nums) - 1
            pos = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    if nums[mid] == target:
                        pos = mid
                    right = mid - 1
            return pos

        def findRight():
            left, right = 0, len(nums) - 1
            pos = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    if nums[mid] == target:
                        pos = mid
                    left = mid + 1
            return pos

        return [findLeft(), findRight()]
