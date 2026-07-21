class Solution(object):
    def sortArrayByParity(self, n):
        k = 0
        for i in range(len(n)):
            if n[i] % 2 == 0:
                n[i], n[k] = n[k],n[i]
                k += 1
        return n