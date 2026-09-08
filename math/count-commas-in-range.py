class Solution:
    def countCommas(self, n: int, m: int) -> int:
        ans = 0
        start = 1000
        commas = 1

        while start <= m:
            end = start * 1000 - 1
            left = max(n, start)
            right = min(m, end)

            if left <= right:
                ans += (right - left + 1) * commas

            start *= 1000
            commas += 1

        return ans