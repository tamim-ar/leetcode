from collections import deque

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i == n - 1:
                    res.append(node.val)
        return res
