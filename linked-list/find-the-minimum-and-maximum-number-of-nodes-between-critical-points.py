class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next
        index = 1

        first = -1
        last = -1
        min_dist = float('inf')
        max_dist = 0

        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):

                if first == -1:
                    first = index
                else:
                    min_dist = min(min_dist, index - last)
                    max_dist = index - first

                last = index

            prev = curr
            curr = curr.next
            index += 1

        if first == last:
            return [-1, -1]

        return [min_dist, max_dist]