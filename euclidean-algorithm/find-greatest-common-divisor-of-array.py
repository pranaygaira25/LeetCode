class Solution(object):
    def findGCD(self, nums):
        mn = min(nums)
        mx = max(nums)

        while mx % mn != 0:
            mx, mn = mn, mx % mn

        return mn