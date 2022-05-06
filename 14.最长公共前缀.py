#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ''
        for i, c in enumerate(strs[0]):
            for s in strs:
                if i >= len(s) or s[i] != c:
                    return longest_prefix
            longest_prefix += c
        return longest_prefix
# @lc code=end

