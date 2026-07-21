class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rank = {}
        
        # Assign ranks to sorted unique values
        for i, num in enumerate(sorted(set(arr)), 1):
            rank[num] = i
        
        # Build the answer
        return [rank[num] for num in arr]