class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empty.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def dfs(i):
            if i == len(empty):
                return True
            r, c = empty[i]
            b = (r // 3) * 3 + (c // 3)
            for val in map(str, range(1, 10)):
                if val not in rows[r] and val not in cols[c] and val not in boxes[b]:
                    board[r][c] = val
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[b].add(val)

                    if dfs(i + 1):
                        return True

                    board[r][c] = '.'
                    rows[r].remove(val)
                    cols[c].remove(val)
                    boxes[b].remove(val)
            return False

        dfs(0)
