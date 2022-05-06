#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n, r = len(s), numRows
        if r == 1 or r >= n:
            return s

        period = 2 * r - 2

        ans = []

        for i in range(r):
            for j in range(0, n - i, period):
                ans.append(s[j + i])
                if 0 < i < r - 1 and j + period - i < n:
                    ans.append(s[j + period - i])
        return ''.join(ans)

# @lc code=end

