from collections import defaultdict
import bisect

class Solution(object):
    def solveQueries(self, nums, queries):
        n = len(nums)
        
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        res = []
        
        for q in queries:
            arr = pos[nums[q]]
            
            if len(arr) == 1:
                res.append(-1)
                continue
            
            i = bisect.bisect_left(arr, q)
            m = len(arr)
            
            # Circular neighbors
            left = arr[(i - 1) % m]
            right = arr[(i + 1) % m]
            
            d1 = abs(left - q)
            d2 = abs(right - q)
            
            ans = min(
                min(d1, n - d1),
                min(d2, n - d2)
            )
            
            res.append(ans)
        
        return res