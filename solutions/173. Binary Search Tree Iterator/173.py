class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.leftmost(root)

    def leftmost(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()

        if node.right:
            self.leftmost(node.right)

        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()