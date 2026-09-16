class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [1] * (k + 1)

        for i in range(1, n):
            for j in range(1, k + 1):
                dp[j] = (dp[j] + dp[j - 1]) % MOD

        return dp[k]