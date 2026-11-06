
class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])
        count = {}
        ans = [0] * len(queries)
        left = right = 0
        m = len(logs)
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        for q, idx in sorted_queries:
            start = q - x
            while right < m and logs[right][1] <= q:
                server = logs[right][0]
                count[server] = count.get(server, 0) + 1
                right += 1
            while left < right and logs[left][1] < start:
                server = logs[left][0]
                count[server] -= 1
                if count[server] == 0:
                    del count[server]
                left += 1
            ans[idx] = n - len(count)
        return ans
