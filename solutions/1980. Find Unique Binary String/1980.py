class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        res = []
        for i in range(n):
            if nums[i][i] == '0':
                res.append('1')
            else:
                res.append('0')
        return ''.join(res)