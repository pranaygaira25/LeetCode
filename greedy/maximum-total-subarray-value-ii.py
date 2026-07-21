import heapq

class Solution(object):
    def maxTotalValue(self, nums, k):
        n = len(nums)

        # Sparse tables for range max/min
        LOG = n.bit_length()

        mx = [[0] * n for _ in range(LOG)]
        mn = [[0] * n for _ in range(LOG)]

        for i in range(n):
            mx[0][i] = nums[i]
            mn[0][i] = nums[i]

        j = 1
        while (1 << j) <= n:
            half = 1 << (j - 1)
            limit = n - (1 << j) + 1

            for i in range(limit):
                mx[j][i] = max(mx[j - 1][i],
                               mx[j - 1][i + half])
                mn[j][i] = min(mn[j - 1][i],
                               mn[j - 1][i + half])
            j += 1

        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1

        def value(l, r):
            length = r - l + 1
            p = lg[length]
            mxv = max(mx[p][l], mx[p][r - (1 << p) + 1])
            mnv = min(mn[p][l], mn[p][r - (1 << p) + 1])
            return mxv - mnv

        # Max heap: (-value, l, r)
        heap = []
        for l in range(n):
            v = value(l, n - 1)
            heapq.heappush(heap, (-v, l, n - 1))

        ans = 0

        for _ in range(k):
            neg_v, l, r = heapq.heappop(heap)
            ans += -neg_v

            if r > l:
                nr = r - 1
                heapq.heappush(heap, (-value(l, nr), l, nr))

        return ans