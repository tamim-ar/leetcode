class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        res = 0
        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if mat[i][j] else 0
            stack = []
            sum_ = 0
            for j in range(n):
                cnt = 1
                while stack and stack[-1][0] >= heights[j]:
                    h, c = stack.pop()
                    sum_ -= h * c
                    cnt += c
                sum_ += heights[j] * cnt
                res += sum_
                stack.append((heights[j], cnt))
        return res
