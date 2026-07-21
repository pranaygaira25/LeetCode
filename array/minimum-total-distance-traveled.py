class Solution:
    def minimumTotalDistance(self, rob, fac):
        
        rob.sort()
        fac.sort()

        m, n = len(fac), len(rob)
        dp = [0] + [float('inf')] * n
                
        for j, (f,l) in enumerate(fac):
            for _ in range(l):
                for i, r in reversed(list(enumerate(rob))):
                    dp[i+1] = min(abs(f-r) + dp[i], dp[i+1])

        return dp[-1]