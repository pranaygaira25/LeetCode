class Solution(object):
    def mirrorDistance(self, n):
        rev = int(str(n)[::-1])
        return abs(n - rev)
       