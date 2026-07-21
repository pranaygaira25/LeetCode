class Solution(object):
    def hasCycle(self, head):
     s=f=head
     while f and f.next:
        s=s.next
        f=f.next.next
        
        if s == f:
         return True
     return False
    
        