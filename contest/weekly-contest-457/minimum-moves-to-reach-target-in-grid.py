import collections

class Solution:
  def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
    # A queue for BFS and a dictionary to track visited states and distances.
    q = collections.deque([(tx, ty)])
    visited = {(tx, ty): 0}

    while q:
      x, y = q.popleft()

      # Path found, return the total moves.
      if x == sx and y == sy:
        return visited[(x, y)]

      # Stop exploring a path if it has overshot the start coordinates.
      if x < sx or y < sy:
        continue
      
      # --- Corrected Backward Move Logic ---

      # Case 1: y > x
      if y > x:
        # Subcase A: The predecessor is (x, y-x). This is valid only if y <= 2x.
        if y <= 2 * x:
          prev_y = y - x
          if (x, prev_y) not in visited:
            visited[(x, prev_y)] = visited[(x, y)] + 1
            q.append((x, prev_y))
        
        # Subcase B: The predecessor is (x, y/2). This is valid only if y > 2x and y is even.
        # If y > 2x and y is odd, it's an impossible state, so we do nothing.
        elif y % 2 == 0: # This implies y > 2x from the if/elif structure
          prev_y = y // 2
          if (x, prev_y) not in visited:
            visited[(x, prev_y)] = visited[(x, y)] + 1
            q.append((x, prev_y))

      # Case 2: x > y (Symmetrical to the y > x case)
      elif x > y:
        # Subcase A: The predecessor is (x-y, y). This is valid only if x <= 2y.
        if x <= 2 * y:
          prev_x = x - y
          if (prev_x, y) not in visited:
            visited[(prev_x, y)] = visited[(x, y)] + 1
            q.append((prev_x, y))

        # Subcase B: The predecessor is (x/2, y). This is valid only if x > 2y and x is even.
        elif x % 2 == 0: # This implies x > 2y
          prev_x = x // 2
          if (prev_x, y) not in visited:
            visited[(prev_x, y)] = visited[(x, y)] + 1
            q.append((prev_x, y))
            
      # Case 3: x == y
      # A state (c, c) can only be reached from (c, 0) or (0, c).
      elif x > 0: # x == y, and we haven't reached (sx, sy)
        # Add predecessor (x, 0)
        if (x, 0) not in visited:
          visited[(x, 0)] = visited[(x, y)] + 1
          q.append((x, 0))
        # Add predecessor (0, y)
        if (0, y) not in visited:
          visited[(0, y)] = visited[(x, y)] + 1
          q.append((0, y))

    # If the queue is empty and we haven't found the start, it's impossible.
    return -1