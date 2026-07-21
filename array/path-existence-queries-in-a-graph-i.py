class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        arr = sorted((nums[i], i) for i in range(n))

        comp = [0] * n
        cid = 0

        comp[arr[0][1]] = cid

        for i in range(1, n):
            if arr[i][0] - arr[i - 1][0] > maxDiff:
                cid += 1
            comp[arr[i][1]] = cid

        ans = []
        for u, v in queries:
            ans.append(comp[u] == comp[v])

        return ans