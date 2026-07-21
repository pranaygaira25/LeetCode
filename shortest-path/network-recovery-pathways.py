class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        from collections import deque

        n = len(online)
        graph = [[] for _ in range(n)]
        indeg = [0] * n
        costs = []

        for u, v, w in edges:
            graph[u].append((v, w))
            indeg[v] += 1
            costs.append(w)

        topo = []
        q = deque(i for i in range(n) if indeg[i] == 0)
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        def check(x):
            INF = 10 ** 30
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue
                if u != 0 and u != n - 1 and not online[u]:
                    continue
                for v, w in graph[u]:
                    if w < x:
                        continue
                    if v != n - 1 and not online[v]:
                        continue
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w

            return dist[n - 1] <= k

        if not check(0):
            return -1

        lo, hi = 0, max(costs)
        ans = 0

        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans