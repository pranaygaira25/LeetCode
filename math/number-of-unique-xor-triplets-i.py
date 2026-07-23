class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 3:
            return n

        x = 1
        while x <= n:
            x <<= 1

        return x