class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        vals = [1 if x == target else -1 for x in nums]

        pre = [0]
        s = 0
        for v in vals:
            s += v
            pre.append(s)

        comp = sorted(set(pre))
        idx = {v: i + 1 for i, v in enumerate(comp)}

        bit = [0] * (len(comp) + 2)

        def update(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def query(i):
            res = 0
            while i:
                res += bit[i]
                i -= i & -i
            return res

        ans = 0
        for p in pre:
            pos = idx[p]
            ans += query(pos - 1)
            update(pos)

        return ans