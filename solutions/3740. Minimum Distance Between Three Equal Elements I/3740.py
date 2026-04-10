class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = {}
        ans = float('inf')

        for i, x in enumerate(nums):
            if x not in pos:
                pos[x] = []
            pos[x].append(i)

        for indices in pos.values():
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    ans = min(ans, 2 * (indices[i + 2] - indices[i]))

        return ans if ans != float('inf') else -1