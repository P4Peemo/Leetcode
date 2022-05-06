#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0) or (x > 0 and not x % 10):
            return False
        second_half = 0
        while x > second_half:
            second_half = second_half * 10 + x % 10
            x //= 10
        return x == second_half or x == second_half // 10
# @lc code=end

