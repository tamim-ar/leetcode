class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first = -1
        prev_critical = -1
        min_distance = float('inf')

        prev = head
        curr = head.next
        index = 1

        while curr and curr.next:
            nxt = curr.next

            if (curr.val > prev.val and curr.val > nxt.val) or \
               (curr.val < prev.val and curr.val < nxt.val):

                if first == -1:
                    first = index
                else:
                    min_distance = min(
                        min_distance,
                        index - prev_critical
                    )

                prev_critical = index

            prev = curr
            curr = nxt
            index += 1

        if first == -1 or first == prev_critical:
            return [-1, -1]

        return [min_distance, prev_critical - first]