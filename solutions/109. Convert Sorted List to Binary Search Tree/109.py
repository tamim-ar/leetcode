class Solution:
    def sortedListToBST(self, head):
        def find_mid(node):
            prev = None
            slow = fast = node
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if prev:
                prev.next = None
            return slow

        if not head:
            return None
        mid = find_mid(head)
        root = TreeNode(mid.val)
        if head != mid:
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root
