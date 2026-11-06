class Solution:
    def resultArray(self, nums, k):
        dp = [0] * k
        ans = [0] * k

        for num in nums:
            r = num % k
            new = [0] * k
            new[r] += 1

            for x in range(k):
                new[(x * r) % k] += dp[x]

            dp = new

            for x in range(k):
                ans[x] += dp[x]

        return ans