class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n, m, res = len(grid), len(grid[0]), 0
        for r in range(n):
            for c in range(m):
                # skip cells with value 0 or visited cells
                if grid[r][c] == 0: continue
                # the init total value of the current island
                v = grid[r][c]
                # mark the starting cell as visited
                grid[r][c] = 0
                # initialize the stack for iterative DFS
                st = [(r, c)]
                while st:
                    x, y = st.pop()
                    # explore the four adjacent cells
                    for next_x, next_y in (
                        (x + 1, y), (x - 1, y),
                        (x, y + 1), (x, y - 1)
                    ):
                        # check bounds and look for unvisited land
                        if (
                            0 <= next_x < n
                            and 0 <= next_y < m
                            and grid[next_x][next_y]
                        ):
                            # add the neighbor's value to the island total
                            v += grid[next_x][next_y]
                            # mark visited before pushing to avoid duplicates
                            grid[next_x][next_y] = 0
                            st.append((next_x, next_y))
                # count the island if its total is divisible by k
                res += v % k == 0
        return res