class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = n + 1
        best = [INF] * n
        ans = INF
        prefix = 0
        seen = {0: -1}
        shortest = INF
        for i in range(n):
            prefix += arr[i]
            if prefix - target in seen:
                start = seen[prefix - target]
                length = i - start + 1
                if start >= 0:
                    ans = min(ans, length + best[start - 1])
                shortest = min(shortest, length)
            best[i] = shortest
            seen[prefix] = i
        return -1 if ans == INF else ans