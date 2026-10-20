class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        # Pass 1: determine next states and mark transitional values
        for r in range(m):
            for c in range(n):
                live_neighbors = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        # 1 was live, -1 was also originally live
                        if abs(board[nr][nc]) == 1:
                            live_neighbors += 1

                # Rule 1 & Rule 3: live cell dies
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1

                # Rule 4: dead cell becomes live
                elif board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2

        # Pass 2: finalize the board to 0s and 1s
        for r in range(m):
            for c in range(n):
                if board[r][c] == -1:
                    board[r][c] = 0
                elif board[r][c] == 2:
                    board[r][c] = 1