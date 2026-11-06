
class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2
        diff.sort(reverse=True)
        diff.append(0)

        if sum(diff) <= k:
            return 0

        n = len(nums1)

        for i in range(n):
            count = i + 1
            need = (diff[i] - diff[i + 1]) * count

            if k >= need:
                k -= need
            else:
                level = diff[i] - k // count
                rem = k % count
                ans = sum(x * x for x in diff[i + 1:n])
                ans += (count - rem) * level * level
                ans += rem * (level - 1) * (level - 1)
                return ans

        return 0
