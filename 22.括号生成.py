#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(combination, left, right):
            if len(combination) == 2 * n:
                ans.append(''.join(combination))
                return
            
            if left < n:
                combination.append('(')
                backtrack(combination, left+1, right)
                combination.pop()
            if right < left:
                combination.append(')')
                backtrack(combination, left, right+1)
                combination.pop()

        backtrack([], 0, 0)
        return ans
# @lc code=end

