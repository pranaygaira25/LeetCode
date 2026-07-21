class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_win = 0
        max_win = 0
        
        for i in nums:
            if i==1:
                curr_win+=1
            else:
                max_win = max(max_win, curr_win)
                curr_win = 0
        
        return max(max_win, curr_win)
        
        