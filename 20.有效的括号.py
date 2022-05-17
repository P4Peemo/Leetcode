#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        valid_pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            if c in "([{":
                stack.append(c)
            elif c in ")]}":
                if not stack or stack[-1] != valid_pairs[c]:
                    return False
                else:
                    stack.pop()
        return not stack

# @lc code=end

