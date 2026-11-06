
from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        # Frequency of each value
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # cnt[g] = numbers divisible by g
        cnt = [0] * (mx + 1)
        for g in range(1, mx + 1):
            for multiple in range(g, mx + 1, g):
                cnt[g] += freq[multiple]

        # exact[g] = pairs having gcd exactly g
        exact = [0] * (mx + 1)
        for g in range(mx, 0, -1):
            c = cnt[g]
            exact[g] = c * (c - 1) // 2
            for multiple in range(2 * g, mx + 1, g):
                exact[g] -= exact[multiple]

        # Prefix sum of pair counts
        prefix = [0] * (mx + 1)
        for g in range(1, mx + 1):
            prefix[g] = prefix[g - 1] + exact[g]

        ans = []
        for q in queries:
            ans.append(bisect_right(prefix, q))

        return ans