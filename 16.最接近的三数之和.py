#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = 3000

        def update(val):
            nonlocal closest
            if abs(val - target) < abs(closest - target):
                closest = val
    
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            second, third = first + 1, n - 1

            while second < third:
                s = nums[first] + nums[second] + nums[third]
                if s == target:
                    return target
                update(s)
                if s > target:
                    k = third - 1
                    while second < k and nums[k] == nums[third]:
                        k -= 1
                    third = k
                else:
                    j = second + 1
                    while j < third and nums[j] == nums[second]:
                        j += 1
                    second = j
        return closest
# @lc code=end

