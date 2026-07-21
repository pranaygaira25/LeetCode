class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        pairs = sorted((x, i) for i, x in enumerate(nums))

        LOG = 20
        jump = [[0] * LOG for _ in range(n)]

        r = n - 1
        for l in range(n - 1, -1, -1):
            while pairs[r][0] - pairs[l][0] > maxDiff:
                r -= 1

            i = pairs[l][1]
            j = pairs[r][1]

            jump[i][0] = j
            for k in range(1, LOG):
                jump[i][k] = jump[jump[i][k - 1]][k - 1]

        ans = []

        for u, v in queries:
            if nums[u] > nums[v]:
                u, v = v, u

            if u == v:
                ans.append(0)
                continue

            if nums[u] == nums[v]:
                ans.append(1)
                continue

            dist = 0

            for k in range(LOG - 1, -1, -1):
                if nums[jump[u][k]] < nums[v]:
                    dist += 1 << k
                    u = jump[u][k]

            if nums[jump[u][0]] < nums[v]:
                ans.append(-1)
            else:
                ans.append(dist + 1)

        return ans