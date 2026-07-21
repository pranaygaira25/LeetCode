class Solution(object):
    def detectCycle(self, head):
        s=f=head 
        while f and f.next:
            s=s.next
            f=f.next.next
            if s == f:
                s = head
                while s!=f:
                    s=s.next
                    f=f.next
                return s
        return None
