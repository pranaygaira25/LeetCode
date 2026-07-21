class Solution(object):
    def maximumWealth(self, accounts):
        ans = 0 
        for accounts in accounts:
            ans= max(ans,sum(accounts))
        return ans 
