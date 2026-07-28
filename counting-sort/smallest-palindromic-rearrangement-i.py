from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = Counter(s)
        
        first_half = []
        middle = ""
        
        # Build the first half in sorted order
        for ch in sorted(cnt.keys()):
            first_half.append(ch * (cnt[ch] // 2))
            if cnt[ch] % 2 == 1:
                middle = ch
        
        first_half = "".join(first_half)
        
        # Palindrome = first half + middle + reverse(first half)
        return first_half + middle + first_half[::-1]