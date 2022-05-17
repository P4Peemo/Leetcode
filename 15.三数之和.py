#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        
        nums.sort()

        for i, first in enumerate(nums):
            if i > 0 and first == nums[i - 1]:
                continue
            k = n - 1
            for j, second in enumerate(nums[i+1:], i + 1):
                if j > i + 1 and second == nums[j - 1]:
                    continue

                while second + nums[k] > -first and j < k:
                    k -= 1
                if j == k:
                    break
                if second + nums[k] == -first:
                    result.append((first, second, nums[k]))
        
        return result

# @lc code=end

