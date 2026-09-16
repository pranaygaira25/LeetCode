class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        ans = 1
        r = 2 * k
        m = n + k - 1

        for i in range(1, r + 1):
            ans = ans * (m - r + i) // i

        return ans % MOD