#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def expandAroundCenter(self, s: str, left: int, right: int) -> tuple[int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        n = len(s)
        max_len = 0

        for i in range(n):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)

            if right1 - left1 + 1 > max_len:
                max_len = right1 - left1 + 1
                start, end = left1, right1
            
            if right2 - left2 + 1 > max_len:
                max_len = right2 - left2 + 1
                start, end = left2, right2
            
        return s[start:end + 1]
# @lc code=end

