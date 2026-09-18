class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = n // 4
        count = {c: s.count(c) for c in "QWER"}
        if all(count[c] == target for c in "QWER"):
            return 0
        ans = n
        left = 0
        for right in range(n):
            count[s[right]] -= 1
            while left <= right and all(count[c] <= target for c in "QWER"):
                ans = min(ans, right - left + 1)
                count[s[left]] += 1
                left += 1
        return ans