class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def gcdSum(self, nums):
        prefixGcd = []
        mx = 0

        # Construct prefixGcd
        for x in nums:
            if x > mx:
                mx = x
            prefixGcd.append(self.gcd(x, mx))

        # Sort
        prefixGcd.sort()

        # Pair smallest with largest
        ans = 0
        i, j = 0, len(prefixGcd) - 1
        while i < j:
            ans += self.gcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1

        return ans