import collections

class Solution:
  def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
    q = collections.deque([(tx, ty)])
    visited = {(tx, ty): 0}

    while q:
      x, y = q.popleft()

      if x == sx and y == sy:
        return visited[(x, y)]

      if x < sx or y < sy:
        continue

      if y > x:
        if y <= 2 * x:
          prev_y = y - x
          if (x, prev_y) not in visited:
            visited[(x, prev_y)] = visited[(x, y)] + 1
            q.append((x, prev_y))
        elif y % 2 == 0:
          prev_y = y // 2
          if (x, prev_y) not in visited:
            visited[(x, prev_y)] = visited[(x, y)] + 1
            q.append((x, prev_y))

      elif x > y:
        if x <= 2 * y:
          prev_x = x - y
          if (prev_x, y) not in visited:
            visited[(prev_x, y)] = visited[(x, y)] + 1
            q.append((prev_x, y))
        elif x % 2 == 0:
          prev_x = x // 2
          if (prev_x, y) not in visited:
            visited[(prev_x, y)] = visited[(x, y)] + 1
            q.append((prev_x, y))

      elif x > 0:
        if (x, 0) not in visited:
          visited[(x, 0)] = visited[(x, y)] + 1
          q.append((x, 0))
        if (0, y) not in visited:
          visited[(0, y)] = visited[(x, y)] + 1
          q.append((0, y))

    return -1
