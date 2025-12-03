import math
from collections import defaultdict, Counter

class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        n = len(points)
        # Map slope (dx, dy) → list of segments (i, j)
        slope2segs = defaultdict(list)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                # normalize slope
                if dx == 0:
                    dx_norm, dy_norm = 0, 1
                elif dy == 0:
                    dx_norm, dy_norm = 1, 0
                else:
                    g = math.gcd(dx, dy)
                    dx_norm = dx // g
                    dy_norm = dy // g
                    # keep unique representation (force dx_norm > 0, or dx_norm==0 and dy_norm>0)
                    if dx_norm < 0:
                        dx_norm = -dx_norm
                        dy_norm = -dy_norm
                    elif dx_norm == 0 and dy_norm < 0:
                        dy_norm = -dy_norm
                slope2segs[(dx_norm, dy_norm)].append((i, j))

        total = 0
        # count all pairs of segments with same slope → potential trapezoids (parallel sides)
        for segs in slope2segs.values():
            m = len(segs)
            total += m * (m - 1) // 2

        # subtract parallelograms (which we counted twice)
        mid_slope_count = Counter()
        for slope, segs in slope2segs.items():
            for (i, j) in segs:
                x1, y1 = points[i]
                x2, y2 = points[j]
                mx = x1 + x2  # doubled midpoint x (to stay integer)
                my = y1 + y2  # doubled midpoint y
                mid_slope_count[(mx, my, slope)] += 1

        parallelograms = 0
        for cnt in mid_slope_count.values():
            if cnt >= 2:
                parallelograms += cnt * (cnt - 1) // 2

        return total - parallelograms
