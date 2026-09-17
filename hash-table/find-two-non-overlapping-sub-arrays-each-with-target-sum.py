class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = n + 1
        best = [INF] * n
        left = 0
        total = 0
        ans = INF

        for right in range(n):
            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            if total == target:
                length = right - left + 1

                if left > 0:
                    ans = min(ans, length + best[left - 1])

                if right > 0:
                    best[right] = min(best[right - 1], length)
                else:
                    best[right] = length
            else:
                if right > 0:
                    best[right] = best[right - 1]

        return -1 if ans == INF else ans