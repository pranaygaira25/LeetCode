class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        
        return 1 + max(left_height, right_height)