#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occurrence = set()
        n = len(s)
        r, max_len = -1, 0
        for i in range(n):
            if i != 0:
                occurrence.remove(s[i - 1])
            while r + 1 < n and s[r + 1] not in occurrence:
                occurrence.add(s[r + 1])
                r += 1
            
            max_len = max(max_len, r - i + 1)
        
        return max_len
# @lc code=end

