class Solution:
    def maxActiveSections(self, s: str) -> int:
        ones = s.count('1')
        n = len(s)

        zero_blocks = []
        one_blocks = []

        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            length = j - i
            if s[i] == '0':
                zero_blocks.append(length)
            else:
                one_blocks.append(length)
            i = j

        if not zero_blocks or not one_blocks:
            return ones

        return ones + max(zero_blocks) - min(one_blocks)