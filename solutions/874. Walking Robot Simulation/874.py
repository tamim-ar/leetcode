class Solution:
    def robotSim(self, commands, obstacles):
        obs = set(map(tuple, obstacles))
        
        x = y = 0
        d = 0  # 0=N, 1=E, 2=S, 3=W
        
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        max_dist = 0
        
        for cmd in commands:
            if cmd == -1:
                d = (d + 1) % 4
            elif cmd == -2:
                d = (d + 3) % 4
            else:
                dx, dy = dirs[d]
                for _ in range(cmd):
                    if (x + dx, y + dy) in obs:
                        break
                    x += dx
                    y += dy
                    max_dist = max(max_dist, x*x + y*y)
        
        return max_dist