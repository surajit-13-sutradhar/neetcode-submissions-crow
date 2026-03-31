class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] is true is the substring s[i...j] is a palindrome
        # s[i...j] is a palindrome if
        # the end characters match s[i] == s[j]
        # and inside part is also a palindrome dp[i + 1][j - 1]

        resIdx, resLen = 0, 0
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1): # n-1 to 0
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

                    # get the staring point and the length of 
                    # the current largest palindrome
                    if resLen < (j - i + 1):
                        resIdx = i 
                        resLen = j - i + 1

        return s[resIdx: resIdx + resLen]
