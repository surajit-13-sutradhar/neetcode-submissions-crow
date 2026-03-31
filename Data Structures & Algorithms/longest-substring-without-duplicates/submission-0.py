class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() # to keep track of occured characters
        l = 0
        res = 0

        for r in range(len(s)):
            # before adding the next character to the charset
            # check if it already exists in the set
            # if it is, first remove element pointed by
            # the left pointer till it isn't
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res