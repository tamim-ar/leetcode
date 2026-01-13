class Solution:
    def separateSquares(self, squares):
        events = []
        total = 0.0
        for x, y, l in squares:
            events.append((y, l))
            events.append((y + l, -l))
            total += l * l

        events.sort()
        target = total / 2.0

        curr = 0.0
        area = 0.0
        prev_y = events[0][0]

        for y, delta in events:
            if curr > 0:
                added = curr * (y - prev_y)
                if area + added >= target:
                    return prev_y + (target - area) / curr
                area += added
            curr += delta
            prev_y = y

        return prev_y
