class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        n = len(bottomLeft)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                x1 = max(bottomLeft[i][0], bottomLeft[j][0])
                y1 = max(bottomLeft[i][1], bottomLeft[j][1])
                x2 = min(topRight[i][0], topRight[j][0])
                y2 = min(topRight[i][1], topRight[j][1])
                if x2 > x1 and y2 > y1:
                    side = min(x2 - x1, y2 - y1)
                    ans = max(ans, side * side)
        return ans
