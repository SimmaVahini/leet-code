class Solution(object):
    def longestPalindrome(self, s):
        if s == s[::-1]:
            return s
            
        start = 0
        max_len = 0

        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_len = r - l + 1
                if curr_len > max_len:
                    max_len = curr_len
                    start = l
                l -= 1
                r += 1

            # Even length palindromes (e.g., "abba")
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_len = r - l + 1
                if curr_len > max_len:
                    max_len = curr_len
                    start = l
                l -= 1
                r += 1

        return s[start : start + max_len]
