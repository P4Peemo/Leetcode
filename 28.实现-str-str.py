#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if n == 0:
            return 0
        pi = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and needle[j] != needle[i]:
                j = pi[j - 1]
            if needle[j] == needle[i]:
                j += 1
            pi[i] = j
        j = 0
        for i in range(m):
            while j > 0 and haystack[i] != needle[j]:
                j = pi[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == n:
                return i - n + 1
        return -1
# @lc code=end

