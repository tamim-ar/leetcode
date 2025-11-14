class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = second = prev = None
        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            if prev and prev.val > node.val:
                if not first:
                    first = prev
                second = node

            prev = node
            node = node.right

        first.val, second.val = second.val, first.val
