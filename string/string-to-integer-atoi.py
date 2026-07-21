class Solution(object):
    def myAtoi(self, s):
        s = s.strip()  # remove leading/trailing spaces
        if not s:
            return 0

        sign = 1
        i = 0
        result = 0

        # check sign
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        # process digits
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result *= sign

        # 32-bit integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result
