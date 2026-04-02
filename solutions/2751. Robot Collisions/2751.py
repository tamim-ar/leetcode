class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        robots = sorted([(positions[i], healths[i], directions[i], i) for i in range(len(positions))])
        
        stack = []
        alive = [True]*len(positions)
        h = healths[:]
        
        for pos, health, d, idx in robots:
            if d == 'R':
                stack.append(idx)
            else:
                while stack and h[idx] > 0:
                    top = stack[-1]
                    
                    if h[top] < h[idx]:
                        alive[top] = False
                        stack.pop()
                        h[idx] -= 1
                    elif h[top] > h[idx]:
                        alive[idx] = False
                        h[top] -= 1
                        break
                    else:
                        alive[top] = False
                        alive[idx] = False
                        stack.pop()
                        break
        
        res = []
        for i in range(len(positions)):
            if alive[i]:
                res.append(h[i])
        
        return res