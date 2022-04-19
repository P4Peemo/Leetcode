#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = dict()
        for i, num in enumerate(nums):
            conjugate = target - num
            if (index := table.get(num, -1)) >= 0:
                return [index, i]
            else:
                table[conjugate] = i
        return []
# @lc code=end

