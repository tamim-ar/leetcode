from typing import List
from collections import deque


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        start = None
        litter_id = {}
        k = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = k
                    k += 1

        full_mask = (1 << k) - 1

        # best[(r, c, mask)] = maximum remaining energy seen
        best = {}

        q = deque()
        q.append((start[0], start[1], 0, energy, 0))
        best[(start[0], start[1], 0)] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, mask, remaining, moves = q.popleft()

            if mask == full_mask:
                return moves

            if remaining == 0:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    nr < 0 or nr >= m or
                    nc < 0 or nc >= n or
                    classroom[nr][nc] == 'X'
                ):
                    continue

                new_remaining = remaining - 1
                new_mask = mask

                # Collect litter
                if (nr, nc) in litter_id:
                    new_mask |= 1 << litter_id[(nr, nc)]

                # Reset energy
                if classroom[nr][nc] == 'R':
                    new_remaining = energy

                key = (nr, nc, new_mask)

                # Only visit if we reach this state with MORE energy
                if new_remaining > best.get(key, -1):
                    best[key] = new_remaining
                    q.append(
                        (nr, nc, new_mask, new_remaining, moves + 1)
                    )

        return -1