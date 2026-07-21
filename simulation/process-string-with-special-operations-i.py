class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []

        for ch in s:
            if ch.isalpha():
                res.append(ch)
            elif ch == '*':
                if res:
                    res.pop()
            elif ch == '#':
                res.extend(res)
            elif ch == '%':
                res.reverse()

        return ''.join(res)