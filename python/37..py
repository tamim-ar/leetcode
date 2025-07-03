class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def isValid(r, c, val):
            for i in range(9):
                if board[r][i] == val or board[i][c] == val or board[3*(r//3)+i//3][3*(c//3)+i%3] == val:
                    return False
            return True

        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for val in map(str, range(1, 10)):
                            if isValid(r, c, val):
                                board[r][c] = val
                                if solve():
                                    return True
                                board[r][c] = '.'
                        return False
            return True

        solve()
