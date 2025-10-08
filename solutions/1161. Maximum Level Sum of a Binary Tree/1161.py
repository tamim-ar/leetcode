from collections import deque

class Solution:
    def maxLevelSum(self, root):
        q = deque([root])
        level = 1
        max_sum = float('-inf')
        ans = 1

        while q:
            s = 0
            for _ in range(len(q)):
                node = q.popleft()
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if s > max_sum:
                max_sum = s
                ans = level
            level += 1
        return ans
