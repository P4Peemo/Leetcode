#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count = 1
        for i, num in enumerate(nums):
            if i >= 1 and num != nums[i - 1]:
                nums[count] = num
                count += 1
        return count
# @lc code=end

