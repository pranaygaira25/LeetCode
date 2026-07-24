class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1

        # All distinct XORs of two different elements
        pair_xor = set()
        for i in range(n):
            for j in range(i + 1, n):
                pair_xor.add(nums[i] ^ nums[j])

        # Form triplets by XORing every pair XOR with every element
        ans = set(nums)  # covers i == j == k
        for x in pair_xor:
            for v in nums:
                ans.add(x ^ v)

        return len(ans)