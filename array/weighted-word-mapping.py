class Solution(object):
    def mapWordWeights(self, words, weights):
        ans = []

        for word in words:
            s = 0
            for c in word:
                s += weights[ord(c) - ord('a')]

            s %= 26
            ans.append(chr(ord('a') + (25 - s)))

        return ''.join(ans)