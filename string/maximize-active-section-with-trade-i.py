class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')
        n = len(s)

        zero_blocks = []
        one_blocks = []

        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1

            if s[i] == '0':
                zero_blocks.append(j - i)
            else:
                one_blocks.append(j - i)

            i = j

        if not zero_blocks or not one_blocks:
            return ones

        return ones + max(zero_blocks) - min(one_blocks)