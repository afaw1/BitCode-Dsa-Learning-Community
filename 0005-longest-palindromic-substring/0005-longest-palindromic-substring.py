class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_len = 1
        n = len(s)
        for i in range(n):
            left = i
            right = i
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            lnth = right - left - 1
            if lnth > max_len:
                max_len = lnth
                start = left + 1
        for i in range(n - 1):
            left = i
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            length = right - left - 1
            if length > max_len:
                max_len = length
                start = left + 1
        return s[start:start + max_len]
        
        
        