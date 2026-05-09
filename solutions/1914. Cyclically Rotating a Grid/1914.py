class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2

        for layer in range(layers):
            elems = []

            top, left = layer, layer
            bottom, right = m - layer - 1, n - layer - 1

            for j in range(left, right + 1):
                elems.append(grid[top][j])

            for i in range(top + 1, bottom):
                elems.append(grid[i][right])

            for j in range(right, left - 1, -1):
                elems.append(grid[bottom][j])

            for i in range(bottom - 1, top, -1):
                elems.append(grid[i][left])

            r = k % len(elems)
            rotated = elems[r:] + elems[:r]

            idx = 0

            for j in range(left, right + 1):
                grid[top][j] = rotated[idx]
                idx += 1

            for i in range(top + 1, bottom):
                grid[i][right] = rotated[idx]
                idx += 1

            for j in range(right, left - 1, -1):
                grid[bottom][j] = rotated[idx]
                idx += 1

            for i in range(bottom - 1, top, -1):
                grid[i][left] = rotated[idx]
                idx += 1

        return grid