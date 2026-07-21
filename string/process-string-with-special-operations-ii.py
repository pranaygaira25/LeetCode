class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        lengths = [0] * (len(s) + 1)

        for i, ch in enumerate(s):
            if 'a' <= ch <= 'z':
                lengths[i + 1] = lengths[i] + 1
            elif ch == '*':
                lengths[i + 1] = max(0, lengths[i] - 1)
            elif ch == '#':
                lengths[i + 1] = lengths[i] * 2
            else:  # '%'
                lengths[i + 1] = lengths[i]

        if k >= lengths[-1]:
            return "."

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            prev = lengths[i]

            if 'a' <= ch <= 'z':
                if k == prev:
                    return ch

            elif ch == '*':
                if k == prev:
                    return "."

            elif ch == '#':
                if k >= prev:
                    k -= prev

            else:  # '%'
                if prev:
                    k = prev - 1 - k

        return "."