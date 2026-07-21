
class Solution(object):
    def middleNode(self, head):
        s=f=head  
        while f and f.next:
          s=s.next
          f=f.next.next
        return s
    