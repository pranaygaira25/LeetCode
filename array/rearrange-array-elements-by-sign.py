class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)
        result = [0] * n
        
        pos_index = 0
        neg_index = 1
        
        for num in nums:
            if num > 0:
                result[pos_index] = num
                pos_index += 2
            else:
                result[neg_index] = num
                neg_index += 2
        
        return result